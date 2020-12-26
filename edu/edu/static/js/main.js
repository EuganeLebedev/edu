$(document).ready(function(){

    $(".answer").click(function(){
        let clickedItem = $(this);
        let my_answer = {};
        $(clickedItem.parent().children('ul').children().children('div')).each(function() {
            if ($(this).children('input[name="answer_radio"]').is(':checked')) {
                my_answer.question_id = $(this).children('input[name="question_id"]').val();
                my_answer.answer_id = $(this).children('input[name="answer_radio"]:checked').val();
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

                if (response.checked_answer.is_correct) {
                    console.log('+')
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


