document.addEventListener("DOMContentLoaded", function () {
    let themeToggle = document.getElementById("toggle-theme");
    let currentTheme = localStorage.getItem("theme") || "light";

    if (currentTheme === "dark") {
        document.body.classList.add("dark-theme");
    }

    themeToggle.addEventListener("click", function (event) {
        event.preventDefault(); // Prevents the default `#` behavior
        document.body.classList.toggle("dark-theme");
        localStorage.setItem("theme", document.body.classList.contains("dark-theme") ? "dark" : "light");
    });
});