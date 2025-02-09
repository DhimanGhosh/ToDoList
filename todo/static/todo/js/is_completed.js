document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".todo-checkbox").forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {
            let todoId = this.dataset.todoId;
            let isChecked = this.checked;

            let csrfMetaTag = document.querySelector('meta[name="csrf-token"]');
            if (!csrfMetaTag) {
                console.error("CSRF token meta tag not found!");
                return;
            }
            let csrftoken = csrfMetaTag.getAttribute("content");

            let alertDiv = document.getElementById(`todo-${todoId}`);

            // Remove any temporary pop effect from previous interactions
            let checkbox = document.querySelector(`#checkbox-${todoId}`);
            if (checkbox) {
                checkbox.classList.add('todo-checkbox-checked');

                setTimeout(() => {
                    checkbox.classList.remove('todo-checkbox-checked');  // Remove pop effect after 300ms
                }, 300);
            }

            // Apply the appropriate background color class with a smooth transition
            alertDiv.classList.remove("alert-success", "alert-warning");
            alertDiv.classList.add(isChecked ? "alert-success" : "alert-warning");

            // Send the status update to the server
            fetch(`/toggle_completed/${todoId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ completed: isChecked })
            })
            .then(response => response.json())
            .then(data => console.log("Task status updated:", data))
            .catch(error => console.error("Error:", error));
        });
    });
});
