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
    $(".add-to-cart-btn").each(function(i, elem) {
        var itemId = $(elem).data("id");

        var cart = $(".item-list").data("cart");

        if (String(itemId) in cart) {
            $(elem).addClass("add-to-cart-btn-clicked");
        } else {
            $(elem).removeClass("add-to-cart-btn-clicked");
        }

    }).click(function(e) {
        if ($(this).hasClass("add-to-cart-btn-clicked")) {
            action = "remove";
        } else {
            action = "add";
        }

        if ((match = window.location.href.match(/\?s=(.*)/)) == [])
            search_item = "";
        else
            search_item = match[1];

        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                item_id: $(this).data("id"),
                action: action,
                search_item: search_item,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (data) {
                console.log(data);
                if (action == "remove") {
                    $(e.target).removeClass("add-to-cart-btn-clicked");
                } else {
                    $(e.target).addClass("add-to-cart-btn-clicked");
                }

            },
            error: function (xhr, ajaxOptions, thrownError) {
                alert(xhr.status);
                alert(thrownError);
            }
        });
    });
});