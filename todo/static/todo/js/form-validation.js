document.addEventListener("DOMContentLoaded", function () {
    let form = document.getElementById("todo-form");
    let hasSubmitted = false; // Track if the form has been submitted

    form.querySelectorAll("input, textarea").forEach(function (field) {
        let isRequired = field.hasAttribute("required");
        let errorDiv = field.parentElement.querySelector(".invalid-feedback");

        // Hide error messages initially
        if (errorDiv) errorDiv.style.display = "none";

        field.addEventListener("blur", function () {
            if (!hasSubmitted) return; // Don't show errors before form submission

            if (!isRequired && !field.value.trim()) {
                field.classList.remove("is-invalid"); // No red border for optional fields
                if (errorDiv) errorDiv.style.display = "none";
                return;
            }

            if (errorDiv) {
                if (field.value.trim() === "" && isRequired) {
                    field.classList.add("is-invalid");
                    errorDiv.style.display = "block";
                } else {
                    field.classList.remove("is-invalid");
                    errorDiv.style.display = "none";
                }
            }
        });
    });

    // Show Django errors only after form submission
    form.addEventListener("submit", function (event) {
        hasSubmitted = true; // Mark form as submitted
        let hasErrors = false;

        form.querySelectorAll("input[required], textarea[required]").forEach(function (field) {
            let errorDiv = field.parentElement.querySelector(".invalid-feedback");

            if (errorDiv) {
                if (!field.value.trim()) {
                    field.classList.add("is-invalid");
                    errorDiv.style.display = "block";
                    hasErrors = true;
                }
            }
        });

        if (hasErrors) {
            event.preventDefault(); // Prevent form submission if errors exist
        }
    });
});
