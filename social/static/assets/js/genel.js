/**
 * Created by seymas on 7/28/2016.
 */
function  Turpla()
{
  $.ajax({
            url: '/post',
            data: "turpMesaj="+$('#txtTurpMesaj').text(),
            type: 'POST',
            success: function(response) {
                   $('#turpListesi').prepend(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
}