const toggle = document.getElementById("theme-toggle");
const status = document.getElementById("status");

toggle?.addEventListener("click", () => {
  const dark = document.body.dataset.theme === "dark";
  if (dark) {
    document.body.dataset.theme = "";
    status.textContent = "Light theme active";
    return;
  }

  document.body.dataset.theme = "dark";
  status.textContent = "Dark theme active";
});
