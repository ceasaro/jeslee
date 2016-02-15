'use strict';

$(document).ready(function() {

  var $generated_measure_container = $('#generated_measure_url_container');
  var $generated_measure_url_element = $('#generated_measure_url');

  $('.measure_title').on('click', function() {
    var url = $generated_measure_url_element.data('measure-url'),
      $clicked_title = $(this),
      $clicked_measure = $clicked_title.closest('.measure_explanation');
    $clicked_measure.toggleClass('selected_for_url');

    var measure_ids = [];
    $('.selected_for_url').each(function( index ) {
      measure_ids.push($(this).data('measure-id'));
      console.log($(this).data('measure-id'));
    });
    if (measure_ids.length > 0 ) {
      jQuery.ajaxSettings.traditional = true; // prevent jquery to add extra '[]'  (open- and close-bracket characters) as suffix to the parameter name
      $.getJSON(url, {'m': measure_ids}).done(function( data ) {
        var location_parts = window.location.href.split('/');
        var url = location_parts[0] + '//' + location_parts[2] + data['url'];
        $generated_measure_url_element.html(url);
      });
      $generated_measure_container.show();
    } else {
      $generated_measure_container.hide();
    }

  });

  $generated_measure_url_element.on('click', function() {
    selectText('generated_measure_url');
  });

  function selectText(containerid) {
    var range;
    if (document.selection) {
        range = document.body.createTextRange();
        range.moveToElementText(document.getElementById(containerid));
        range.select();
    } else if (window.getSelection) {
        range = document.createRange();
        range.selectNode(document.getElementById(containerid));
        window.getSelection().addRange(range);
    }
}
});