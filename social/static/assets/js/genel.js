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
    var button = $(this);
  $.ajax({
           url:  "/like",
            data: "postId="+id,
            type: 'POST',
            success: function(response) {
                console.log(response);
                   if(response=="1"){
                       button.html('<span class="glyphicon glyphicon-thumbs-up"></span> Liked');
                       button.addClass("liked")
                   } else {
                       button.html('Like');
                       button.removeClass("liked");
                   }
            },
            error: function(error) {
                console.log(error);
            }
        });
   return false;
});

