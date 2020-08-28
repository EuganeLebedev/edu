$(document).ready(function(){

    $(".answer").click(function(){
        //window.alert($(this).parent().prop('nodeName'))
        let clickedItem = $(this);
        //let my_answer = {};
        let answer_list = []
        $(clickedItem.parent().children('ul').children().children('div')).each(function() {

            let my_answer = {};
            my_answer.question_id = $(this).children('input[name="question_id"]').prop('value')[0];
            console.log($(this).children('input[name="question_id"]').prop('value'));
            //$(this).children('input').prop('nodeName') ;
            //my_list += $(this).children('input[name="question_id"]').prop('nodeName') ;
            //my_list += ':' + $(this).children('label').prop('nodeName') + '\n';
            answer_list.push(JSON.stringify(my_answer))

        });
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_text: $(this).text(),
                answer_list:  answer_list
            },
            success: function(response) {
                $(this).text(response.seconds)
                $(".answer").toggleClass('btn-success')
                $(".answer").toggleClass('btn-info')
                clickedItem.parent().toggleClass('bg-warning')
                //window.alert(clickedItem.parent().prop('nodeName'))
                $('#seconds').append('<li>' + response.seconds + ' ' + answer_list  + '</li>')
            }
        });
    });
});