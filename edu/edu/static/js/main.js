$(document).ready(function(){

    $(".answer").click(function(){
        //window.alert($(this).parent().prop('nodeName'))
        let clickedItem = $(this)
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_text: $(this).text()
            },
            success: function(response) {
                $(this).text(response.seconds)
                $(".answer").toggleClass('btn-success')
                $(".answer").toggleClass('btn-info')
                clickedItem.parent().toggleClass('bg-warning')
                window.alert(clickedItem.parent().prop('nodeName'))
                $('#seconds').append('<li>' + response.seconds  + '</li>')
            }
        });
    });
});