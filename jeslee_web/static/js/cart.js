"use strict";
jeslee.cart || (function($) {
    jeslee.cart = {
        init:function () {
            console.log("cart loaded.");
            var $shipping_address_inline = $('#shipping-address-inline'),
                $checkout_form_bank_account = $('#checkout-form-bank-account'), // payment method nr. 1
                $checkout_form_credit_card = $('#checkout-form-credit-card'); // payment method nr. ???

            $('#place-oder-button').click(function(event) {
               event.preventDefault();
                $('#checkout-form').submit();
            });

            $('#id_no_shipping').click(function(event) {
                if ($(this).is(':checked')) {
                    $shipping_address_inline.slideUp();
                } else {
                    $shipping_address_inline.slideDown();
                }
            });

            $('input[name="payment_method"]').click(function(event) {
                var $clicked_radio = $(this),
                    $clicked_method_id = $(this).data('payment-method');
                $('.payment-method-form').slideUp();
                if ($clicked_method_id == 1) {
                    $checkout_form_bank_account.slideDown()
                }
//                else if ($clicked_method_id == ?) {
//                    $checkout_form_credit_card.slideDown()
//                }

            });

        }
    };
})(jQuery);

$(document).ready(jeslee.cart.init);