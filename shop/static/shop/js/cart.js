function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$(document).ready(function() {
     function updateSummPrice() {
         summPrice = 0;
         $(".price").each(function(i, elem) {
             $(elem).html(parseInt($(elem).attr("multiplier")) * parseInt($(elem).attr("default")) + "р.");
             summPrice += $(elem).attr("multiplier") * parseInt($(elem).attr("default"));
         });
         $(".summ-price").html(summPrice + "р.");
     }

    updateSummPrice();

    $("button").click(function(e) {
        multValue = parseInt($(this).siblings(".mult-value").val());
        if ($(this).html() == "+") {
            multValue++;
        } else if (multValue - 1 >= 1) {
            multValue--;
        }

        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                item_id: $(e.target).parent().data("id"),
                action: "change_count",
                new_count: multValue,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (data) {
                console.log(data);
                $(e.target).siblings(".mult-value").val(multValue);
                $(e.target).parent().parent().siblings(".price").attr("multiplier", multValue);
                updateSummPrice();
            },
            error: function (xhr, ajaxOptions, thrownError) {
                alert(xhr.status);
                alert(thrownError);
            }
        });
    });
});