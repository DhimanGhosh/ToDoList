function startTimer(todo) {
    console.log(`Starting timer for: ${todo.title}`);  // Debugging output

    let hoursInput = document.getElementById(`hours-${todo.id}`);
    let minutesInput = document.getElementById(`minutes-${todo.id}`);
    let secondsInput = document.getElementById(`seconds-${todo.id}`);

    if (!hoursInput || !minutesInput || !secondsInput) {
        console.error("Input fields not found for todo:", todo.id);
        return;
    }

    let hours = parseInt(hoursInput.value) || 0;
    let minutes = parseInt(minutesInput.value) || 0;
    let seconds = parseInt(secondsInput.value) || 0;

    let totalTime = (hours * 60 * 60 + minutes * 60 + seconds) * 1000;

    if (totalTime <= 0) {
        alert("Please enter a valid time.");
        return;
    }

    let countdown = document.getElementById(`countdown-${todo.id}`);
    let endTime = new Date().getTime() + totalTime;

    let timer = setInterval(function () {
        let now = new Date().getTime();
        let distance = endTime - now;

        if (distance <= 0) {
            clearInterval(timer);
            countdown.innerHTML = "⏰ Time's up!";
            // Send an AJAX request to mark the task as completed
            fetch(`/update_task_status/${todo.id}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie('csrftoken')
                },
                body: JSON.stringify({ completed: true })
            })
            .then(response => {
                if (response.ok) {
                    console.log("Task marked as completed.");
                    // Update the UI to reflect that the task is completed
                    updateTaskUI(todo.id);
                } else {
                    console.error("Failed to update task.");
                }
            })
            .catch(err => console.error("Failed to update task."));
        } else {
            let hrs = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            let mins = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            let secs = Math.floor((distance % (1000 * 60)) / 1000);
            countdown.innerHTML = `${hrs}h ${mins}m ${secs}s remaining`;
        }
    }, 1000);
}

// Helper function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateTaskUI(todoId) {
    let todoElement = document.getElementById(`todo-${todoId}`);

    // Change the alert class to 'success' and apply a smooth background color transition
    todoElement.classList.remove('alert-warning');
    todoElement.classList.add('alert-success');
    todoElement.style.transition = "background-color 1s ease";

    // Update the checkbox and apply the pop-out effect
    let checkbox = document.getElementById(`checkbox-${todoId}`);
    if (checkbox) {
        checkbox.checked = true;

        // Pop-out effect
        checkbox.style.transition = "transform 0.5s ease";  // Longer transition for visibility
        checkbox.style.transform = "scale(2)";  // Increase size for pop-out effect

        setTimeout(() => {
            checkbox.style.transform = "scale(1)";  // Return to normal size
        }, 500);  // Wait 500ms to shrink back
    }

    console.log(`UI updated for task ${todoId}`);
}
