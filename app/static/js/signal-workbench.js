(() => {
  "use strict";
  const $ = (id) => document.getElementById(id);
  const configs = {
    opamp: {
      title: "Op-amp transfer curve", subtitle: "Input voltage versus clipped output voltage",
      fields: [
        ["gain", "Closed-loop gain magnitude", 5, 0.1, 1000, 0.1],
        ["supply", "Symmetric output rail (V)", 5, 0.1, 100, 0.1],
        ["vinMax", "Input sweep magnitude (V)", 1, 0.01, 100, 0.01]
      ],
      sweep: ["gain", "supply"], xLabel: "Input voltage (V)", yLabel: "Output voltage (V)", timingXLabel: "Time (ms)", timingYLabel: "Voltage (V)",
      assumptions: "Idealized inverting transfer: Vout = −gain × Vin, clipped to symmetric ideal rails. Real op-amps have finite bandwidth, slew rate, input limits and output-swing constraints."
    },
    timer555: {
      title: "555 astable output", subtitle: "Square-wave output with approximate classic 555 timing",
      fields: [
        ["ra", "RA (Ω)", 10000, 1, 100000000, 1],
        ["rb", "RB (Ω)", 10000, 1, 100000000, 1],
        ["capUf", "Capacitance (µF)", 10, 0.001, 100000, 0.001],
        ["cycles", "Displayed cycles", 3, 1, 10, 1]
      ],
      sweep: ["ra", "rb", "capUf"], xLabel: "Time (ms)", yLabel: "Normalized output", timingXLabel: "Time (ms)", timingYLabel: "Capacitor voltage (V)",
      assumptions: "Uses TH ≈ 0.693(RA + RB)C and TL ≈ 0.693 RBC. The displayed waveform is an idealized square wave; discharge path details and component tolerances affect hardware behavior."
    },
    adc: {
      title: "ADC staircase transfer", subtitle: "Ideal unipolar input voltage versus quantized output level",
      fields: [
        ["bits", "Resolution (bits)", 4, 1, 10, 1],
        ["reference", "Reference voltage (V)", 5, 0.1, 100, 0.1]
      ],
      sweep: ["bits", "reference"], xLabel: "Input voltage (V)", yLabel: "Quantized voltage (V)", timingXLabel: "Time (ms)", timingYLabel: "Quantized voltage (V)",
      assumptions: "Ideal unipolar N-bit floor-code teaching model with 2^N codes and LSB = Vref/2^N. Practical ADC architectures may use different transfer conventions and have offset, gain, INL/DNL and noise."
    },
    pll: {
      title: "Simplified PLL lock response", subtitle: "Illustrative phase-error settling after a frequency mismatch",
      fields: [
        ["initialPhase", "Initial phase error (degrees)", 120, -180, 180, 1],
        ["tau", "Settling time constant (ms)", 20, 0.1, 1000, 0.1],
        ["duration", "Displayed duration (ms)", 100, 1, 5000, 1]
      ],
      sweep: ["tau", "initialPhase"], xLabel: "Time (ms)", yLabel: "Phase error (degrees)", timingXLabel: "Time (ms)", timingYLabel: "Phase error (degrees)",
      assumptions: "Illustrative first-order exponential phase-error decay, not a circuit-level PLL model. Real capture range, loop bandwidth, damping, VCO behavior and lock dynamics depend on the PLL architecture."
    },
    digital: {
      title: "Clocked D flip-flop timing", subtitle: "Input D sampled at rising clock edges to produce Q",
      fields: [
        ["data", "D input bit sequence (e.g. 101101)", "101101", "bits", 16],
        ["initialQ", "Initial Q state", 0, 0, 1, 1]
      ],
      sweep: ["initialQ"], xLabel: "Clock step", yLabel: "Logic state", timingXLabel: "Clock step", timingYLabel: "Logic state",
      assumptions: "Ideal positive-edge-triggered D flip-flop: Q updates to D at each rising edge and holds between edges. Setup/hold violations, propagation delay and metastability are not modeled."
    }
  };
  const colors = ["#167a72", "#2779b9", "#d47a37", "#8758b6", "#b54c65", "#65768b", "#4b8b45"];
  let currentRows = [];
  let currentCurves = [];
  let currentMode = "opamp";

  const num = (value, name, min, max) => {
    const parsed = Number(value);
    if (!Number.isFinite(parsed) || parsed < min || parsed > max) throw new Error(`${name} must be between ${min} and ${max}.`);
    return parsed;
  };
  const fmt = (value, digits = 4) => Number.isFinite(value) ? Number(value).toPrecision(digits) : "—";
  const escapeHtml = (value) => String(value).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  function renderFields() {
    const config = configs[currentMode];
    $("p3-chart-title").textContent = config.title;
    $("p3-chart-subtitle").textContent = config.subtitle;
    $("p3-assumptions").textContent = config.assumptions;
    $("p3-fields").innerHTML = config.fields.map(([key, label, value, min, max, step]) => {
      if (min === "bits") return `<label class="phase3-field"><span>${escapeHtml(label)}</span><input name="${key}" value="${escapeHtml(value)}" maxlength="16" autocomplete="off" spellcheck="false" inputmode="numeric" aria-label="${escapeHtml(label)}"></label>`;
      if (key === "bits" || (key === "initialQ" && currentMode === "digital")) {
        const options = key === "bits" ? Array.from({length:10},(_,i)=>i+1) : [0,1];
        return `<label class="phase3-field"><span>${escapeHtml(label)}</span><select name="${key}">${options.map(v=>`<option value="${v}" ${Number(value)===v?"selected":""}>${v}${key==="bits"?" bit"+(v>1?"s":""):""}</option>`).join("")}</select></label>`;
      }
      return `<label class="phase3-field"><span>${escapeHtml(label)}</span><input type="number" name="${key}" value="${value}" min="${min}" max="${max}" step="${step || "any"}" required></label>`;
    }).join("");
    $("p3-sweep").innerHTML = config.sweep.map(key => {
      const field = config.fields.find(item => item[0] === key);
      return `<option value="${key}">${escapeHtml(field ? field[1] : key)}</option>`;
    }).join("");
    const first = config.fields.find(item => item[0] === config.sweep[0]);
    $("p3-sweep-start").value = first && typeof first[2] === "number" ? first[2] * 0.5 : 1;
    $("p3-sweep-end").value = first && typeof first[2] === "number" ? first[2] * 1.5 : 5;
    if (currentMode === "adc") {
      $("p3-sweep-start").value = "2";
      $("p3-sweep-end").value = "8";
    }
    if (currentMode === "digital") {
      $("p3-sweep-start").value = "0";
      $("p3-sweep-end").value = "1";
    }
  }
  function readParams() {
    const result = {};
    for (const field of configs[currentMode].fields) {
      const el = $("p3-fields").querySelector(`[name="${field[0]}"]`);
      if (!el) continue;
      if (field[3] === "bits") {
        const sequence = el.value.trim();
        if (!/^[01]{1,16}$/.test(sequence)) throw new Error("D input sequence must contain 1–16 binary digits (0 or 1).");
        result[field[0]] = sequence;
      } else if (field[0] === "bits" || field[0] === "initialQ") {
        result[field[0]] = num(el.value, field[1], field[3], field[4]);
      } else {
        result[field[0]] = num(el.value, field[1], field[3], field[4]);
      }
    }
    return result;
  }
  function model(mode, p, sweepValue, sweepKey) {
    const v = {...p};
    if (sweepKey) v[sweepKey] = sweepValue;
    const curve = [];
    let metrics = [];
    let timing = [];
    if (mode === "opamp") {
      const max = v.vinMax;
      for (let i=0;i<=200;i++) {
        const x = -max + (2*max*i/200);
        curve.push({x, y: Math.max(-v.supply, Math.min(v.supply, -v.gain*x))});
      }
      metrics = [["Gain magnitude", fmt(v.gain)], ["Positive rail", `${fmt(v.supply)} V`], ["Linear input limit", `±${fmt(v.supply/v.gain)} V`]];
      for (let i=0;i<=400;i++) {
        const tMs = 40*i/400;
        const input = max * Math.sin(2*Math.PI*2*tMs/40);
        timing.push({x:tMs,y:Math.max(-v.supply,Math.min(v.supply,-v.gain*input))});
      }
    } else if (mode === "timer555") {
      const cap = v.capUf * 1e-6;
      const high = .693 * (v.ra + v.rb) * cap;
      const low = .693 * v.rb * cap;
      const period = high + low;
      const cycles = v.cycles || 3;
      const duration = period * cycles;
      for (let i=0;i<=600;i++) {
        const x = duration * i / 600;
        const phase = x % period;
        curve.push({x: x*1000, y: phase < high ? 1 : 0});
      }
      metrics = [["High time", `${fmt(high*1000)} ms`], ["Low time", `${fmt(low*1000)} ms`], ["Frequency", `${fmt(1/period)} Hz`], ["Duty cycle", `${fmt(high/period*100)} %`]];
      const supply = 5;
      for (let i=0;i<=600;i++) {
        const t = duration*i/600;
        const phase = t%period;
        const voltage = phase < high
          ? supply - (supply-supply/3)*Math.exp(-phase/((v.ra+v.rb)*cap))
          : (2*supply/3)*Math.exp(-(phase-high)/(v.rb*cap));
        timing.push({x:t*1000,y:voltage});
      }
    } else if (mode === "adc") {
      const levels = 2 ** v.bits;
      const lsb = v.reference / levels;
      for (let i=0;i<=512;i++) {
        const x = v.reference*i/512;
        const code = Math.min(levels-1, Math.floor(x/lsb));
        curve.push({x, y: code*lsb});
      }
      metrics = [["Code levels", String(levels)], ["LSB step", `${fmt(lsb)} V`], ["Quantization bound", `less than ${fmt(lsb)} V`]];
      for (let i=0;i<=400;i++) {
        const tMs = 40*i/400;
        const input = v.reference/2*(1+Math.sin(2*Math.PI*2*tMs/40));
        const code = Math.min(levels-1,Math.floor(input/lsb));
        timing.push({x:tMs,y:code*lsb});
      }
    } else if (mode === "pll") {
      const duration = v.duration;
      for (let i=0;i<=200;i++) {
        const x = duration*i/200;
        const y = v.initialPhase * Math.exp(-x/v.tau);
        curve.push({x, y});
      }
      metrics = [["Initial phase error", `${fmt(v.initialPhase)}°`], ["Time constant", `${fmt(v.tau)} ms`], ["Error at duration", `${fmt(v.initialPhase*Math.exp(-duration/v.tau))}°`]];
      timing = curve;
    } else if (mode === "digital") {
      const bits = v.data;
      let q = Number(v.initialQ);
      curve.push({x:0,y:q});
      for (let i=0;i<bits.length;i++) {
        q = Number(bits[i]);
        curve.push({x:i+1-.001,y:Number(curve[curve.length-1].y)});
        curve.push({x:i+1,y:q});
        curve.push({x:i+1.5,y:q});
      }
      metrics = [["Clock edges", String(bits.length)], ["Input sequence", bits], ["Final Q", String(q)]];
      timing = curve;
    }
    return {curve, metrics, timing, params:v};
  }
  function axisRange(curves, axis) {
    const values = curves.flatMap(c=>c.curve.map(point=>point[axis])).filter(Number.isFinite);
    if (!values.length) return {min:0,max:1};
    let min = Math.min(...values), max = Math.max(...values);
    if (min === max) {min -= 1;max += 1;}
    const pad = (max-min)*.08;
    return {min:min-pad,max:max+pad};
  }
  function drawChart(canvas, curves, xLabel, yLabel, options={}) {
    const ctx = canvas.getContext("2d");
    const ratio = window.devicePixelRatio || 1;
    const width = Math.max(320, canvas.clientWidth || 800);
    const height = options.height || Number(canvas.getAttribute("height")) || 360;
    canvas.width = Math.round(width*ratio);
    canvas.height = Math.round(height*ratio);
    canvas.style.height = `${height}px`;
    ctx.scale(ratio,ratio);
    ctx.clearRect(0,0,width,height);
    ctx.fillStyle = "#ffffff"; ctx.fillRect(0,0,width,height);
    const margin = {left:65,right:22,top:20,bottom:55};
    const plotW = width-margin.left-margin.right, plotH=height-margin.top-margin.bottom;
    const xr = axisRange(curves,"x"), yr=axisRange(curves,"y");
    if (options.fixedX) {xr.min=options.fixedX[0];xr.max=options.fixedX[1];}
    if (options.fixedY) {yr.min=options.fixedY[0];yr.max=options.fixedY[1];}
    const px=x=>margin.left+(x-xr.min)/(xr.max-xr.min)*plotW;
    const py=y=>margin.top+(yr.max-y)/(yr.max-yr.min)*plotH;
    ctx.strokeStyle="#e7edf2";ctx.lineWidth=1;ctx.fillStyle="#5f6d7b";ctx.font="11px system-ui";
    for(let i=0;i<=5;i++){
      const y=margin.top+plotH*i/5;
      ctx.beginPath();ctx.moveTo(margin.left,y);ctx.lineTo(margin.left+plotW,y);ctx.stroke();
      const val=yr.max-(yr.max-yr.min)*i/5;
      ctx.fillText(fmt(val,3),7,y+4);
    }
    for(let i=0;i<=6;i++){
      const x=margin.left+plotW*i/6;
      ctx.beginPath();ctx.moveTo(x,margin.top);ctx.lineTo(x,margin.top+plotH);ctx.stroke();
      const val=xr.min+(xr.max-xr.min)*i/6;
      ctx.fillText(fmt(val,3),x-17,margin.top+plotH+18);
    }
    ctx.strokeStyle="#6f8191";ctx.beginPath();ctx.moveTo(margin.left,margin.top);ctx.lineTo(margin.left,margin.top+plotH);ctx.lineTo(margin.left+plotW,margin.top+plotH);ctx.stroke();
    curves.forEach((curve,index)=>{
      ctx.strokeStyle=colors[index%colors.length];ctx.lineWidth=index===0?2.7:1.8;ctx.beginPath();
      curve.curve.forEach((point,i)=>{
        const x=px(point.x),y=py(point.y);
        if(i===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
      });
      ctx.stroke();
    });
    ctx.fillStyle="#223447";ctx.font="12px system-ui";ctx.textAlign="center";ctx.fillText(xLabel,margin.left+plotW/2,height-9);
    ctx.save();ctx.translate(16,margin.top+plotH/2);ctx.rotate(-Math.PI/2);ctx.fillText(yLabel,0,0);ctx.restore();ctx.textAlign="start";
  }
  function showMetrics(result) {
    $("p3-metrics").innerHTML = result.metrics.map(([label,value])=>`<div class="phase3-metric"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong></div>`).join("");
  }
  function showLegend(curves, sweepKey) {
    $("p3-legend").innerHTML = curves.map((c,i)=>`<span><i style="background:${colors[i%colors.length]}"></i>${escapeHtml(c.label || (i===0?"Baseline":`${sweepKey} ${fmt(c.sweepValue,3)}`))}</span>`).join("");
  }
  function runSingle() {
    try {
      const params=readParams();
      const result=model(currentMode,params);
      currentCurves=[{...result,label:"Current settings"}];
      showMetrics(result);
      showLegend(currentCurves);
      const config=configs[currentMode];
      drawChart($("p3-chart"),currentCurves,config.xLabel,config.yLabel);
      drawChart($("p3-timing"),[{curve:result.timing,label:"Companion response"}],config.timingXLabel,config.timingYLabel,{height:220});
      $("p3-timing-subtitle").textContent = currentMode==="digital" ? "D is sampled at each rising edge; Q holds between edges." : config.subtitle;
      $("p3-status").textContent="UPDATED";
      $("p3-status").classList.remove("warn");
      $("p3-table-head").innerHTML="<tr><th>Parameter</th><th>Value</th><th>Calculated result</th></tr>";
      $("p3-table-body").innerHTML=result.metrics.map(([k,v])=>`<tr><td>${escapeHtml(k)}</td><td>—</td><td>${escapeHtml(v)}</td></tr>`).join("");
      currentRows=result.metrics.map(([Parameter,Result])=>({Parameter,Result}));
    } catch(error) {
      $("p3-status").textContent="CHECK INPUTS";$("p3-status").classList.add("warn");
      $("p3-metrics").innerHTML=`<div class="phase3-error">${escapeHtml(error.message)}</div>`;
    }
  }
  function compare() {
    try {
      const params=readParams();
      const key=$("p3-sweep").value;
      let start=num($("p3-sweep-start").value,"Sweep start",-1e9,1e9);
      let end=num($("p3-sweep-end").value,"Sweep end",-1e9,1e9);
      const count=num($("p3-sweep-count").value,"Curve count",3,7);
      if(start>end)[start,end]=[end,start];
      if(key==="bits" || key==="initialQ") {start=Math.round(start);end=Math.round(end);}
      if(key==="bits" && (start<1 || end>10)) throw new Error("ADC resolution sweep must stay between 1 and 10 bits.");
      if(key==="initialQ" && (start<0 || end>1)) throw new Error("Initial Q sweep must stay between 0 and 1.");
      if(["ra","rb","capUf","reference","gain","supply","tau","duration"].includes(key) && start<=0) throw new Error("This parameter's sweep range must be positive.");
      let values=Array.from({length:count},(_,i)=>start+(end-start)*i/(count-1));
      if (key === "bits") values = [...new Set(values.map(value => Math.round(value)))];
      if (key === "initialQ") values = [...new Set([Math.round(start), Math.round(end)])];
      currentCurves=values.map((value,i)=>{
        const result=model(currentMode,params,value,key);
        return {...result,sweepValue:value,label:`${key} = ${fmt(value,3)}`};
      });
      const baseline=model(currentMode,params);
      showMetrics(baseline);showLegend(currentCurves,key);
      const config=configs[currentMode];
      drawChart($("p3-chart"),currentCurves,config.xLabel,config.yLabel);
      drawChart($("p3-timing"),[{curve:currentCurves[Math.floor(currentCurves.length/2)].timing,label:"Middle sweep response"}],config.timingXLabel,config.timingYLabel,{height:220});
      $("p3-status").textContent=`${count} CURVES`;$("p3-status").classList.remove("warn");
      $("p3-timing-subtitle").textContent=`Time-domain response using middle sweep value (${key} = ${fmt(values[Math.floor(values.length/2)],3)}).`;
      $("p3-table-head").innerHTML=`<tr><th>${escapeHtml(key)}</th><th>Primary metric</th><th>Secondary metric</th></tr>`;
      currentRows=values.map(value=>{
        const result=model(currentMode,params,value,key);
        const primary=result.metrics[0]||["Result","—"];
        const secondary=result.metrics[1]||["","—"];
        return {[key]:value,[primary[0]]:primary[1],[secondary[0]||"Secondary"]:secondary[1]};
      });
      $("p3-table-body").innerHTML=currentRows.map(row=>`<tr>${Object.values(row).map(v=>`<td>${escapeHtml(v)}</td>`).join("")}</tr>`).join("");
    } catch(error) {
      $("p3-status").textContent="CHECK INPUTS";$("p3-status").classList.add("warn");
      $("p3-metrics").innerHTML=`<div class="phase3-error">${escapeHtml(error.message)}</div>`;
    }
  }
  function exportCsv() {
    if(!currentRows.length) { $("p3-status").textContent="NOTHING TO EXPORT"; return; }
    const headers=[...new Set(currentRows.flatMap(row=>Object.keys(row)))];
    const csv=[headers,...currentRows.map(row=>headers.map(header=>row[header]??""))]
      .map(row=>row.map(value=>`"${String(value).replace(/"/g,'""')}"`).join(",")).join("\r\n");
    const blob=new Blob([csv],{type:"text/csv;charset=utf-8"});
    const url=URL.createObjectURL(blob);
    const link=document.createElement("a");link.href=url;link.download=`ldica-${currentMode}-comparison.csv`;link.click();
    URL.revokeObjectURL(url);
  }
  $("p3-mode").addEventListener("change",()=>{currentMode=$("p3-mode").value;renderFields();runSingle();});
  $("p3-run").addEventListener("click",runSingle);
  $("p3-compare").addEventListener("click",compare);
  $("p3-reset").addEventListener("click",()=>{renderFields();runSingle();});
  $("p3-export").addEventListener("click",exportCsv);
  window.addEventListener("resize",()=>{if(currentCurves.length){const config=configs[currentMode];drawChart($("p3-chart"),currentCurves,config.xLabel,config.yLabel);}});
  renderFields();runSingle();
})();