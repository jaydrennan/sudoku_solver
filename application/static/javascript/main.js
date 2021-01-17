$(document).ready(function () {

    $("form").change(function (event) {
        var form_data = JSON.stringify($(this).serializeArray());
        $.ajax({
            data: form_data,
            type: 'POST',
            dataType: 'json',
            url: '/solve',
            contentType: 'application/json',
            success: function (data) {
                var y = 0;
                for (y = 0; y < 9; y++) {
                    var x = 0;
                    for (x = 0; x < 9; x++) {
                        var y_str = y.toString();
                        var x_str = x.toString();
                        var key = x_str.concat(y_str);
                        var key_location = '#'.concat(key);
                        var solution = ''.concat(data[key].toString());

                        if (solution != '0') {
                            $(key_location).attr("placeholder", solution);
                        } else if (solution == '0') {
                            $(key_location).attr("placeholder", "");
                            $(key_location).attr("value", "");
                        }
                    }
                }
                $(".error-message").hide();
            },
            error: function (data) {
                $(".error-message").show().css("display", "flex");
                return false;
            }
        })
        event.preventDefault();
    });
    $("#clear").on("click", function () {
        $(".error-message").hide();
        $(".sudoku-input").trigger("reset");
        $("input").attr("placeholder", "");
    });
})
;