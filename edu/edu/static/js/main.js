$(document).ready(function(){

    $(".answer").click(function(){
        //window.alert($(this).parent().prop('nodeName'))
        let clickedItem = $(this);
        let my_list = "";
        $(clickedItem.parent().children('ul').children().children('div')).each(function() {
            my_list += $(this).children('input').prop('nodeName') ;
            my_list += ':' + $(this).children('label').prop('nodeName') + '\n';
        });
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_text: $(this).text(),
                answer_id:  my_list
            },
            success: function(response) {
                $(this).text(response.seconds)
                $(".answer").toggleClass('btn-success')
                $(".answer").toggleClass('btn-info')
                clickedItem.parent().toggleClass('bg-warning')
                //window.alert(clickedItem.parent().prop('nodeName'))
                $('#seconds').append('<li>' + response.seconds + ' ' + my_list  + '</li>')
            }
        });
    });
});