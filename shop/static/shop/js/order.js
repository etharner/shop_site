$(document).ready(function() {
    $(".post-order-btn").keydown(function (e) {
        if (e.which == 13)
            e.preventDefault();
    });
});