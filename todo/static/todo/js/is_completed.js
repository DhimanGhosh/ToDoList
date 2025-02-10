document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".todo-checkbox").forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {
            let todoId = this.dataset.todoId;
            let isChecked = this.checked;
            let alertDiv = document.getElementById(`todo-${todoId}`);
            let timerButton = document.getElementById(`timer-button-${todoId}`);
            let csrfToken = document.querySelector('meta[name="csrf-token"]').content;

            console.log("Updating Todo ID:", todoId, "Completed:", isChecked);

            fetch(`/toggle_completed/${todoId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ completed: isChecked })
            })
                .then(response => response.json())
                .then(data => {
                    console.log("Response:", data);

                    // Update the color without refreshing the page
                    alertDiv.classList.remove("alert-success", "alert-warning");
                    if (data.completed) {
                        alertDiv.classList.add("alert-success");
                        timerButton.disabled = true;  // Disable timer on completion
                    } else {
                        alertDiv.classList.add("alert-warning");
                        timerButton.disabled = false;  // Enable timer for incomplete tasks
                    }
                })
                .catch(error => console.error("Error:", error));
        });
    });
});
