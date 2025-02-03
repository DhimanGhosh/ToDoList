document.addEventListener("DOMContentLoaded", function () {
    let changeColorBtn = document.getElementById("change-todo-colors");
    let pendingColorPicker = document.getElementById("pendingColor");
    let completedColorPicker = document.getElementById("completedColor");

    // Load saved colors
    let savedPendingColor = localStorage.getItem("pendingColor") || "#ffc107"; // Default: Yellow
    let savedCompletedColor = localStorage.getItem("completedColor") || "#198754"; // Default: Green

    pendingColorPicker.value = savedPendingColor;
    completedColorPicker.value = savedCompletedColor;

    document.documentElement.style.setProperty("--pending-task-color", savedPendingColor);
    document.documentElement.style.setProperty("--completed-task-color", savedCompletedColor);

    // Open modal
    changeColorBtn.addEventListener("click", function () {
        new bootstrap.Modal(document.getElementById("todoColorModal")).show();
    });

    // Save colors
    document.getElementById("save-colors").addEventListener("click", function () {
        let pendingColor = pendingColorPicker.value;
        let completedColor = completedColorPicker.value;

        localStorage.setItem("pendingColor", pendingColor);
        localStorage.setItem("completedColor", completedColor);

        document.documentElement.style.setProperty("--pending-task-color", pendingColor);
        document.documentElement.style.setProperty("--completed-task-color", completedColor);

        bootstrap.Modal.getInstance(document.getElementById("todoColorModal")).hide();
    });
});