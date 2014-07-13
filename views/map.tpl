<!DOCTYPE HTML>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="user-scalable=no, initial-scale=1.0, maximum-scale=1.0"/>
<meta name="apple-mobile-web-app-capable" content="yes"/>
<meta name="apple-mobile-web-app-status-bar-style" content="black">

<link rel="apple-touch-icon-precomposed" sizes="114x114" href="images/splash/splash-icon.png">
<link rel="apple-touch-startup-image" href="images/splash/splash-screen.png" 			media="screen and (max-device-width: 320px)" />  
<link rel="apple-touch-startup-image" href="images/splash/splash-screen@2x.png" 		media="(max-device-width: 480px) and (-webkit-min-device-pixel-ratio: 2)" /> 
<link rel="apple-touch-startup-image" sizes="640x1096" href="images/splash/splash-screen@3x.png" />
<link rel="apple-touch-startup-image" sizes="1024x748" href="images/splash/splash-screen-ipad-landscape" media="screen and (min-device-width : 481px) and (max-device-width : 1024px) and (orientation : landscape)" />
<link rel="apple-touch-startup-image" sizes="768x1004" href="images/splash/splash-screen-ipad-portrait.png" media="screen and (min-device-width : 481px) and (max-device-width : 1024px) and (orientation : portrait)" />
<link rel="apple-touch-startup-image" sizes="1536x2008" href="images/splash/splash-screen-ipad-portrait-retina.png"   media="(device-width: 768px)	and (orientation: portrait)	and (-webkit-device-pixel-ratio: 2)"/>
<link rel="apple-touch-startup-image" sizes="1496x2048" href="images/splash/splash-screen-ipad-landscape-retina.png"   media="(device-width: 768px)	and (orientation: landscape)	and (-webkit-device-pixel-ratio: 2)"/>

<title>Heat map</title>

<link href="styles/style.css"     		rel="stylesheet" type="text/css">
<link href="styles/framework.css" 		rel="stylesheet" type="text/css">
<link href="styles/owl.carousel.css" 	 rel="stylesheet" type="text/css">
<link href="styles/owl.theme.css" 		rel="stylesheet" type="text/css">
<link href="styles/swipebox.css"		 rel="stylesheet" type="text/css">
<link href="styles/colorbox.css"		 rel="stylesheet" type="text/css">

<script type="text/javascript" src="scripts/jquery.js"></script>
<script type="text/javascript" src="scripts/jqueryui.js"></script>
<script type="text/javascript" src="scripts/owl.carousel.min.js"></script>
<script type="text/javascript" src="scripts/jquery.swipebox.js"></script>
<script type="text/javascript" src="scripts/colorbox.js"></script>
<script type="text/javascript" src="scripts/snap.js"></script>
<script type="text/javascript" src="scripts/contact.js"></script>
<script type="text/javascript" src="scripts/custom.js"></script>
<script type="text/javascript" src="scripts/framework.js"></script>
<script type="text/javascript" src="scripts/framework.launcher.js"></script>


<style type="text/css">
	  #map-canvas { height: 400px; width: 100% }
	  
	  .two-thirds{
		width:62%;
		float:left;
		margin-right:4%;	
	}
    </style>
<script type="text/javascript"
      src="https://maps.googleapis.com/maps/api/js?sensor=false&key=AIzaSyAMjFBfOqfXql5zrvWlgiDoGHcttszVxIA">
    </script>
    <script type="text/javascript" src="scripts/map.js">
    </script>
    
</head>
<body>

<div id="preloader">
	<div id="status">
    	<p class="center-text">
			Loading the content...
            <em>Loading depends on your connection speed!</em>
        </p>
    </div>
</div>

<div class="top-deco"></div>

<div class="content">
	<div class="header">
    	<a href="#" class="homepage-logo">
    	  <img src="images/WhereAmI_web.jpeg" alt="img"> 
    	  </a>
    	<h1>Where Should I? </h1>
    	<a href="index.html" class="go-home">HOME</a>
        <a href="#" class="go-menu">MENU</a>
        <a href="#" class="go-back">CLOSE</a>
    </div>
    <div class="decoration"></div>
    
    <div class="navigation">
    	<div class="corner-deco"></div>
    	<div class="navigation-wrapper">
            <div class="navigation-item">
                <a href="index.html" class="home-icon">Homepage</a>
                <em class="inactive-menu"></em>
            </div>
            <div class="navigation-item">
                <a href="#" class="features-icon has-submenu">Features</a>
                <em class="dropdown-menu"></em>
              	<div class="submenu">
                    <a href="type.html">Typography		 <em></em></a>
                    <a href="jquery.html">jQuery		   <em></em></a>
                </div>
            </div>
            <div class="navigation-item">
                <a href="#" class="portfolio-icon has-submenu">Portfolios</a>
                <em class="dropdown-menu dropup-menu"></em>
                <div class="submenu active-submenu">
                	<a href="tile-folio.html">Tile Portfolio	<em></em></a>
                    <a href="one-column.html">One Column		<em class="selected-submenu"></em></a>
                    <a href="two-column.html">Two Column		<em></em></a>
                    <a href="three-column.html">Three Columns <em></em></a>
                </div>
            </div>
            <div class="navigation-item">
                <a href="#" class="gallery-icon has-submenu">Gallery</a>
                <em class="dropdown-menu"></em>
                <div class="submenu">
                	<a href="tile-gallery.html">Tile Gallery<em></em></a>
                    <a href="thumbnail-gallery.html">Thumb Gallery<em></em></a>
                </div>
            </div>
            <div class="navigation-item">
                <a href="videos.html" class="videos-icon">Videos</a>
                <em class="inactive-menu"></em>
            </div>
            <div class="navigation-item">
                <a href="contact.html" class="contact-icon">Contact</a>
                <em class="inactive-menu"></em>
            </div>
        </div>
    </div>
</div>

<div class="content">
    <div class="container no-bottom">
        <h4>Heat map</h4>
        
        <div class="container">
            <div class="two-thirds">
                <div>
                    <div id="map-canvas"></div>        
                </div>
            </div>
            
            <div class="one-third last-column">
                <div class="tabs">
                    <a href="#" class="tab-but tab-but-1 tab-active">Basic</a>
                    <a href="#" class="tab-but tab-but-2">Advanced</a>   
                </div>
                <div class="clear"></div>
                <div class="tab-content tab-content-1">
                    <div id="sliders"></div>
                </div>
                <div class="tab-content tab-content-2">
                    <div id="sliders-advanced"></div>
                </div>
            </div>
        </div>
    </div>

   
	<div class="decoration"></div>            
    <div class="footer">
        <div class="socials">
            <a href="#" class="twitter-icon"></a>
            <a href="#" class="google-icon"></a>
            <a href="#" class="facebook-icon"></a>
        </div>
        <div class="clear"></div>
        <p class="copyright">
            COPYRIGHT 2014.<br>
            ALL RIGHTS RESERVED
        </p>
    </div> 
    
</div>

<div class="bottom-deco"></div>



</body>
</html>
