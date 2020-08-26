$(document).ready(function(){

    $(".answer").click(function(){
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_text: $(this).text()
            },
            success: function(response) {
                $(".answer").text(response.seconds)
                $(".answer").removeClass('btn-success')
                $(".answer").addClass('btn-info')
                $('#seconds').append('<li>' + response.seconds  + '</li>')
            }
        });
    });
});