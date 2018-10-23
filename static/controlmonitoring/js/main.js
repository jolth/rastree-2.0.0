$(document).ready(function() {

  var lat;
  var lng;

  var google_maps = {

    start: function() {
    //function start() {
      var latlng = new google.maps.LatLng(lat,lng);
      var options = {
        zoom: 19,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      };
      var map = new google.maps.Map(document.getElementById("map_canvas"),
        options);

      var image = '/static/img/trunkgreen.png';
      var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        icon: image, 
        title: "Map"
      });
      google_maps.click_row();
      google_maps.events();
    },
    click_row: function() {
      $('.caption').click(function() {

        $('#mapModal').modal('show');

        var position = $(this).attr('data-position').split(",");
        lat = position[0].substring(1);
        lng = position[1].substring(0, position[1].indexOf(')'));
        
        var device = Object();
        device.street = $(this).attr('data-location');
        //device.position = $(this).attr('data-position');
        device.position = lat + ', ' + lng;
        children = $(this).contents("td");
        device.placa = children[2].outerText;
        device.id = children[1].outerText;
        device.ign = children[3].outerText;
        device.speed = children[4].outerText;
        device.datetime = children[5].outerText;
        device.link = "http://maps.google.com/maps?q=" + device.position; 

        $('#myLargeModalLabel').html(device.street);
        $('#info').html("<br><p><strong>placa: </strong>"+ device.placa +
        "</p><p><strong>id: </strong>"+ device.id +
        "</p><p><strong>street: </strong>"+ device.street +
        "</p><p><strong>position: </strong>" + device.position +
        "</p><p><strong>ignition: </strong>" + device.ign +
        "</p><p><strong>speed: </strong>" + device.speed +
        "</p><p><strong>datetime: </strong>" +  device.datetime + 
        "</p><p><strong>link: </strong><a href='"+ device.link + "' target=_blank>" + device.link + "</p>"
        );
      });
    },  
    events: function() {
      $('#mapModal').on('shown.bs.modal', function(e) {
        google.maps.event.addDomListener(document.getElementById("map_canvas"), 'load', google_maps.start());
      });

      $('#mapModal').on('hidden.bs.modal', function(e) {
        $('#map_canvas').html('<div></div>'); // establece una propiedad individual CSS
      });

      google.maps.event.addDomListener(document.getElementById("map_canvas"), 'resize', google_maps.start);
    },
  };

  // activate google maps 
  google_maps.start();

  /** overview.html **/
  $('#vehiclest').tableFilter();

/*
    $('.caption').click(function() {

        $('#mapModal').modal('show');

        var position = $(this).attr('data-position').split(",");
        lat = position[0].substring(1);
        lng = position[1].substring(0, position[1].indexOf(')'));
        
        var device = Object();
        device.street = $(this).attr('data-location');
        //device.position = $(this).attr('data-position');
        device.position = lat + ', ' + lng;
        children = $(this).contents("td");
        device.placa = children[2].outerText;
        device.id = children[1].outerText;
        device.ign = children[3].outerText;
        device.speed = children[4].outerText;
        device.datetime = children[5].outerText;
        device.link = "http://maps.google.com/maps?q=" + device.position; 

        $('#myLargeModalLabel').html(device.street);
        $('#info').html("<br><p><strong>placa: </strong>"+ device.placa +
        "</p><p><strong>id: </strong>"+ device.id +
        "</p><p><strong>street: </strong>"+ device.street +
        "</p><p><strong>position: </strong>" + device.position +
        "</p><p><strong>ignition: </strong>" + device.ign +
        "</p><p><strong>speed: </strong>" + device.speed +
        "</p><p><strong>datetime: </strong>" +  device.datetime + 
        "</p><p><strong>link: </strong><a href='"+ device.link + "' target=_blank>" + device.link + "</p>"
        );
    });
*/
/*  $('#mapModal').on('shown.bs.modal', function(e) {
    google.maps.event.addDomListener(document.getElementById("map_canvas"), 'load', google_maps.start());
  });

  $('#mapModal').on('hidden.bs.modal', function(e) {
    $('#map_canvas').html('<div></div>'); // establece una propiedad individual CSS
  });

  google.maps.event.addDomListener(document.getElementById("map_canvas"), 'resize', google_maps.start);
*/
});


