window.onload = function() {
    let alerts = document.querySelectorAll('.alert');

    if (alerts) {
        alerts.forEach(alert => {
            setTimeout(function() {
                alert.classList.add("fade");

                setTimeout(function() {
                    alert.remove();
                }, 300);
            }, 3000);
        });
    }
};

