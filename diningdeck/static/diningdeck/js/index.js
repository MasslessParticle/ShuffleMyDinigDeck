function createAddressLink(address) {
    return $('<a />', {href : "http://maps.google.com/?q=" + address + ", Denver, Colorado"})
}

function buildSuggestions(response) {
    $('#suggestion-display').empty();

    var authendicated = response.authenticated;
    var restaurants = response.restaurants;

    for (var i = 0; i < restaurants.length; i++ ){
        var eatenLink = $('<a />')
        .attr('href', '#')
        .addClass('ate-here')
        .addClass('btn')
        .addClass('btn-sm')
        .addClass('btn-primary')
        .html("I've Eaten Here!");

        var registerLink = $('<a />')
        .attr('href', '/diningdeck/register')
        .addClass('btn')
        .addClass('btn-sm')
        .addClass('btn-primary')
        .html("Register to keep track of where you've eaten!");

        var colDiv = $('<div />', {class : "col-md-4"});
        var panelDiv = $('<div />', {class : "panel panel-primary"});
        var panelHeader = $('<div />', {class : "panel-heading"});
        var panelBody = $('<div />', {class : "panel-body"});
        var panelFooter = $('<div />', {class : "panel-footer text-center"});

        var detailList = $('<dt />', {class : "dl-horizontal"});
        var resturantUrl = "http://maps.google.com/?q="
            + encodeURIComponent(restaurants[i].name)
            + ", "
            + encodeURIComponent(restaurants[i].address)
            + ", Denver, Colorado";



        colDiv.append(panelDiv);
        panelDiv.append(panelHeader);
        panelDiv.append(panelBody);
        panelDiv.append(panelFooter);
        panelHeader.html(restaurants[i].name);
        panelBody.append($('<p />').html(restaurants[i].description));
        panelBody.append(detailList);

        if (authendicated) {
            panelFooter.append($('<p />').append(eatenLink));
        } else {
            panelFooter.append($('<p />').html(registerLink))
        }

        detailList.append($('<dt />').html("Neighborhood: "));
        detailList.append($('<dd />').html(restaurants[i].neighborhood));
        detailList.append($('<dt />').html("Cost: "));
        detailList.append($('<dd />').html(restaurants[i].cost));
        detailList.append($('<dt />').html("Address: "));
        detailList.append($('<dd />')
            .append($('<a />', {href : resturantUrl, target : "blank"})
                .html(restaurants[i].address)));
        detailList.append($('<dt />').html("Phone Number: "));
        detailList.append($('<dd />').html(restaurants[i].phone_number));

        $('#suggestion-display').append(colDiv);
    }

    $('#restaurant-display').show('slide');

    $('.ate-here').click(
      function (event){
        $(this).toggleClass('btn-primary btn-danger', 500);
        event.preventDefault();
      }
    );
}

$(document).ready(
  function (){
    $('#restaurant-display').hide();

	$('.tsp-menu').click(
      function(event) {
        var newText = $(this).text() + ' <span class="caret" />';
      	var buttonGroup = $(this).parents('.btn-group');
        $(buttonGroup).children('.btn').html(newText);
      }
    );

    $('#filter-button').click(
      function (event) {
      	var icon = $(this).children('.glyphicon');
        $(icon).toggleClass('glyphicon-plus-sign glyphicon-minus-sign', 500);
      }
    );

    $('#show-things').click(
      function (event){

        var formData = $('#stuff-select').serialize();
        var eatenAt = $('.btn-danger').parents('.panel-primary');

        for (var i = 0; i < eatenAt.length; i++){
            var restaurant = encodeURIComponent($(eatenAt[i]).children('.panel-heading').html());
            formData += "&eaten-at=" + restaurant;
        }

        $.ajax({
            url: "/diningdeck/getsuggestion/",
            type: "post",
            data:  formData,
            dataType: 'json',
            success: function(response) {
                $('#restaurant-display').hide('slide', function() {
                    buildSuggestions(response);
                });
            },
            error: function(response) {
                //TODO: Make a nicer error message
                alert('Request failed');
            }
        });

       $('.ate-here').each(
          function () {
            $(this).removeClass('btn-danger');
            $(this).addClass('btn-primary');
          }
        );

        event.preventDefault();
      }
    );

    $("#price-select").select2({
        placeholder: "Price",
        allowClear: true
    });

    $("#hood-select").select2({
        placeholder: "Neighborhood",
        allowClear: true
    });


  }()
);