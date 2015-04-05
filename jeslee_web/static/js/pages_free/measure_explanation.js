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
      $clicked_title = $(this);
    $clicked_title.toggleClass('selected_for_url');

    var $selected_measures = $('.selected_for_url');
    $.getJSON(url, get_data).done(function( data ) {
      url = data['url'];
      console.log('url = '+url);
      $generated_measuer_url_element.find('.direct_url').html(url)
    });

    $generated_measuer_url_element.show();
  });

});