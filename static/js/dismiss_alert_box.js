document.addEventListener("DOMContentLoaded", function () {
    let successAlert = document.getElementById("alert-message-box-success");
    let infoAlert = document.getElementById("alert-message-box-info");

    if (successAlert) {
        setTimeout(function () {
            bootstrap.Alert.getOrCreateInstance(successAlert).close();  // Auto-dismiss success after 1s
        }, 1000);
    }

    if (infoAlert) {
        setTimeout(function () {
            bootstrap.Alert.getOrCreateInstance(infoAlert).close();  // Auto-dismiss info after 2s
        }, 2000);
    }
});
