function loadBaiduMapAPI(){
    var oMapScript = document.createElement('script');
    oMapScript.src = 'http://api.map.baidu.com/api?v=3.0&ak=lpEePrfzT4iGz7yxVTowx2M8HS0nzTPn';
    document.head.appendChild(oMapScript);
}
class Map {
    constructor(id) {
        this.map = new BMap.Map("map");
        var point = new BMap.Point(113.265158, 23.154779);
        this.map.centerAndZoom(point, 15);
        this.map.enableScrollWheelZoom();
        this.points = new Array();
    };

    addPoints() {
        this.points = [{'lng':113.265158,'lat':23.154779,'count':Math.floor(Math.random()*100)},
        {'lng':113.331992,'lat':23.155377,'count':Math.floor(Math.random()*100)},
        {'lng':113.274393,'lat':22.99459,'count':Math.floor(Math.random()*100)}]
        for(var i = 0;i <100;i++){
            var lng = Math.floor(Math.random()*10000)/10000000;
            0.5 < Math.random()?null:lng = -lng;
            var lat = Math.floor(Math.random()*10000)/10000000;
            0.5 < Math.random()?null:lat = -lat;
            this.points.push({'lng':113.265158+lng,'lat':23.154779+lat,'count':Math.floor(Math.random()*100)})
            document.title = lng;
        }
    }

    addHotSpot() {
        var heatmapOverlay = new BMapLib.HeatmapOverlay({"radius":20});
	    this.map.addOverlay(heatmapOverlay);
	    this.addPoints();

	    heatmapOverlay.setDataSet({data:this.points,max:100});
	    //this.setGradient(heatmapOverlay);
	    heatmapOverlay.show();
    }
    setGradient(heatmapOverlay){
     	/*格式如下所示:
		{
	  		0:'rgb(102, 255, 0)',
	 	 	.5:'rgb(255, 170, 0)',
		  	1:'rgb(255, 0, 0)'
		}*/
     	var gradient = {};
     	var colors = document.querySelectorAll("input[type='color']");
     	colors = [].slice.call(colors,0);
     	colors.forEach(function(ele){
			gradient[ele.getAttribute("data-key")] = ele.value;
     	});
        heatmapOverlay.setOptions({"gradient":gradient});
    }
}