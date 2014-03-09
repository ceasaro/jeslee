/**
 * Created by PyCharm.
 * User: ceasaro
 * Date: 3/24/12
 * Time: 4:48 PM
 * To change this template use File | Settings | File Templates.
 */
"use strict";

var JESLEE_HEADQUATERS = new google.maps.LatLng(53.196041, 6.873017);

jeslee.route || (function ($) {
    var settings = {};
    jeslee.route = {

        init: function (params) {
            if (params && params.mapOptions && !params.mapOptions.center) {
                if (params.mapOptions.destinationLatLng) {
                    params.mapOptions.center = params.mapOptions.destinationLatLng;
                } else {
                    params.mapOptions.center = JESLEE_HEADQUATERS;
                }
            }
            var defaultOptions = {
                destinationLatLng: JESLEE_HEADQUATERS,
                mapCssId: 'map_canvas',
                directionsCssId: 'directions',
                $fromAddress: $('#fromAddress'),
                mapOptions: {
                    zoom: 16,
                    mapTypeId: google.maps.MapTypeId.HYBRID,
                    center: JESLEE_HEADQUATERS
                }

            };
            $.extend(true, settings, defaultOptions, params);

            var map = new google.maps.Map(document.getElementById(settings.mapCssId), settings.mapOptions);

            settings.directionsDisplay = new google.maps.DirectionsRenderer();
            settings.directionsDisplay.setPanel(document.getElementById(settings.directionsCssId));
            settings.directionsDisplay.setMap(map);

            /*
             var imageWidth = 107;
             var imageHeight = 107;
             var image = new google.maps.MarkerImage(
             'images/maps/marker-jeslee.jpg',
             new google.maps.Size(25, 35), // This marker is 107 pixels wide by 107 pixels tall.
             new google.maps.Point(imageWidth/2, imageHeight/2) // The origin for this image.
             ); // The anchor for this image.
             */

            var destinationMarker = new google.maps.Marker({
                position: settings.destinationLatLng,
                //icon: image,
                map: map
            });

            $('.calc-route-onsubmit').submit(function(event) {
                event.preventDefault();
                jeslee.route.calcRoute(settings.$fromAddress.val() + " nederland");
            });


        },

        calcRoute: function (origin) {
            var destination = settings.destinationLatLng;

            var request = {
                origin: origin,
                destination: destination,
                travelMode: google.maps.DirectionsTravelMode.DRIVING
            };

            var directionsService = new google.maps.DirectionsService();
            directionsService.route(request, function (response, status) {

                if (status == google.maps.DirectionsStatus.OK) {
                    settings.directionsDisplay.setDirections(response);
                }
            });
        }
    };
})(jQuery);
