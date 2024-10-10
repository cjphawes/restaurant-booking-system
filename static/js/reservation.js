window.onload = function() {
    let anyMessages = document.querySelector('.alert');

    if (anyMessages) {
        let modal = new bootstrap.Modal(document.getElementById('reservationModal'));
        modal.show();
    }
};

