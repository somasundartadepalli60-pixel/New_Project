(() => {
  const clock = document.getElementById('exam-clock');
  if (!clock) return;
  let remaining = Math.max(0, Number.parseInt(clock.dataset.seconds || '0', 10));
  const form = document.getElementById('mock-exam-form');
  const paint = () => {
    const mins = Math.floor(remaining / 60);
    const secs = remaining % 60;
    clock.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    clock.classList.toggle('time-low', remaining <= 60);
  };
  paint();
  const tick = window.setInterval(() => {
    remaining = Math.max(0, remaining - 1);
    paint();
    if (remaining === 0) {
      window.clearInterval(tick);
      clock.textContent = 'Time elapsed — submit your answers';
      clock.setAttribute('role', 'alert');
    }
  }, 1000);
  form?.addEventListener('submit', () => window.clearInterval(tick));
})();
