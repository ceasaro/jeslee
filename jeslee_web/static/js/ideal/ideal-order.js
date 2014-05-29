/**
 * Created by ceasaro on 5/29/14.
 */

"use strict";
jeslee.ideal_order || (function($) {
    var _io = {
        init:function () {
            setTimeout(function() {
                $('#ideal-pay-form').submit();
            }, 3000)
        }
    };
    jeslee.ideal_order = _io;
})(jQuery);

$(document).ready(jeslee.product_detail.init);