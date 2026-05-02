/**
 * TaskFlow – app.js
 * Handles task CRUD, filtering, theme toggle, and count updates.
 */

const STORAGE_KEY = "taskflow_tasks";

// ── State ──────────────────────────────────────────────────────────────────

let tasks = loadTasks();
let currentFilter = "all";

// ── DOM references ─────────────────────────────────────────────────────────

const form        = document.getElementById("add-task-form");
const taskInput   = document.getElementById("task-input");
const taskList    = document.getElementById("task-list");
const taskCount   = document.getElementById("task-count");
const emptyState  = document.getElementById("empty-state");
const themeToggle = document.getElementById("theme-toggle");
const themeIcon   = document.getElementById("theme-icon");
const themeLabel  = document.getElementById("theme-label");
const statusEl    = document.getElementById("status");
const filterBtns  = document.querySelectorAll(".filter-btn");

// ── Persistence ────────────────────────────────────────────────────────────

function loadTasks() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) ?? defaultTasks();
  } catch {
    return defaultTasks();
  }
}

function saveTasks() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

function defaultTasks() {
  return [
    { id: 1, title: "Improve layout hierarchy", completed: false },
    { id: 2, title: "Add keyboard shortcuts",   completed: false },
    { id: 3, title: "Improve color contrast",   completed: true  },
  ];
}

// ── Rendering ──────────────────────────────────────────────────────────────

function getVisibleTasks() {
  if (currentFilter === "active")    return tasks.filter(t => !t.completed);
  if (currentFilter === "completed") return tasks.filter(t =>  t.completed);
  return tasks;
}

function renderTasks() {
  const visible = getVisibleTasks();
  taskList.innerHTML = "";

  visible.forEach(task => {
    const li = createTaskElement(task);
    taskList.appendChild(li);
  });

  emptyState.hidden = visible.length > 0;
  updateCount();
}

function createTaskElement(task) {
  const li = document.createElement("li");
  li.className = `task-item${task.completed ? " completed" : ""}`;
  li.dataset.id = task.id;

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.className = "task-checkbox";
  checkbox.checked = task.completed;
  checkbox.id = `task-${task.id}`;
  checkbox.setAttribute("aria-label", `Mark "${task.title}" as ${task.completed ? "incomplete" : "complete"}`);

  const label = document.createElement("label");
  label.htmlFor = `task-${task.id}`;
  label.className = "task-title";
  label.textContent = task.title;

  const deleteBtn = document.createElement("button");
  deleteBtn.className = "btn btn-danger";
  deleteBtn.setAttribute("aria-label", `Delete task: ${task.title}`);
  deleteBtn.textContent = "×";

  checkbox.addEventListener("change", () => toggleTask(task.id));
  deleteBtn.addEventListener("click", () => deleteTask(task.id, task.title));

  li.append(checkbox, label, deleteBtn);
  return li;
}

function updateCount() {
  const active = tasks.filter(t => !t.completed).length;
  taskCount.textContent = `${active} remaining`;
}

// ── Task operations ────────────────────────────────────────────────────────

function addTask(title) {
  const trimmed = title.trim();
  if (!trimmed) return;
  const id = Date.now();
  tasks.push({ id, title: trimmed, completed: false });
  saveTasks();
  renderTasks();
  announce(`Task "${trimmed}" added`);
}

function toggleTask(id) {
  const task = tasks.find(t => t.id === id);
  if (!task) return;
  task.completed = !task.completed;
  saveTasks();
  renderTasks();
}

function deleteTask(id, title) {
  tasks = tasks.filter(t => t.id !== id);
  saveTasks();
  renderTasks();
  announce(`Task "${title}" deleted`);
}

// ── Filters ────────────────────────────────────────────────────────────────

function setFilter(filter) {
  currentFilter = filter;
  filterBtns.forEach(btn => {
    const isActive = btn.dataset.filter === filter;
    btn.classList.toggle("active", isActive);
    btn.setAttribute("aria-pressed", String(isActive));
  });
  renderTasks();
}

// ── Theme ──────────────────────────────────────────────────────────────────

function applyTheme(dark) {
  document.body.dataset.theme = dark ? "dark" : "";
  themeIcon.textContent  = dark ? "☀️" : "🌙";
  themeLabel.textContent = dark ? "Light mode" : "Dark mode";
  themeToggle.setAttribute("aria-pressed", String(dark));
  localStorage.setItem("theme_dark", dark);
}

// ── Accessibility helper ───────────────────────────────────────────────────

function announce(message) {
  statusEl.textContent = "";
  // Force reflow so screen readers re-read the region
  requestAnimationFrame(() => { statusEl.textContent = message; });
}

// ── Event listeners ────────────────────────────────────────────────────────

form.addEventListener("submit", e => {
  e.preventDefault();
  addTask(taskInput.value);
  taskInput.value = "";
  taskInput.focus();
});

filterBtns.forEach(btn => {
  btn.addEventListener("click", () => setFilter(btn.dataset.filter));
});

themeToggle.addEventListener("click", () => {
  const isDark = document.body.dataset.theme === "dark";
  applyTheme(!isDark);
});

// ── Init ───────────────────────────────────────────────────────────────────

(function init() {
  const savedDark = localStorage.getItem("theme_dark") === "true";
  applyTheme(savedDark);
  renderTasks();
})();
