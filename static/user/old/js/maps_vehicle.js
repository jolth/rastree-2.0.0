/* [ ---- Panel - Eventos ---- ] */

$(document).ready(function() {
    //* maps vehicles
    maps_vehicle.init();
});

//* map vehicle 
map_vehicle = {
    init: function(lat, lng, zm, ubicacion){
            google.maps.event.addDomListener(window, 'load', map_vehicle.initialize(lat, lng, zm, ubicacion));
    },
    initialize: function(lat, lng, zm, ubicacion){
        var latlng = new google.maps.LatLng(lat,lng);
        var mapOptions = {
            zoom: zm,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById('map_canvas'),
                                      mapOptions);
        var image = '/static/img/trunkgreen.png';
        var marker = new google.maps.Marker({
          position: latlng,
          map: map,
          icon: image, 
          title: "Map"
        });

        var infowindow = new google.maps.InfoWindow(
            { content: '<b>Posición:</b> ' + latlng + '<br>' + '<b>Ubicación:</b> ' + ubicacion,
              size: new google.maps.Size(50,50),
              position: latlng
        });
        google.maps.event.addListener(marker, 'click', function() {
            //map.setZoom(8);
            infowindow.open(map, marker);
        });
    },
};

//* ubicación del vehículo en el mapa.
maps_vehicle = {
    init: function(){
        $('.ubica').on(
            'click',
            function(){
                var position = $(this).attr('data-position').split(",");
                var ubicacion = $(this).attr('data-content')
                map_vehicle.init(position[0], position[1], 19, ubicacion);
            });
    }
};

