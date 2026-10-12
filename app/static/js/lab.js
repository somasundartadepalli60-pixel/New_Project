(() => {
  'use strict';
  const $ = (selector) => document.querySelector(selector);
  const modeConfig = {
    opamp: {unit:'UNIT 1 · OPERATIONAL AMPLIFIERS', title:'Inverting amplifier', fields:[['rf','Feedback resistance Rf (Ω)',47000,1,1000000000],['rin','Input resistance Rin (Ω)',10000,1,1000000000],['vin','Input voltage Vin (V)',0.2,-1000,1000],['supply','Symmetric supply rail (V)',5,1,100]], defaults:{rf:47000,rin:10000,vin:0.2,supply:5}},
    timer555: {unit:'UNIT 2 · TIMER APPLICATIONS', title:'555 astable timer', fields:[['ra','Timing resistor RA (Ω)',10000,1,1000000000],['rb','Timing resistor RB (Ω)',10000,1,1000000000],['capacitance_uf','Timing capacitor (µF)',10,0.001,1000000]], defaults:{ra:10000,rb:10000,capacitance_uf:10}},
    adc: {unit:'UNIT 3 · DATA CONVERTERS', title:'ADC quantisation explorer', fields:[['bits','Resolution (bits)',8,1,16],['reference_v','Reference voltage (V)',5,0.001,1000],['vin','Input voltage (V)',2.4,0,5]], defaults:{bits:8,reference_v:5,vin:2.4}},
    logic: {unit:'UNIT 4 · DIGITAL LOGIC', title:'Logic gate explorer', fields:[['gate','Logic gate','AND','AND,OR,XOR,NAND,NOR,XNOR'],['a','Input A',1,0,1],['b','Input B',0,0,1]], defaults:{gate:'AND',a:1,b:0}}
  };
  const diagnosis = {
    clipping:{title:'Check the output range first',body:'Compare the calculated ideal output with the supply rails. Then inspect input amplitude, gain-setting resistors, load conditions, and whether the real op-amp supports the expected input/output swing.',steps:['Estimate Vout from the circuit equation.','Compare the estimate with available supply rails.','Check common-mode range and output swing in the actual IC datasheet.','Reduce gain or input amplitude and rerun the test.']},
    zero:{title:'Trace the signal path',body:'A near-zero output may be consistent with a zero input, missing supply, incorrect feedback path, grounded input, or a wiring/measurement error. Do not assume a single cause from the symptom alone.',steps:['Verify power and ground references.','Measure the input and both input-node voltages.','Inspect resistor connections and feedback continuity.','Test with a known small input signal.']},
    'no-oscillation':{title:'Inspect the timing network',body:'A 555 astable circuit needs the expected timing-resistor/capacitor path, valid supply and reset state, and correct connections. Component selection and wiring determine whether oscillation starts.',steps:['Verify supply and reset pin state.','Check RA, RB, and capacitor values and connections.','Inspect threshold/trigger capacitor node wiring.','Compare observed timing with the approximate equations.']},
    'wrong-code':{title:'Resolution sets the ideal step size',body:'For an ideal N-bit unipolar converter, a common teaching estimate is Vref/2^N per code step. Check the selected resolution, reference voltage, input range, and the convention used to map voltage to code.',steps:['Calculate the number of codes, 2^N.','Calculate the ideal step size from the reference range.','Check whether the input is within the configured range.','Confirm the ADC architecture’s actual transfer convention.']},
    unknown:{title:'Change one variable at a time',body:'A useful diagnosis starts with a reproducible baseline and a controlled experiment. Capture inputs, assumptions, expected output, measured output, and the smallest change that reproduces the symptom.',steps:['Restore the last known-good settings.','Change exactly one parameter.','Record prediction and result.','Check units, limits, model assumptions, and measurement setup.']}
  };
  let mode = 'opamp';
  let lastResult = null;
  let lastPayload = null;
  const notebookKey = 'ldica_virtual_lab_experiments_v1';
  const circuitKey = 'ldica_circuit_design_v1';
  let circuitComponents = [];
  let nextComponentId = 1;
  const componentTypes = {source:{label:'Signal source',pins:['+','−']},resistor:{label:'Resistor',pins:['A','B']},capacitor:{label:'Capacitor',pins:['A','B']},opamp:{label:'Op-amp',pins:['IN−','IN+','OUT','V+','V−']},timer555:{label:'555 timer',pins:['TRIG','THR','DISCH','OUT','VCC','GND','RESET','CTRL']},logic:{label:'Logic gate',pins:['A','B','Y','VCC','GND']},ground:{label:'Ground reference',pins:['GND']},output:{label:'Output probe',pins:['IN']}};
  const safe = (value) => String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  function readNotebook(){try{const value=JSON.parse(localStorage.getItem(notebookKey)||'[]');return Array.isArray(value)?value:[]}catch(_){return []}}
  function writeNotebook(items){localStorage.setItem(notebookKey,JSON.stringify(items.slice(0,100)))}
  function renderFields(useDefaults=true){
    const config=modeConfig[mode]; $('#lab-unit-label').textContent=config.unit; $('#lab-title').textContent=config.title;
    $('#lab-fields').innerHTML=config.fields.map(([key,label,value,min,max])=>{
      if(key==='gate')return `<label class="lab-field" for="field-${key}">${label}<select id="field-${key}" name="${key}">${['AND','OR','XOR','NAND','NOR','XNOR'].map(g=>`<option ${((useDefaults?config.defaults[key]:lastPayload?.[key])===g)?'selected':''}>${g}</option>`).join('')}</select></label>`;
      const current=useDefaults?config.defaults[key]:(lastPayload?.[key]??value);
      return `<label class="lab-field" for="field-${key}">${label}<input id="field-${key}" name="${key}" type="number" step="any" min="${min}" ${max!==undefined?`max="${max}"`:''} value="${safe(current)}" required></label>`;
    }).join('');
    $('#lab-model-note').textContent = mode==='opamp' ? 'Model assumption: ideal inverting op-amp; output is clipped at the selected symmetric supply rails. Real IC limits may be narrower.' : mode==='timer555' ? 'Model assumption: classic 555 astable timing approximations; actual values depend on IC thresholds and component tolerances.' : mode==='adc' ? 'Model assumption: ideal unipolar ADC with floor-based code mapping; real converters may use a different transfer convention.' : 'Model assumption: ideal two-input Boolean gate; propagation delay and electrical loading are not modelled.';
    drawCircuit();
  }
  function drawCircuit(){
    const stage=$('#lab-circuit-stage');
    if(mode==='opamp') stage.innerHTML='<svg viewBox="0 0 640 330" role="img" aria-label="Conceptual inverting amplifier with input resistor and feedback resistor"><g fill="none" stroke="#458f9b" stroke-width="3" stroke-linejoin="round"><path d="M35 125H165M205 125H275M275 125V155H310M310 155L310 95L425 160L310 225Z" fill="#eaf6f4"/><path d="M425 160H560M490 160V55H275V125M35 185H275"/><path d="M185 111V139M185 111H205M185 139H205"/></g><g fill="#172536" font-family="Arial" font-size="15"><text x="35" y="106">Vin</text><text x="165" y="103">Rin</text><text x="332" y="145">−</text><text x="332" y="197">+</text><text x="421" y="43">Rf feedback</text><text x="565" y="165">Vout</text><text x="327" y="255">OP-AMP</text></g></svg>';
    else if(mode==='timer555') stage.innerHTML='<svg viewBox="0 0 640 330" role="img" aria-label="Conceptual 555 astable timing network"><rect x="245" y="65" width="150" height="190" rx="12" fill="#eaf6f4" stroke="#458f9b" stroke-width="3"/><g fill="#172536" font-family="Arial" font-size="15" text-anchor="middle"><text x="320" y="105" font-weight="700">555 TIMER</text><text x="320" y="135">TRIG / THR</text><text x="320" y="160">DISCHARGE</text><text x="320" y="208">OUTPUT</text></g><g fill="none" stroke="#458f9b" stroke-width="3"><path d="M95 80H245M95 80V125M95 125H245M95 125V225H245M395 200H540M540 200V80H395"/></g><g fill="#1c78b7" font-family="Arial" font-size="13"><text x="35" y="65">RA / RB</text><text x="35" y="244">Timing capacitor C</text><text x="495" y="185">Square output</text></g></svg>';
    else if(mode==='adc') stage.innerHTML='<svg viewBox="0 0 640 330" role="img" aria-label="ADC quantisation steps"><path d="M75 255H570M75 255V50" stroke="#7b8b9a" stroke-width="2" fill="none"/><path d="M75 255H145V220H215V185H285V150H355V115H425V80H495V45H565" stroke="#1c78b7" stroke-width="4" fill="none" stroke-linejoin="round"/><path d="M75 235L565 50" stroke="#d39a45" stroke-width="2" stroke-dasharray="6 6"/><g fill="#172536" font-family="Arial" font-size="14"><text x="410" y="290">Input voltage →</text><text x="90" y="35">Digital code</text><text x="430" y="65" fill="#1c78b7">Quantised level</text></g></svg>';
    else stage.innerHTML='<svg viewBox="0 0 640 330" role="img" aria-label="Logic gate inputs and output"><path d="M105 95H225M105 225H225M365 160H525" stroke="#458f9b" stroke-width="4" fill="none"/><path d="M225 70Q340 70 365 160Q340 250 225 250Z" fill="#eaf6f4" stroke="#458f9b" stroke-width="3"/><g fill="#172536" font-family="Arial" font-size="17"><text x="75" y="84">A</text><text x="75" y="215">B</text><text x="535" y="166">Y</text><text x="280" y="166" text-anchor="middle" font-weight="700">GATE</text></g></svg>';
  }
  async function runSimulation(event){
    if(event)event.preventDefault();
    const form=new FormData($('#lab-form')); const payload={mode};
    for(const [key,value] of form.entries()) { if(key==='csrf_token') continue; payload[key]=key==='gate'?value:Number(value); }
    if(mode==='adc' && payload.vin>payload.reference_v){$('#field-vin').setCustomValidity('Input voltage must not exceed the reference voltage.');$('#field-vin').reportValidity();$('#field-vin').setCustomValidity('');return}
    try{
      const token=$('#lab-form input[name=csrf_token]').value;
      const response=await fetch('/lab/simulate',{method:'POST',headers:{'Content-Type':'application/json','X-CSRFToken':token},body:JSON.stringify(payload)});
      const data=await response.json(); if(!response.ok||!data.ok)throw new Error(data.error||'Simulation could not be completed.');
      lastPayload=payload;lastResult=data.result;renderResults(data.result);$('#lab-status').textContent='SIMULATED';
      $('#lab-equation').innerHTML=`<strong>Model relationship</strong><p>${safe(data.result.equation)}</p><span>${safe(data.result.interpretation)}</span>`;
    }catch(error){$('#lab-results').innerHTML=`<div class="lab-empty"><strong>Input needs attention</strong><p>${safe(error.message)}</p></div>`;$('#lab-status').textContent='CHECK INPUTS'}
  }
  function formatValue(key,value){
    if(typeof value!=='number')return String(value);
    if(key.includes('_s'))return value>=1?`${value.toPrecision(5)} s`:`${(value*1000).toPrecision(5)} ms`;
    if(key.includes('_v')||key.endsWith('_v'))return `${value.toPrecision(5)} V`;
    if(key==='frequency_hz')return `${value>=1000?(value/1000).toPrecision(5)+' kHz':value.toPrecision(5)+' Hz'}`;
    if(key==='duty_percent')return `${value.toFixed(2)}%`;
    if(key==='gain')return `${value.toFixed(4)}×`;
    if(key==='quantization_error_v')return `${(value*1000).toPrecision(5)} mV`;
    return Number.isInteger(value)?String(value):value.toPrecision(6);
  }
  function renderResults(result){
    const labels={gain:'Closed-loop gain',ideal_output_v:'Ideal output',output_v:'Modelled output',saturated:'Rail clipping',high_s:'Output high time',low_s:'Output low time',period_s:'Period',frequency_hz:'Frequency',duty_percent:'Duty cycle',levels:'Number of codes',lsb_v:'Ideal step size',code_decimal:'Output code (decimal)',code_binary:'Output code (binary)',reconstructed_v:'Reconstructed level',quantization_error_v:'Quantization error',gate:'Selected gate',a:'Input A',b:'Input B',output:'Output'};
    const preferred=Object.keys(labels).filter(key=>key in result);
    $('#lab-results').innerHTML=preferred.map(key=>`<div class="lab-metric"><span>${labels[key]}</span><strong>${safe(key==='saturated'?(result[key]?'Yes':'No'):formatValue(key,result[key]))}</strong></div>`).join('')+`<div class="lab-interpretation"><strong>What it means</strong><p>${safe(result.interpretation)}</p></div>`;
  }
  function saveExperiment(){
    if(!lastResult||!lastPayload){$('#lab-status').textContent='RUN A MODEL FIRST';return}
    const items=readNotebook();items.unshift({id:Date.now(),savedAt:new Date().toISOString(),mode,title:modeConfig[mode].title,inputs:lastPayload,result:lastResult,prediction:$('#lab-prediction').value.trim(),observation:$('#lab-observation-text').value.trim()});
    try{writeNotebook(items);renderHistory();$('#lab-status').textContent='SAVED LOCALLY'}catch(_){$('#lab-status').textContent='BROWSER STORAGE FULL'}
  }
  function renderHistory(){const items=readNotebook();const host=$('#lab-history');if(!items.length){host.innerHTML='<p class="muted">No experiments saved in this browser yet.</p>';return}host.innerHTML=items.map(item=>`<article class="lab-history-item"><div><strong>${safe(item.title)}</strong><small>${safe(new Date(item.savedAt).toLocaleString())}</small><p>${safe(item.observation||item.prediction||'No notes recorded.')}</p></div><button class="button secondary small" data-load="${item.id}" type="button">Load</button></article>`).join('');host.querySelectorAll('[data-load]').forEach(button=>button.addEventListener('click',()=>loadExperiment(Number(button.dataset.load))))}
  function loadExperiment(id){const item=readNotebook().find(entry=>entry.id===id);if(!item)return;mode=item.mode;lastPayload=item.inputs;lastResult=item.result;document.querySelectorAll('.lab-mode').forEach(button=>button.classList.toggle('active',button.dataset.mode===mode));renderFields(false);for(const [key,value] of Object.entries(item.inputs)){const input=$(`#field-${key}`);if(input)input.value=value}$('#lab-prediction').value=item.prediction||'';$('#lab-observation-text').value=item.observation||'';renderResults(item.result);$('#lab-equation').innerHTML=`<strong>Model relationship</strong><p>${safe(item.result.equation)}</p><span>${safe(item.result.interpretation)}</span>`;$('#lab-status').textContent='LOADED FROM NOTEBOOK';}
  function exportNotebook(){const blob=new Blob([JSON.stringify({schema:'ldica-lab-notebook-v1',exportedAt:new Date().toISOString(),experiments:readNotebook()},null,2)],{type:'application/json'});const url=URL.createObjectURL(blob);const link=document.createElement('a');link.href=url;link.download='ldica-lab-notebook.json';link.click();URL.revokeObjectURL(url)}
  function diagnose(){const item=diagnosis[$('#lab-fault').value];$('#lab-diagnosis-answer').innerHTML=`<strong>${safe(item.title)}</strong><p>${safe(item.body)}</p><ol>${item.steps.map(step=>`<li>${safe(step)}</li>`).join('')}</ol><small>Guided reasoning only: several causes may produce the same symptom. Verify against the actual circuit and component datasheet.</small>`}
  function addComponent(type, nets={}){
    const definition=componentTypes[type];if(!definition)return;
    const component={id:nextComponentId++,type,name:`${definition.label} ${circuitComponents.filter(item=>item.type===type).length+1}`,nets:{}};
    definition.pins.forEach(pin=>component.nets[pin]=nets[pin]||'');circuitComponents.push(component);renderCircuitBuilder();
  }
  function renderCircuitBuilder(){
    const host=$('#lab-builder-list');if(!circuitComponents.length){host.innerHTML='<p class="muted">No components yet. Load a starter topology or add components above.</p>';return}
    host.innerHTML=circuitComponents.map(component=>{const def=componentTypes[component.type];return `<article class="lab-component" data-component="${component.id}"><div class="lab-component-head"><strong>${safe(component.name)}</strong><button type="button" data-remove-component="${component.id}">Remove component</button></div><div class="lab-component-pins">${def.pins.map(pin=>`<label>${safe(pin)} node<input type="text" maxlength="24" data-component-id="${component.id}" data-pin="${safe(pin)}" value="${safe(component.nets[pin]||'')}" placeholder="e.g. GND"></label>`).join('')}</div></article>`}).join('');
    host.querySelectorAll('[data-remove-component]').forEach(button=>button.addEventListener('click',()=>{circuitComponents=circuitComponents.filter(item=>item.id!==Number(button.dataset.removeComponent));renderCircuitBuilder()}));
    host.querySelectorAll('[data-component-id]').forEach(input=>input.addEventListener('change',()=>{const item=circuitComponents.find(component=>component.id===Number(input.dataset.componentId));if(item)item.nets[input.dataset.pin]=input.value.trim().toUpperCase().replace(/\s+/g,'_')}));
  }
  function loadStarterTopology(){
    const starter=$('#lab-topology').value;circuitComponents=[];nextComponentId=1;
    if(starter==='inverting'){
      addComponent('source',{'+':'IN','−':'GND'});addComponent('resistor',{A:'IN',B:'SUM'});addComponent('opamp',{'IN−':'SUM','IN+':'GND',OUT:'OUT','V+':'VCC','V−':'VEE'});addComponent('resistor',{A:'OUT',B:'SUM'});addComponent('ground',{GND:'GND'});addComponent('output',{IN:'OUT'});
    }else if(starter==='timer555'){
      addComponent('source',{'+':'VCC','−':'GND'});addComponent('resistor',{A:'VCC',B:'DISCH'});addComponent('resistor',{A:'DISCH',B:'TIMING'});addComponent('capacitor',{A:'TIMING',B:'GND'});addComponent('timer555',{TRIG:'TIMING',THR:'TIMING',DISCH:'DISCH',OUT:'OUT',VCC:'VCC',GND:'GND',RESET:'VCC',CTRL:'VCC'});addComponent('ground',{GND:'GND'});addComponent('output',{IN:'OUT'});
    }else if(starter==='logic'){
      addComponent('source',{'+':'A','−':'GND'});addComponent('source',{'+':'B','−':'GND'});addComponent('logic',{A:'A',B:'B',Y:'OUT',VCC:'VCC',GND:'GND'});addComponent('ground',{GND:'GND'});addComponent('output',{IN:'OUT'});
    }
    $('#lab-circuit-report').className='lab-circuit-report';$('#lab-circuit-report').innerHTML='<strong>Starter loaded</strong><p>Inspect the named nets, edit a connection, then validate the topology.</p>';renderCircuitBuilder();
  }
  function validateCircuit(){
    const errors=[],warnings=[],allPins=[];const count=type=>circuitComponents.filter(component=>component.type===type).length;
    circuitComponents.forEach(component=>{const def=componentTypes[component.type];def.pins.forEach(pin=>{const net=(component.nets[pin]||'').trim().toUpperCase();if(!net)errors.push(`${component.name}: pin ${pin} has no node name.`);else allPins.push({net,component:component.name,pin})})});
    if(!circuitComponents.length)errors.push('Add at least one component before validating.');
    const topology=$('#lab-topology').value;
    const required=topology==='inverting'?[['opamp',1,'one op-amp'],['resistor',2,'two resistors'],['source',1,'one signal source'],['ground',1,'a ground reference'],['output',1,'an output probe']]:topology==='timer555'?[['timer555',1,'one 555 timer'],['resistor',2,'two timing resistors'],['capacitor',1,'a timing capacitor'],['ground',1,'a ground reference'],['output',1,'an output probe']]:topology==='logic'?[['logic',1,'one logic gate'],['source',2,'two input sources'],['ground',1,'a ground reference'],['output',1,'an output probe']]:[];
    required.forEach(([type,min,label])=>{if(count(type)<min)errors.push(`This starter expects ${label}; found ${count(type)} ${type} component(s).`)});
    const nets=new Map();allPins.forEach(pin=>nets.set(pin.net,(nets.get(pin.net)||0)+1));
    const exempt=new Set(['GND','VCC','VEE','VDD','VSS','NC']);
    nets.forEach((total,net)=>{if(total===1&&!exempt.has(net))warnings.push(`Node ${net} appears on only one terminal; check whether it should connect to another component.`)});
    if(topology==='inverting'){for(const net of ['SUM','OUT','GND'])if(!nets.has(net))errors.push(`Expected net ${net} is missing from this inverting-amplifier starter.`)}
    if(topology==='timer555'){for(const net of ['TIMING','DISCH','VCC','GND','OUT'])if(!nets.has(net))errors.push(`Expected net ${net} is missing from this 555 starter.`)}
    if(topology==='logic'){for(const net of ['A','B','OUT','GND'])if(!nets.has(net))errors.push(`Expected net ${net} is missing from this logic starter.`)}
    const host=$('#lab-circuit-report');host.className='lab-circuit-report '+(errors.length?'warn':'good');host.innerHTML=`<strong>${errors.length?'Review needed':warnings.length?'Topology checks passed with warnings':'Topology checks passed'}</strong><p>Inspected ${circuitComponents.length} components and ${allPins.length} terminals across ${nets.size} named nodes. This is a structural check, not electrical simulation.</p>${errors.length?`<strong>Errors</strong><ul>${errors.map(item=>`<li>${safe(item)}</li>`).join('')}</ul>`:''}${warnings.length?`<strong>Warnings</strong><ul>${warnings.map(item=>`<li>${safe(item)}</li>`).join('')}</ul>`:''}${!errors.length&&!warnings.length?'<p>Required starter components and expected signal nodes are present.</p>':''}`;
  }
  function saveCircuit(){try{localStorage.setItem(circuitKey,JSON.stringify({topology:$('#lab-topology').value,components:circuitComponents,nextId:nextComponentId,savedAt:new Date().toISOString()}));$('#lab-circuit-report').className='lab-circuit-report good';$('#lab-circuit-report').innerHTML='<strong>Design saved in this browser</strong><p>Your component list and node assignments will be restored when you reopen this page in the same browser profile.</p>'}catch(_){$('#lab-circuit-report').className='lab-circuit-report warn';$('#lab-circuit-report').innerHTML='<strong>Could not save design</strong><p>Browser storage may be disabled or full. Export your experiment notebook for other recorded results.</p>'}}
  function restoreCircuit(){try{const saved=JSON.parse(localStorage.getItem(circuitKey)||'null');if(saved&&Array.isArray(saved.components)){circuitComponents=saved.components;nextComponentId=Number(saved.nextId)||circuitComponents.length+1;$('#lab-topology').value=saved.topology||'blank';renderCircuitBuilder()}}catch(_){circuitComponents=[];renderCircuitBuilder()}}
  document.querySelectorAll('[data-add-component]').forEach(button=>button.addEventListener('click',()=>addComponent(button.dataset.addComponent)));
  $('#lab-load-topology').addEventListener('click',loadStarterTopology);$('#lab-check-circuit').addEventListener('click',validateCircuit);$('#lab-save-circuit').addEventListener('click',saveCircuit);$('#lab-clear-circuit').addEventListener('click',()=>{circuitComponents=[];$('#lab-circuit-report').className='lab-circuit-report';$('#lab-circuit-report').innerHTML='<strong>Design cleared</strong><p>Add a component or load a starter topology.</p>';renderCircuitBuilder()});
  document.querySelectorAll('.lab-mode').forEach(button=>button.addEventListener('click',()=>{mode=button.dataset.mode;document.querySelectorAll('.lab-mode').forEach(item=>item.classList.toggle('active',item===button));lastResult=null;lastPayload=null;renderFields(true);$('#lab-results').innerHTML='<div class="lab-empty"><span>↗</span><strong>Ready when you are</strong><p>Set your inputs and run the simulation to see calculated outputs here.</p></div>';$('#lab-equation').textContent='Equations and assumptions will appear after simulation.';$('#lab-status').textContent='READY'}));
  $('#lab-form').addEventListener('submit',runSimulation);$('#lab-save').addEventListener('click',saveExperiment);$('#lab-diagnose').addEventListener('click',diagnose);$('#lab-export').addEventListener('click',exportNotebook);
  $('#lab-reset').addEventListener('click',()=>{renderFields(true);$('#lab-prediction').value='';$('#lab-observation-text').value='';$('#lab-status').textContent='RESET'});
  $('#lab-fields').addEventListener('change',event=>{if(event.target.name==='gate')drawCircuit()});
  renderFields(true);renderHistory();restoreCircuit();
})();
