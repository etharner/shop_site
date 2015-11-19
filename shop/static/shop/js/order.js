$(document).ready(function() {
    $(".field select").val($(".pay_method").attr("method"));

    $(".post-order-btn").keydown(function (e) {
        if (e.which == 13)
            e.preventDefault();
    });
});