(() => {
  const $ = (id) => document.getElementById(id);
  const safeNumber = (id) => {
    const value = Number($(id).value);
    if (!Number.isFinite(value)) throw new Error('Enter finite numeric values.');
    return value;
  };
  const showError = (id, message) => { $(id).textContent = message; };
  const truth = (gate, a, b) => ({AND:a&b, OR:a|b, NOT:1-a, NAND:1-(a&b), NOR:1-(a|b), XOR:a^b, XNOR:1-(a^b)})[gate];
  const gateExplain = {AND:'HIGH only when both inputs are HIGH.',OR:'HIGH when at least one input is HIGH.',NOT:'Inverts input A; input B is ignored.',NAND:'Inverse of AND.',NOR:'Inverse of OR.',XOR:'HIGH when inputs differ.',XNOR:'HIGH when inputs match.'};
  function renderTruthTable() {
    const gate = $('logic-gate').value;
    const a = Number($('logic-a').value), b = Number($('logic-b').value);
    $('logic-output').textContent = String(truth(gate,a,b));
    $('logic-explanation').textContent = gateExplain[gate];
    $('logic-table').innerHTML = [0,1].flatMap(x => [0,1].map(y => ({x,y}))).map(({x,y}) => `<tr><td>${x}</td><td>${y}</td><td><strong>${truth(gate,x,y)}</strong></td></tr>`).join('');
  }
  ['logic-gate','logic-a','logic-b'].forEach(id => $(id).addEventListener('change', renderTruthTable));
  $('logic-evaluate').addEventListener('click', renderTruthTable);
  $('logic-export').addEventListener('click', () => {
    const gate=$('logic-gate').value; const rows=['A,B,Y',...[0,1].flatMap(a=>[0,1].map(b=>`${a},${b},${truth(gate,a,b)}`))];
    const blob=new Blob([rows.join('\n')],{type:'text/csv;charset=utf-8;'}); const url=URL.createObjectURL(blob); const link=document.createElement('a'); link.href=url; link.download=`${gate.toLowerCase()}-truth-table.csv`; link.click(); URL.revokeObjectURL(url);
  });
  function runSequence() {
    const mode=$('sequence-model').value; const pattern=$('sequence-pattern').value.split(',').map(v=>v.trim());
    if (pattern.length>64 || pattern.some(v=>v!=='' && !/^[01]$/.test(v))) { showError('sequence-note','Use at most 64 comma-separated binary values (0 or 1).'); return; }
    let state=0; const width=Number($('counter-width').value); const mask=(1<<width)-1;
    const rows=pattern.filter(v=>v!=='').map((v,index)=>{ const input=Number(v); if(mode==='dff') state=input; else state=(state+1)&mask; return `<tr><td>${index+1}</td><td>${mode==='dff'?input:'Clock edge'}</td><td>${state}</td><td>${state.toString(2).padStart(mode==='dff'?1:width,'0')}</td></tr>`; });
    $('sequence-table').innerHTML=rows.join(''); $('sequence-note').textContent=mode==='dff'?'Q samples D at each simulated active edge. Setup/hold violations and asynchronous controls are not modelled.':`Modulo-${mask+1} binary count, starting at zero; real propagation delays are not modelled.`;
  }
  $('sequence-run').addEventListener('click',runSequence); $('sequence-model').addEventListener('change',runSequence);
  function analogCalculate() {
    try {
      const model=$('analog-model').value, a=safeNumber('analog-a'), b=safeNumber('analog-b'), c=safeNumber('analog-c'); let result, detail;
      if(model==='inverting'){ if(a<=0||b<0) throw new Error('Rin must be positive and Rf cannot be negative.'); result=-(b/a); detail=`Av = −Rf/Rin = −${b}/${a}; phase inversion is represented by the negative sign.`; }
      else if(model==='noninverting'){ if(b<0||a<=0) throw new Error('Rg must be positive and Rf cannot be negative.'); result=1+b/a; detail=`Av = 1 + Rf/Rg = 1 + ${b}/${a}.` }
      else if(model==='timer'){ if(a<=0||b<=0||c<=0) throw new Error('RA, RB and C must all be positive.'); result=1.44/((a+2*b)*c); detail=`Approximate astable frequency f ≈ 1.44 / ((RA + 2RB)C), using ohms and farads.` }
      else if(model==='adc'){ if(a<=0||!Number.isInteger(b)||b<1||b>32) throw new Error('Use positive Vref and an integer bit count from 1 to 32 in the second field.'); result=a/(2**b); detail=`Ideal code step = Vref / 2^N = ${a} / 2^${b}. The third value is ignored for this model.` }
      else { if(a<=0||b<=0) throw new Error('R and C must be positive.'); result=a*b; detail=`τ = RC = ${a} Ω × ${b} F. The third value is ignored for this model.` }
      $('analog-result').textContent=Number.isFinite(result)?Number(result.toPrecision(8)).toLocaleString(undefined,{maximumSignificantDigits:8}):'Out of range'; $('analog-detail').textContent=detail;
    } catch(error) { showError('analog-result','Check inputs'); showError('analog-detail',error.message); }
  }
  $('analog-calculate').addEventListener('click',analogCalculate);
  $('analog-model').addEventListener('change',()=>{const model=$('analog-model').value; const labels={inverting:['Rin (Ω)','Rf (Ω)','Unused'],noninverting:['Rg (Ω)','Rf (Ω)','Unused'],timer:['RA (Ω)','RB (Ω)','C (F)'],adc:['Vref (V)','Bits N','Unused'],rc:['R (Ω)','C (F)','Unused']}; $('analog-label-a').firstChild.textContent=labels[model][0]; $('analog-label-b').firstChild.textContent=labels[model][1]; $('analog-label-c').firstChild.textContent=labels[model][2]; });
  function formulaCalculate() {
    try { const kind=$('formula-choice').value,a=safeNumber('formula-a'),b=safeNumber('formula-b'); let result,detail;
      if(kind==='inv'){if(b<=0)throw new Error('Rin must be greater than zero.');result=-(a/b);detail='Av = −Rf/Rin; both resistance values must use the same unit.'}
      else if(kind==='noninv'){if(b<=0)throw new Error('Rg must be greater than zero.');result=1+a/b;detail='Av = 1 + Rf/Rg; both resistance values must use the same unit.'}
      else if(kind==='adc'){if(b<1||b>32||!Number.isInteger(b)||a<=0)throw new Error('Value A must be positive Vref; value B must be an integer from 1 to 32.');result=a/(2**b);detail=`Ideal quantisation step under the Vref/2^N convention.`}
      else if(kind==='rc'){if(a<=0||b<=0)throw new Error('Use positive R in ohms and C in farads.');result=a*b;detail='τ = RC; output unit is seconds when inputs use SI units.'}
      else {if(b<1||b>52||!Number.isInteger(b))throw new Error('N must be an integer from 1 to 52.');result=2**b-1;detail=`Unsigned ${b}-bit range: 0 to ${result}.`}
      $('formula-result').textContent=Number.isFinite(result)?Number(result.toPrecision(10)).toLocaleString(undefined,{maximumSignificantDigits:10}):'Out of range';$('formula-detail').textContent=detail;
    }catch(error){showError('formula-result','Check inputs');showError('formula-detail',error.message)}
  }
  $('formula-calculate').addEventListener('click',formulaCalculate); $('formula-choice').addEventListener('change',()=>{const kind=$('formula-choice').value; $('formula-label-a').firstChild.textContent=kind==='adc'?'Vref (V)':kind==='rc'?'R (Ω)':kind==='binary'?'Unused A':'Rf'; $('formula-label-b').firstChild.textContent=kind==='adc'||kind==='binary'?'Bit count N':kind==='rc'?'C (F)':kind==='inv'?'Rin':'Rg';});
  document.querySelectorAll('.workbench-tab').forEach(tab=>tab.addEventListener('click',()=>{document.querySelectorAll('.workbench-tab').forEach(t=>{const active=t===tab;t.classList.toggle('active',active);t.setAttribute('aria-selected',String(active));});document.querySelectorAll('.workbench-panel').forEach(panel=>{const active=panel.id===tab.dataset.panel;panel.classList.toggle('active',active);panel.hidden=!active;});}));
  renderTruthTable(); runSequence();
})();
