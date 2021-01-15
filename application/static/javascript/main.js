$(document).ready(function () {


    // $("#sudoku-input").validate();

// submit

$("form").on("keyup",function (event) {
    var form_data = JSON.stringify($(this).serializeArray());

    $.ajax({
        data: form_data,
        type: 'POST',
        dataType: 'json',
        url: '/solve',
        contentType: 'application/json'
    })
        .done(function (data) {
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
                    }

                }
            }
            //$('#answer').text(full_solution);

        });
    event.preventDefault();
});

$("#clear").on("click", function () {
    for (y = 0; y < 9; y++) {
        var x = 0;
        var row_solution = '';
        for (x = 0; x < 9; x++) {

            var y_str = y.toString();
            var x_str = x.toString();
            var key = x_str.concat(y_str);
            var key_location = '#'.concat(key);

            $(key_location).attr("placeholder", "").val("");

        }
    }
});

})
;




