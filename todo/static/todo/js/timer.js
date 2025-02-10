function startTimer(todo) {
    let hours = parseInt(document.getElementById(`hours-${todo.id}`).value) || 0;
    let minutes = parseInt(document.getElementById(`minutes-${todo.id}`).value) || 0;
    let seconds = parseInt(document.getElementById(`seconds-${todo.id}`).value) || 0;
    let countdown = document.getElementById(`countdown-${todo.id}`);
    let checkbox = document.querySelector(`.todo-checkbox[data-todo-id="${todo.id}"]`);
    let timerButton = document.getElementById(`timer-button-${todo.id}`);

    let totalTime = (hours * 3600 + minutes * 60 + seconds) * 1000;

    if (totalTime <= 0) {
        alert("Please set a valid timer!");
        return;
    }

    let endTime = Date.now() + totalTime;

    let timer = setInterval(function () {
        let now = Date.now();
        let distance = endTime - now;

        if (distance <= 0) {
            clearInterval(timer);
            countdown.innerHTML = "⏰ Time's up!";
            checkbox.checked = true;  // Check the checkbox

            // Trigger the checkbox change event to update UI instantly
            checkbox.dispatchEvent(new Event("change"));
            timerButton.disabled = true;
        } else {
            let hrs = Math.floor(distance / (1000 * 60 * 60));
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
