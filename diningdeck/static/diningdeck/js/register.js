/**
This file is part of Shuffle My Dining Deck.

Shuffle My Dining Deck is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Shuffle My Dining Deck is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

Author: Travis Patterson (masslessparticle@gmail.com)
*/

//Initial validation of the registrationa form
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
        //Add validation to submit response.
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