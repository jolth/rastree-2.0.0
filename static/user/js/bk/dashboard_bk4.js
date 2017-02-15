/* [ ---- Gebo Admin Panel - dashboard ---- ] */

	$(document).ready(function() {
		//* sortable/searchable list
		gebo_flist.init();
        
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
        jQuery('.sl_name').popover('hide');

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

	//* filterable list
	gebo_flist = {
		init: function(){
			//*typeahead
			var list_source = [];
			$('.user_list li').each(function(){
				var search_name = $(this).find('.sl_name').text();
				//var search_email = $(this).find('.sl_email').text();
				list_source.push(search_name);
			});
			$('.user-list-search').typeahead({source: list_source, items:5});
			
			var pagingOptions = {};
			var options = {
				valueNames: [ 'sl_name', 'sl_status', 'sl_email' ],
				page: 5,
				plugins: [
					[ 'paging', {
						pagingClass	: "bottomPaging",
						innerWindow	: 1,
						left		: 1,
						right		: 1
					} ]
				]
			};
			var userList = new List('user-list', options);
			
			$('#filter-online').on('click',function() {
				$('ul.filter li').removeClass('active');
				$(this).parent('li').addClass('active');
				userList.filter(function(item) {
					//if (item.values().sl_status == "online") {
					//if (item.values().sl_status == "on") {
					//if (item.values().sl_status == "True") {
					if (item.values().sl_status == "Encendido") {
						return true;
					} else {
						return false;
					}
				});
				return false;
			});
			$('#filter-offline').on('click',function() {
				$('ul.filter li').removeClass('active');
				$(this).parent('li').addClass('active');
				userList.filter(function(item) {
					//if (item.values().sl_status == "offline") {
					//if (item.values().sl_status == "off") {
					//if (item.values().sl_status == "False") {
					if (item.values().sl_status == "Apagado") {
						return true;
					} else {
						return false;
					}
				});
				return false;
			});
			$('#filter-none').on('click',function() {
				$('ul.filter li').removeClass('active');
				$(this).parent('li').addClass('active');
				userList.filter();
				return false;
			});
			
			$('#user-list').on('click','.sort',function(){
					$('.sort').parent('li').removeClass('active');
					if($(this).parent('li').hasClass('active')) {
						$(this).parent('li').removeClass('active');
					} else {
						$(this).parent('li').addClass('active');
					}
				}
			);
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

//* ubicación del vehículo en el mapa.
maps_vehicle = {
    init: function(){
        $('.sl_name').on(
            'click',
            function(){
                console.log('clic: ' + this);
            });
    }
};









