document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".todo-checkbox").forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {
            let todoId = this.dataset.todoId;
            let isChecked = this.checked;

            // Get CSRF token from meta tag
            let csrfMetaTag = document.querySelector('meta[name="csrf-token"]');
            if (!csrfMetaTag) {
                console.error("CSRF token meta tag not found!");
                return; // Stop execution if CSRF token is missing
            }
            let csrftoken = csrfMetaTag.getAttribute("content");

            console.log("Sending update for Todo ID:", todoId, "Completed:", isChecked);

            fetch(`/toggle_completed/${todoId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ completed: isChecked })
            })
            .then(response => response.json())
            .then(data => {
                console.log("Response:", data);
                if (data.status === "success") {
                    let alertDiv = document.getElementById(`todo-${todoId}`);
                    alertDiv.classList.remove("alert-success", "alert-warning");
                    alertDiv.classList.add(data.completed ? "alert-success" : "alert-warning");
                }
            })
            .catch(error => console.error("Error:", error));
        });
    });
});
