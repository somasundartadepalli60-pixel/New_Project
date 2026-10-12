(() => {
  const byId = (id) => document.getElementById(id);
  const number = (id, fallback = 0) => {
    const el = byId(id); const value = el ? Number(el.value) : fallback;
    return Number.isFinite(value) ? value : fallback;
  };
  const fmt = (value, digits = 5) => Number.isFinite(value) ? value.toPrecision(digits) : "—";

  function initGain() {
    const ids = ["vin", "rin", "rf", "rg"];
    if (!byId("gain-output")) return;
    const update = () => {
      const vin = number("vin"), rin = number("rin"), rf = number("rf"), rg = number("rg");
      if (rin <= 0 || rg <= 0 || rf < 0) {
        byId("gain-output").textContent = "Resistance values must be positive (Rf may be zero)."; return;
      }
      const invGain = -rf / rin, nonGain = 1 + rf / rg;
      byId("gain-output").textContent = `Inverting gain = ${fmt(invGain)}; estimated Vout = ${fmt(invGain * vin)} V\nNon-inverting gain = ${fmt(nonGain)}; estimated Vout = ${fmt(nonGain * vin)} V\nAssumes ideal op-amp, linear operation and correct feedback topology.`;
    };
    ids.forEach(id => byId(id).addEventListener("input", update)); update();
  }

  function initTimer() {
    if (!byId("timer-svg")) return;
    let paused = false, phase = 0, raf = null;
    const wave = byId("timer-wave");
    const render = () => {
      const ra = number("ra", 10), rb = number("rb", 10), cap = number("cap", 10);
      if (ra <= 0 || rb <= 0 || cap <= 0) {
        byId("timer-output").textContent = "RA, RB and C must be positive."; return;
      }
      const th = .693 * (ra + rb) * 1000 * cap * 1e-6;
      const tl = .693 * rb * 1000 * cap * 1e-6;
      const period = th + tl, hz = period > 0 ? 1 / period : 0;
      let d = "";
      for (let x = 0; x <= 610; x += 2) {
        const cycle = ((x / 610 + phase) % 1);
        const y = cycle < th / period ? 142 - 59 * cycle / (th / period) : 83 + 59 * (cycle - th / period) / (tl / period);
        d += `${x === 0 ? "M" : "L"}${45+x} ${y.toFixed(2)} `;
      }
      wave.setAttribute("d", d);
      byId("timer-output").textContent = `Approximate high time: ${fmt(th)} s | low time: ${fmt(tl)} s | frequency: ${fmt(hz)} Hz\nModel: classic 555 astable equations; real timing depends on tolerances and circuit details.`;
    };
    const tick = () => { if (!paused) { phase = (phase + .0025) % 1; render(); } raf = requestAnimationFrame(tick); };
    ["ra","rb","cap"].forEach(id => byId(id).addEventListener("input", render));
    byId("timer-play").addEventListener("click", () => { paused = !paused; byId("timer-play").textContent = paused ? "Play animation" : "Pause animation"; });
    render(); tick();
  }

  function initAdc() {
    if (!byId("adc-svg")) return;
    const update = () => {
      const input = number("adc-input"), bits = number("adc-bits", 4), ref = number("adc-ref", 5);
      byId("adc-input-label").textContent = `${input.toFixed(2)} V`;
      if (ref <= 0) { byId("adc-output").textContent = "Reference must be greater than zero."; return; }
      const levels = 2 ** bits, lsb = ref / levels;
      const code = Math.min(levels - 1, Math.max(0, Math.floor(Math.min(input, ref) / lsb)));
      const svg = byId("adc-svg");
      let paths = `<path d="M50 25 V210 H660" fill="none" stroke="#8293a3"/>`;
      for (let i = 0; i < levels; i++) {
        const x = 50 + i * 600 / levels, next = 50 + (i+1) * 600 / levels;
        const y = 205 - (i+1) * 175 / levels;
        paths += `<path d="M${x} ${y} H${next}" fill="none" stroke="${i===code?'#16816c':'#1c78b7'}" stroke-width="${i===code?4:2}"/>`;
        if (bits <= 5) paths += `<text x="${(x+next)/2}" y="230" font-size="10" text-anchor="middle" fill="#172536">${i.toString(2).padStart(bits,"0")}</text>`;
      }
      const markerX = 50 + Math.min(input, ref) / ref * 600;
      paths += `<path d="M${markerX} 25 V210" stroke="#c46d3a" stroke-dasharray="4 4" stroke-width="2"/>`;
      svg.innerHTML = paths;
      byId("adc-output").textContent = `LSB step ≈ ${fmt(lsb)} V | code = ${code} | binary = ${code.toString(2).padStart(bits,"0")} | ideal quantised level ≈ ${(code*lsb).toFixed(4)} V\nThis educational model uses floor quantisation and clips inputs at the reference voltage. Real ADCs have offset, gain, INL/DNL, noise and timing effects.`;
    };
    ["adc-input","adc-bits","adc-ref"].forEach(id => byId(id).addEventListener("input", update)); update();
  }

  function initCounter() {
    if (!byId("counter-bits")) return;
    let state = 0, timer = null;
    const render = () => {
      byId("counter-bits").innerHTML = [...state.toString(2).padStart(4,"0")].map((bit, i) => `<div style="padding:18px 22px;border-radius:12px;background:${bit==="1"?"#102b43":"#e3ebef"};color:${bit==="1"?"#b7f0e2":"#172536"};font:700 24px 'DM Mono',monospace">${bit}<small style="display:block;font-size:9px;text-align:center;opacity:.8">Q${3-i}</small></div>`).join("");
      byId("counter-output").textContent = `Decimal state: ${state} | Binary state: ${state.toString(2).padStart(4,"0")} | Next state: ${((state+1)%16).toString(2).padStart(4,"0")}`;
    };
    const step = () => { state = (state + 1) % 16; render(); };
    byId("counter-step").addEventListener("click", step);
    byId("counter-reset").addEventListener("click", () => { state = 0; render(); });
    byId("counter-run").addEventListener("click", () => {
      if (timer) { clearInterval(timer); timer = null; byId("counter-run").textContent = "Run"; }
      else { timer = setInterval(step, 700); byId("counter-run").textContent = "Pause"; }
    });
    render();
  }
  document.addEventListener("DOMContentLoaded", () => { initGain(); initTimer(); initAdc(); initCounter(); });
})();
