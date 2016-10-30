$(document).ready(function() {
    $('#id_amount').on('change', function() {
        var $taxInput = $('#id_tax'),
            $amountInput = $('#id_amount'),
            tax_value = $amountInput.val() * 0.21;
            $id_amout_tax_calculated = $('#id_amout_tax_calculated');
        if ($id_amout_tax_calculated.length > 0) {
            $id_amout_tax_calculated.html(tax_value);
        } else {
            $amountInput.after('&nbsp;&nbsp;<span>21% tax = </span><span id="id_amout_tax_calculated">'+tax_value+'</span>');
        }
        if (! $taxInput.val() ) {
            $taxInput.val(tax_value);
            $taxInput.css({backgroundColor: '#FF7700'});
            $taxInput.animate({backgroundColor: '#FFFFFF'}, 'slow');
        }
    })
});
