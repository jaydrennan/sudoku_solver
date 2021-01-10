$(document).ready(function() {
         $("form").submit(function(event) {
         var form_data = JSON.stringify($(this).serializeArray());

       $.ajax({
          data : form_data,
           type : 'POST',
           dataType : 'json',
           url : '/json',
           contentType : 'application/json'
           })
        .done(function(data) {
            console.log(data)
            var y =0;
            for (y = 0; y < 9 ; y++){
                var x =0;
                var row_solution ='';
                for(x = 0; x < 9; x++)
                {
                    var y_str = y.toString();
                    var x_str = x.toString();
                    var key = x_str.concat(y_str)
                    row_solution = row_solution.concat(data[key].toString());
                    if(x == 8){
                        var row_name = '#row'
                        row_name = row_name.concat(y.toString())
                        $(row_name).text(row_solution)
                    }
                }
            }
          $('#answer').text(full_solution);

      });
      event.preventDefault();
      });

});




