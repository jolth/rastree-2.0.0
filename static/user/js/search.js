/* [ ---- Panel - search ---- ] */

	$(document).ready(function() {
		//* table filter
		table_filter.init();
        
        //* resize map
        var mapHeight = jQuery(document).height();
        jQuery('#map_canvas').height(mapHeight-(mapHeight*11.50/100));
        // google-chrome
        jQuery(document).load(function(){
            var mapHeight = jQuery(this).height();
            jQuery('#map_canvas').height(mapHeight-(mapHeight*11.50/100));
        });
        //
        jQuery(window).resize(function(){
            var mapHeight = jQuery(this).height();
            jQuery('#map_canvas').height(mapHeight-(mapHeight*11.50/100));
        });

        //* popovers
        //jQuery('tbody tr').popover('toggle');
        //jQuery('.sl_name').popover('show');
        //jQuery('.sl_name').popover('hide');

		//* resize elements on window resize
		/*var lastWindowHeight = $(window).height();
		var lastWindowWidth = $(window).width();
		$(window).on("debouncedresize",function() {
			if($(window).height()!=lastWindowHeight || $(window).width()!=lastWindowWidth){
				lastWindowHeight = $(window).height();
				lastWindowWidth = $(window).width();
				//* rebuild calendar
				//$('#calendar').fullCalendar('render');
			}
		});*/

        //* google map
        //map_dashboard.init();
        //map_dashboard.init(5.06798, -75.51738);
        map_dashboard.init(5.06798, -75.51738, 6);

        //* maps vehicles
        maps_vehicle.init();
	});

	//* table filter
	//gebo_flist = {
	table_filter = {
		init: function(){
			//*typeahead
			var list_source = [];
			$('.table tr').each(function(){
				var search_name = $(this).find('.sl_name').text();
				//var search_email = $(this).find('.sl_email').text();
				list_source.push(search_name);
			});
			$('.user-list-search').typeahead({source: list_source, items:5});

            $('.user-list-search').change(function(){
                        var vehiculo = $(this).attr('value');
                        //console.log('cambia: ' + vehiculo);
                        $('#'+vehiculo).removeClass('hide');
                    });
		}
	};

//* google map 
map_dashboard = {
    init: function(lat, lng, zm){
        /*var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = 'https://maps.googleapis.com/maps/api/js?sensor=fale' 
        //script.src = 'https://maps.googleapis.com/maps/api/js?sensor=false&' +  
                     //'callback=map_dashboard.initialize(5.06798, -75.51738)';
        document.body.appendChild(script);*/
        google.maps.event.addDomListener(window, 'load', map_dashboard.initialize(lat, lng, zm));
    },
    initialize: function(lat, lng, zm){
        var mapOptions = {
            //zoom: 8,
            zoom: zm,
            //center: new google.maps.LatLng(5.06798,-75.51738),
            center: new google.maps.LatLng(lat, lng),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById('map_canvas'),
                                      mapOptions);
    },
    /*start: function(){
        google.maps.event.addDomListener(window, 'load', initialize);
    }*/
};

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
            //center: new google.maps.LatLng(lat, lng),
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
            { //content: '<b>Posición:</b> ' + latlng + '<br>' + '<b>Ubicación:</b> ' + ubicacion,
              content: '<b>Ubicación:</b> ' + ubicacion,           
              size: new google.maps.Size(50,50),
              position: latlng
        });
        google.maps.event.addListener(marker, 'click', function() {
            //map.setZoom(8);
            infowindow.open(map, marker);
        });
    },
    /*start: function(){
        google.maps.event.addDomListener(window, 'load', initialize);
    }*/
};

//* ubicación del vehículo en el mapa.
maps_vehicle = {
    init: function(){
        $('.sl_name').on(
            'click',
            function(){
                //console.log('clic: ' + this);
                //console.log('position: ' + $(this).attr('data-position'));
                //map_vehicle.init($(this).attr('data-position'), 19);
                var position = $(this).attr('data-position').split(",");
                var ubicacion = $(this).attr('data-content')
                map_vehicle.init(position[0], position[1], 19, ubicacion);
                //console.log('position: ' + $(this).attr('data-position'));
                //console.log('[position]: ' + position[0]);
                //console.log(ubicacion);
            });
    }
};

