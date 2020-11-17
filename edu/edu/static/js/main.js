$(document).ready(function(){

    $(".answer").click(function(){
        //window.alert($(this).parent().prop('nodeName'))
        let clickedItem = $(this);
        //let my_answer = {};
        let my_answer = {};
        $(clickedItem.parent().children('ul').children().children('div')).each(function() {
            if ($(this).children('input[name="answer_radio"]').is(':checked')) {
                my_answer.question_id = $(this).children('input[name="question_id"]').prop('value')[0];
                my_answer.answer_id = $(this).children('input[name="answer_radio"]:checked').val();
                //console.log($(this).children('input[name="question_id"]').prop('value'));
                //$(this).children('input').prop('nodeName') ;
                //my_list += $(this).children('input[name="question_id"]').prop('nodeName') ;
                //my_list += ':' + $(this).children('label').prop('nodeName') + '\n';
            } else {
            }



        });
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_text: $(this).text(),
                my_answer: JSON.stringify(my_answer)
            },
            success: function(response) {
                $(this).text(response.seconds)
                //$(".answer").toggleClass('btn-success')
                //$(".answer").toggleType('hidden')
                clickedItem.parent().toggleClass('bg-warning')
                //window.alert(clickedItem.parent().prop('nodeName'))
                $('#seconds').append('<li>1' + JSON.stringify(response.checked_answer)  + '</li>')
                if (response.checked_answer.is_correct) {
                    console.log('+')
                    clickedItem.parent().append('<h1><div class="alert alert-success" role="alert">Правильный ответ</div></h1>')
                }
                else {
                    console.log('-')
                    clickedItem.parent().append('<h1><div class="alert alert-warning" role="alert">Ошибка</div></h1>')
                }

                answer_list = []
                my_answer = {}
            }
        });
    });
});


