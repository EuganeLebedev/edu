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
                //window.alert(clickedItem.parent().prop('nodeName'))

                //$('#seconds').append('<li>1' + JSON.stringify(response.checked_answer)  + '</li>')

                //clickedItem.parent().find("button.answer").remove()
                if (response.checked_answer.is_correct) {
                    console.log('+')
                    //clickedItem.parent().children(".alert").remove()
                    clickedItem.parent().find("div.alert").remove()
                    clickedItem.parent().append('<div class="alert alert-success" role="alert">Правильный ответ</div>')

                }
                else {
                    console.log('-')
                    clickedItem.parent().find("div.alert").remove()
                    clickedItem.parent().append('<div class="alert alert-warning" role="alert">Ошибка</div>')
                }
                $('#progress-bar').css({ 'width': JSON.stringify(response.progress) + '%' })
                $('#progress-bar').attr({ 'aria-valuenow': JSON.stringify(response.progress) })

                $('#answers_count').text(JSON.stringify(response.answer_count))

                clickedItem.parent().find("button.answer").remove()

                answer_list = []
                my_answer = {}
            }
        });
    });
});


