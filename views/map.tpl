<!DOCTYPE html>
<html>
<head><title>Where should I?</title></head>
<body>
<style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      .map { height: 100%; width: 80%; float: left; clear: both;}
      #sliders { height: 100%; width: 20%; float: right; clear: both; }
    </style>
<script type="text/javascript" src="http://code.jquery.com/jquery-2.1.1.min.js"></script>
<script type="text/javascript"
      src="https://maps.googleapis.com/maps/api/js?sensor=false&key=AIzaSyAMjFBfOqfXql5zrvWlgiDoGHcttszVxIA">
    </script>
    <script type="text/javascript" src="/js/map.js">
    </script>
</body>
<div style="height: 100%;">
<div class="map">
<div class="map" id="map-canvas" />
</div>
</div>
<div id="sliders" />
</html>