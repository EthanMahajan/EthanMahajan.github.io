(() => {
  const button = document.createElement("button");
  button.id = "back-to-top";
  button.type = "button";
  button.hidden = true;
  button.setAttribute("aria-label", "Back to top");
  button.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m7 14 5-5 5 5-1.4 1.4L12 11.8l-3.6 3.6Z"/></svg>';
  document.body.append(button);

  button.addEventListener("click", () => {
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    window.scrollTo({ top: 0, behavior: reducedMotion ? "instant" : "smooth" });
    document.getElementById("main-content")?.focus({ preventScroll: true });
  });

  const update = () => {
    button.hidden = window.scrollY < 400;
  };
  window.addEventListener("scroll", update, { passive: true });
  update();
})();
