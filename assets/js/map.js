var map;

var heatmapLayer = new google.maps.KmlLayer(null);
var pointLayers = [];


var sliders = [
    {'id': 'income',
     'name': 'Income',
     'low_label': 'Low',
     'high_label': 'High'},
    {'id': 'population', // TODO density
     'name': 'Population', // TODO density
     'low_label': 'Low',
     'high_label': 'High'},
    {'id': 'age',
     'name': 'Median Age',
     'low_label': 'Younger',
     'high_label': 'Older'},
    {'id': 'household',
     'name': 'Household Type',
     'low_label': 'Singles/Couples',
     'high_label': 'Families'},
    {'id': 'schools',
     'name': 'Distance to Schools',
     'low_label': 'Closer',
     'high_label': 'Further'},
    {'id': 'hospitals',
     'name': 'Distance to Hospitals',
     'low_label': 'Closer',
     'high_label': 'Further'}
];

function initialize() {
    var mapOptions = {
        center: new google.maps.LatLng(-35.3075, 149.1244),
        zoom: 11
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
				  mapOptions);
    displaySliders();
    loadHeatmapLayer();
}

function togglePointLayer(layerName) {
    if (pointLayers[layerName]['enabled']) {
	pointLayers[layerName]['layer'].setMap(null);
    } else {
	
    }
}

function displaySliders() {
    sliders.forEach(function (slider) {
	$('#sliders').append('<div class="slider"><label for="slider_' + slider['id'] + '">' + slider['name'] + '</label><input name="slider_' + slider['id'] + '" type="range" min="0" max="6" onchange="loadHeatmapLayer()" /></div>');
    });
}

function loadHeatmapLayer() {
    params = {}
    sliders.forEach(function (slider) {
	params[slider['id'] + '_val'] = $('[name=slider_' + slider['id'] + ']')[0].value;
	params[slider['id'] + '_weight'] = 2; // TODO fix
    });
    newHeatmapUrl = 'http://' + window.location.host + '/heatmap.kml?' + $.param(params);
    heatmapLayer.setMap(null);
    heatmapLayer = new google.maps.KmlLayer({
	url: newHeatmapUrl,
	preserveViewport: true,
	suppressInfoWindows: true,
	map: map});
}

google.maps.event.addDomListener(window, 'load', initialize);
