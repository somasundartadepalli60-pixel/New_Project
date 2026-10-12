document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const expanded = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!expanded));
      nav.classList.toggle("is-open", !expanded);
    });
  }

  document.querySelectorAll("[data-confirm]").forEach((element) => {
    element.addEventListener("click", (event) => {
      if (!window.confirm(element.dataset.confirm)) event.preventDefault();
    });
  });

  document.querySelectorAll("form").forEach((form) => {
    form.addEventListener("submit", () => {
      const button = form.querySelector('button[type="submit"], input[type="submit"]');
      if (button && !button.dataset.noLoading) {
        button.dataset.originalText = button.textContent;
        button.classList.add("is-submitting");
      }
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-tutor-prompt]").forEach((button) => {
    button.addEventListener("click", () => {
      const input = document.querySelector("#question");
      if (input) { input.value = button.dataset.tutorPrompt || ""; input.focus(); }
    });
  });
});
