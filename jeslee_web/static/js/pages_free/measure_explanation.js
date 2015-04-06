/**
 * Created by ceasaro on 5-4-15.
 */

$(document).ready(function() {

  var $generated_measuer_url_element = $('#generated_measure_url');

	$('.image-popup-fit-width').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		image: {
			verticalFit: false
		}
	});

  $('.measure_title').on('click', function() {
    var url = $generated_measuer_url_element.data('measure-url'),
      $clicked_title = $(this),
      $clicked_measure = $clicked_title.closest('.measure_explanation');
    $clicked_measure.toggleClass('selected_for_url');

    var measure_ids = [];
    $('.selected_for_url').each(function( index ) {
      measure_ids.push($(this).data('measure-id'));
      console.log($(this).data('measure-id'));
    });
    jQuery.ajaxSettings.traditional = true; // prevent jquery to add extra '[]'  (open- and close-bracket characters) as suffix to the parameter name
    $.getJSON(url, {'m': measure_ids}).done(function( data ) {
      url = data['url'];
      console.log('url = '+url);
      $generated_measuer_url_element.find('.direct_url').html(url)
    });

    $generated_measuer_url_element.show();
  });

});