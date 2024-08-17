<script>
    $(document).ready(function() {
        $('#reservationForm').submit(function(e) {
            e.preventDefault();

            $.ajax({
                type: 'POST',
                url: "{% url 'create_reservation' %}",
                data: $(this).serialize(),
                success: function(response) {
                    $('#form-success-message').show();
                    $('#reservationForm').trigger('reset');
                },
                error: function (response) {
                    alert('There was an error whilst making your reservation. Please try again.');
                }
            });
        })
    });
</script>