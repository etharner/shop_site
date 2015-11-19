$(document).ready(function() {
    prevHTML = "";
    prevObj = null;
    $("td").each(function(i, elem) {
        if (prevHTML == "") {
            prevHTML = $(elem).html();
            prevObj = elem
        } else {
            if ($(elem).html() == prevHTML) {
                $(elem).css("background-color", "blue");
                $(prevObj).css("background-color", "blue");
            }
        }
    })
});