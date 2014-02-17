$(document).ready(
  function (){
    $('#message').hide();

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