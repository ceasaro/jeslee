"use strict";
jeslee.product_detail || (function($) {
    jeslee.product_detail = {
        init:function () {
            $('#product-form .sub-image').click(function(event) {
                event.preventDefault();
                var $sub_image = $(this),
                    $sub_image_index = $sub_image.data('slide-index');
                $('.cycle-slideshow').cycle('goto', $sub_image_index);

            });
        }
    };
})(jQuery);

$(document).ready(jeslee.product_detail.init);