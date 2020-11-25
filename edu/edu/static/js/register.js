$(document).ready(function(){

    $('#id_username').keyup(function () {
                // create an AJAX call
                $.ajax({
                    data: $(this).serialize(), // get the form data
                    url: "",
                    type: "get",
                    // on success
                    success: function (response) {
                        if (response.is_taken == true) {
                            $('#id_username').removeClass('is-valid').addClass('is-invalid');
                            $('#id_username').after('<div class="invalid-feedback d-block" id="usernameError">This username is not available!</div>')
                        }
                        else {
                            $('#id_username').removeClass('is-invalid').addClass('is-valid');
                            $('#usernameError').remove();

                        }

                    },
                    // on error
                    error: function (response) {
                        // alert the error if any error occured
                        console.log(response.responseJSON.errors)
                    }
                });

                return false;
            });

            $("#id_password2").keyup(function () {
                let pass = $('input[name=password1]').val();
                let repass = $('input[name=password2]').val();
                if ( pass == repass) {
                    $('#id_password2').removeClass('is-invalid').addClass('is-valid');
                    $('#password2Error').remove();
                }
                else {
                  $('#id_password2').removeClass('is-valid').addClass('is-invalid');
                    $('#password2Error').remove();
                  $('#id_password2').after('<div class="invalid-feedback d-block" id="password2Error">Пароли не совпадают!</div>')
                };
            });
});


