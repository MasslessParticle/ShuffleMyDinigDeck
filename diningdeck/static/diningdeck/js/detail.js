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

$(document).ready(
  function (){
    $('#message').hide();

    //When the eaten buttons are clicked, change their color.
    $('.eaten-btn').click(function (event) {
        if($(this).attr('class').indexOf('btn-success') > 0) {
            $(this).removeClass('btn-success');
            $(this).addClass('btn-danger');
            $(this).html("I've Eaten Here");
        } else {
            $(this).removeClass('btn-danger');
            $(this).addClass('btn-success');
            $(this).html("I Haven't Eaten Here");
        }

        event.preventDefault();
    });

    //Gather a form and post it to save where the user has eaten
    $('#save-button').click(function(event){
        var formData = $('#save-form').serialize();
        var buttons = $('.eaten-btn');

        for (var i = 0; i < buttons.length; i++){
            var button = buttons[i];
            var buttonRestaurant = $(button).parents('tr').children("td[class!='text-center']").html();

            if($(button).attr('class').indexOf('btn-success') >= 0){
                formData += "&not-eaten=" + encodeURIComponent(buttonRestaurant);
            } else {
                formData += "&eaten=" + encodeURIComponent(buttonRestaurant);
            }
        }

        $.ajax({
            url: "/diningdeck/saverestaurants/",
            type: "post",
            data:  formData,
            dataType: 'json',
            success: function(response) {
                var alertButton =
                    '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>'

                var alert = $('#message');
                var message = "";

                if (response.success){
                    $(alert).removeClass('alert-danger');
                    $(alert).addClass('alert-success');
                    message = "Restaurants saved";
                } else {
                    $(alert).removeClass('alert-success');
                    $(alert).addClass('alert-danger');
                    message = "There was an issue saving your restaurants.";
                }

                $(alert).html(alertButton + message);
                $(alert).show();
            },
            error: function(response) {
                //TODO: Make a nicer error message
                alert('Request failed');
            }
        });
        event.preventDefault();
    });

  }()
);