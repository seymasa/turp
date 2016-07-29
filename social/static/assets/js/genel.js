/**
 * Created by seymas on 7/28/2016.
 */
$("#turp-form").submit(function(){
  $.ajax({
            url: '/signUpUser',
            data: "message="+message,
            type: 'POST',
            success: function(response) {
                   $('#postListesi').prepend(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
}