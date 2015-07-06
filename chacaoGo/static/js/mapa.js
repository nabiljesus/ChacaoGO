function loadMap(){
  dojo.require("esri.map");
    dojo.require("dijit.layout.ContentPane");
    dojo.require("dijit.layout.BorderContainer");
    var map;
  function Init() {
      dojo.style(dojo.byId("map"), { width: dojo.contentBox("map").w + "px", height: (esri.documentBox.h - dojo.contentBox("navTable").h - 40) + "px" });
      map = new esri.Map("map");
      var layer = new esri.layers.ArcGISTiledMapServiceLayer("http://200.74.193.82/ArcGIS/rest/services/RETOCHACAO/infomapa1/MapServer");
      map.addLayer(layer);
      var resizeTimer;
                              dojo.connect(map, 'onLoad', function(theMap) {
                                dojo.connect(dijit.byId('map'), 'resize', function() {
                                  clearTimeout(resizeTimer);
                                  resizeTimer = setTimeout(function() {
                                    map.resize();
                                    map.reposition();
                                   }, 500);
                                 });
                               });
    }
    dojo.addOnLoad(Init);
}
    