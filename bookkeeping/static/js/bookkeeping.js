/**
 * Created by ceasaro on 11-9-14.
 */

$(document).ready(function() {
    var $financial_form = $('.financial-form');
    var remove_items_name = $financial_form.data('remove-items-name');
    $financial_form.find('[data-remove-item-id]').on('click', function(event) {
        event.preventDefault();
        var $item = $(this);
        var surrounding_tr = $item.parent().closest('tr');
        var item_id = $item.data('remove-item-id');
        if (surrounding_tr.hasClass('disabled')) {
            surrounding_tr.removeClass('disabled');
            $financial_form.find('input[value='+item_id+']').remove();
        } else {
            var html_hidden_input = '<input type="hidden" name="' + remove_items_name + '" value="' + item_id + '" />';
            $financial_form.append(html_hidden_input);
            surrounding_tr.addClass('disabled');
        }
    });

    $financial_form.find('[data-edit-item-id]').on('click', function(event) {

    });

});