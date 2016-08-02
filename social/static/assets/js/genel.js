/**
 * Created by seymas on 7/28/2016.
 */
function Turpla()
{
  $.ajax({
            url: '/post',
            data: "turpMesaj="+$('#txtTurpMesaj').val(),
            type: 'POST',
            success: function(response) {
                   $('#turpListesi').prepend(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
}

$(document).on('click', '.button-like', function () {
   var id = $(this).data("id");
   console.log(id);
   return false;
});
