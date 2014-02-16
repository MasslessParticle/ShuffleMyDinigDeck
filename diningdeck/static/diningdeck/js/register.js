function validateForm(){
    var username = $('#username').val();
    var password = $('#password').val();
    var passwordVerify = $('#password_verify').val();
    var valid = true;

    if (username === ""){
        $('#username').parents('.form-group').removeClass('has-success');
        $('#username').parents('.form-group').addClass('has-error');
        valid = false;
    } else {
        $('#username').parents('.form-group').removeClass('has-error');
        $('#username').parents('.form-group').addClass('has-success');
        valid = valid && true;
    }

    if (password === ""){
        $('#password').parents('.form-group').removeClass('has-success');
        $('#password').parents('.form-group').addClass('has-error');
        valid = false;
    } else {
        $('#password').parents('.form-group').removeClass('has-error');
        $('#password').parents('.form-group').addClass('has-success');
        valid = valid && true;
    }

    if (valid) {
        if (password !== passwordVerify) {
            $('#password_verify').parents('.form-group').removeClass('has-success');
            $('#password_verify').parents('.form-group').addClass('has-error');

            $('#password').parents('.form-group').removeClass('has-success');
            $('#password').parents('.form-group').addClass('has-error');
            valid = false;
        } else {
            $('#password_verify').parents('.form-group').removeClass('has-error');
            $('#password_verify').parents('.form-group').addClass('has-success');

            $('#password').parents('.form-group').removeClass('has-error');
            $('#password').parents('.form-group').addClass('has-success');
            valid = valid && true;
        }

        if (!valid) {
            $('#error_modal_content').html("Passwords do not match");
            $('#error_modal').modal({'show' : true});
        }

    } else {
        $('#error_modal_content').html("Username and password must not be blank.");
        $('#error_modal').modal({'show' : true});
    }

    return valid;
}

$(document).ready(
    function () {
        $('#submitButton').click(
            function (event) {
                event.preventDefault();
                if (validateForm()) {
                    $('#registerForm').submit();
                }
            }
        );
    }()
);