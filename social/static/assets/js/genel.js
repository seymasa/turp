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
/*

<script>
$('#like').click(function(){
      $.ajax({
               type: "POST",
               url: "{% url 'like' %}",
               data: {'slug': $(this).attr('name'), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
               dataType: "json",
               success: function(response) {
                      alert(response.message);
                      alert('Company likes count is now ' + response.likes_count);
                },
                error: function(rs, e) {
                       alert(rs.responseText);
                }
          });
    })
</script>