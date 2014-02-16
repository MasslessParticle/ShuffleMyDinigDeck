$(document).ready(
  function (){
    $('#foo').hide();

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

        //return false;
      }
    );

    $('#show-things').click(
      function (event){
        $('#foo').hide('slide');

        $('.ate-here').each(
          function () {
            $(this).removeClass('btn-danger');
            $(this).addClass('btn-primary');
          }
        );

        //TODO: ajax stuff to get cards

        $('#foo').show('slide');
        return false;
      }
    );

    $('.ate-here').click(
      function (foo){
        $(this).toggleClass('btn-primary btn-danger', 500);
        return false;
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