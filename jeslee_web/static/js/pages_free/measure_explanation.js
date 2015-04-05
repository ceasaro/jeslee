/**
 * Created by ceasaro on 5-4-15.
 */

$(document).ready(function() {

	$('.image-popup-fit-width').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		image: {
			verticalFit: false
		}
	});

});