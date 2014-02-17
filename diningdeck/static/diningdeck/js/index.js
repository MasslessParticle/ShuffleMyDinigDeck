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

function createAddressLink(address) {
    return $('<a />', {href : "http://maps.google.com/?q=" + address + ", Denver, Colorado"})
}

function buildSuggestions(response) {
    $('#suggestion-display').empty();

    var authenticated = response.authenticated;
    var restaurants = response.restaurants;

    if (restaurants.length === 0) {
        var alertDiv = $('<div />')
            .addClass('alert')
            .addClass('alert-danger');

        $(alertDiv).html("No restaurants match your search. ")

        var alertLink = $('<a />')
            .addClass('alert-link')
            .attr('href', '/diningdeck/restaurants/');

        if (authenticated) {
            $(alertLink).html("Have you eaten everywhere?");
            $(alertDiv).append(alertLink);
        }

        $('#suggestion-display').append(alertDiv);
    }

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

        if (authenticated) {
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
        placeholder: "Max Price",
        allowClear: true
    });

    $("#hood-select").select2({
        placeholder: "Neighborhood",
        allowClear: true
    });


  }()
);