/**
 * Created by seymas on 7/28/2016.
 */
function  Turpla() {
    var message=$("#txtTurpMesaj").text();

  $.ajax({
            url: '/signUpUser',
            data: message,
            type: 'POST',
            success: function(response) {
                   $('#postListesi').append(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
}