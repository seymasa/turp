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
  $.ajax({
           url:  "/like",
            data: "postId="+id,
            type: 'POST',
            success: function(response) {
                   if(response=="1"){
                       $(this).html('<span class="glyphicon glyphicon-thumbs-up"></span> Liked')
                       document.getElementById("myBtn").disabled = true;
                   }
            },
            error: function(error) {
                console.log(error);
            }
        });
   return false;
});

