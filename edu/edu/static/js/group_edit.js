$(document).ready(function() {
  $(".search.group-users").keyup(function () {
    var searchTerm = $(".search.group-users").val();
    var listItem = $('.results.group-users tbody').children('tr');
    var searchSplit = searchTerm.replace(/ /g, "'):containsi('")

  $.extend($.expr[':'], {'containsi': function(elem, i, match, array){
        return (elem.textContent || elem.innerText || '').toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
    }
  });

  $(".results.group-users tbody tr").not(":containsi('" + searchSplit + "')").each(function(e){
    $(this).attr('visible','false');
  });

  $(".results.group-users tbody tr:containsi('" + searchSplit + "')").each(function(e){
    $(this).attr('visible','true');
  });

  var jobCount = $('.results.group-users tbody tr[visible="true"]').length;
    $('.counter').text(jobCount + ' item');

  if(jobCount == '0') {$('.no-result.group-users').show();}
    else {$('.no-result.group-users').hide();}
		  });


    $(".search.all-users").keyup(function () {
    var searchTerm = $(".search.all-users").val();
    var listItem = $('.results.all-users tbody').children('tr');
    var searchSplit = searchTerm.replace(/ /g, "'):containsi('")

  $.extend($.expr[':'], {'containsi': function(elem, i, match, array){
        return (elem.textContent || elem.innerText || '').toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
    }
  });

  $(".results.all-users tbody tr").not(":containsi('" + searchSplit + "')").each(function(e){
    $(this).attr('visible','false');
  });

  $(".results.all-users tbody tr:containsi('" + searchSplit + "')").each(function(e){
    $(this).attr('visible','true');
  });

  var jobCount = $('.results.all-users tbody tr[visible="true"]').length;
    $('.counter').text(jobCount + ' item');

  if(jobCount == '0') {$('.no-result.all-users').show();}
    else {$('.no-result.all-users').hide();}
		  });



		$(".all-users.user-add").click(function(){
        let clickedItem = $(this);
        let my_answer = {};
        let tableRow = $(this).parents('tr').html();

        $(this).parents('tr').addClass('test-class')
        $(this).parents('tr').remove()

        $('.table.group-users tbody').append('<tr>' + tableRow + '</tr>')

        $.ajax({
            url: '',
            type: 'get',
            data: {
                ajax_user_id: $(this).parents('tr').children('th').text(),
                action: 'add',
//                my_answer: JSON.stringify(my_answer)
            },
            success: function(response) {
//                $(this).text(response.seconds)
//
//                if (response.checked_answer.is_correct) {
//                    console.log('+')
//                    clickedItem.parent().find("div.alert").remove()
//                    clickedItem.parent().append('<div class="alert alert-success" role="alert">Правильный ответ</div>')
//
//                }
//                else {
//                    console.log('-')
//                }
//
//                clickedItem.parent().find("button.answer").remove()
//
//                answer_list = []
//                my_answer = {}
            }
        });
    })

});