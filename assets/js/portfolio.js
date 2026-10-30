// These controls work independently of third-party scripts.
(() => {
  const toggle = document.querySelector("[data-menu-toggle]");
  const menu = document.getElementById("navbarNav");
  if (toggle && menu) {
    document.documentElement.classList.add("menu-enhanced");
    toggle.hidden = false;
    const close = () => {
      toggle.setAttribute("aria-expanded", "false");
      menu.classList.remove("is-open");
    };
    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") !== "true";
      toggle.setAttribute("aria-expanded", String(open));
      menu.classList.toggle("is-open", open);
    });
    menu.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        close();
        toggle.focus();
      }
    });
    menu.querySelectorAll("a").forEach((link) => link.addEventListener("click", close));
  }
  document.querySelectorAll("[data-video]").forEach((root) => {
    const button = root.querySelector("[data-video-load]");
    button.hidden = false;
    button.addEventListener(
      "click",
      () => {
        const frame = document.createElement("iframe");
        frame.src = `https://www.youtube-nocookie.com/embed/${encodeURIComponent(root.dataset.video)}?autoplay=1`;
        frame.title = root.dataset.videoTitle;
        frame.allow = "autoplay; encrypted-media; picture-in-picture";
        frame.allowFullscreen = true;
        root.querySelector(".video-poster").replaceChildren(frame);
        frame.focus();
      },
      { once: true }
    );
  });
})();
