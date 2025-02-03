document.addEventListener("DOMContentLoaded", function () {
    let usernameInput = document.getElementById("username-input");
    let confirmBtn = document.getElementById("confirm-btn");
    let errorMessage = document.getElementById("error-message");
    let hiddenUsername = document.getElementById("hidden-username");

    // Get username from HTML instead of template directly in JavaScript
    let actualUsername = document.getElementById("actual-username").innerText.trim();

    usernameInput.addEventListener("input", function () {
        let enteredUsername = usernameInput.value.trim();

        if (enteredUsername === actualUsername) {
            confirmBtn.disabled = false;
            errorMessage.classList.add("d-none");
            hiddenUsername.value = actualUsername; // Store the username in hidden input
        } else {
            confirmBtn.disabled = true;
            errorMessage.classList.remove("d-none");
        }
    });
});
