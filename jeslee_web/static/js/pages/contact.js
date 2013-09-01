/**
 * Created by PyCharm.
 * User: ceasaro
 * Date: 3/24/12
 * Time: 4:48 PM
 * To change this template use File | Settings | File Templates.
 */

var map;
var CENTER_MAPS = new google.maps.LatLng(53.196041, 6.873017);
var TENNIS_COURT_ALOE = new google.maps.LatLng(53.196041, 6.873017);

function maps_initialize() {

    var myOptions = {
        zoom:16,
        mapTypeId: google.maps.MapTypeId.HYBRID,
//        mapTypeId: google.maps.MapTypeId.ROADMAP,
        center: CENTER_MAPS
    };
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

    directionsDisplay = new google.maps.DirectionsRenderer();
    directionsDisplay.setPanel(document.getElementById("directions"));
    directionsDisplay.setMap(map);
    /*
     var imageWidth = 107;
    var imageHeight = 107;
    var image = new google.maps.MarkerImage(
        'images/maps/marker-jeslee.jpg',
        new google.maps.Size(25, 35), // This marker is 107 pixels wide by 107 pixels tall.
        new google.maps.Point(imageWidth/2, imageHeight/2) // The origin for this image.
    ); // The anchor for this image.
*/

    var marker = new google.maps.Marker({
        position: TENNIS_COURT_ALOE,
        //icon: image,
        map: map
    });

}

function calcRoute() {
    var origin = document.getElementById("fromAddress").value + " nederland";
    var destination = TENNIS_COURT_ALOE;//new google.maps.LatLng(52.34786600014047, 5.009175000001558);

    var request = {
        origin: origin,
        destination:destination,
        travelMode: google.maps.DirectionsTravelMode.DRIVING
    };

    var directionsService = new google.maps.DirectionsService();
    directionsService.route(request, function(response, status) {

        if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
        }
    });
}

google.maps.event.addDomListener(window, 'load', maps_initialize);
/*
 jQuery(document).ready(function () {
 maps_initialize();
 });
 */