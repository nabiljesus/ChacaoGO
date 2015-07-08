   <script src="http://leafletjs.com/dist/leaflet.js"></script>
   <script>

      var map = L.map('map').setView([10.54562, -426.87142], 13);

      L.tileLayer('https://{s}.tiles.mapbox.com/v3/{id}/{z}/{x}/{y}.png', {
         maxZoom: 18,
         attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
            '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="http://mapbox.com">Mapbox</a>',
         id: 'examples.map-i875mjb7'
      }).addTo(map);


      var mark_police = L.icon({
       iconUrl: '/static/img/pin_police.png',
       shadowUrl: '/static/img/pin_shadow.png',

       iconSize:     [45, 45], // size of the icon
       shadowSize:   [45, 45], // size of the shadow
       iconAnchor:   [10, 45], // point of the icon which will correspond to marker's location
       shadowAnchor: [10, 45],  // the same for the shadow
       popupAnchor:  [0, -35] // point from which the popup should open relative to the iconAnchor
      });

      var mark_street = L.icon({
       iconUrl: '/static/img/pin_street.png',
       shadowUrl: '/static/img/pin_shadow.png',

       iconSize:     [45, 45], // size of the icon
       shadowSize:   [45, 45], // size of the shadow
       iconAnchor:   [10, 45], // point of the icon which will correspond to marker's location
       shadowAnchor: [10, 45],  // the same for the shadow
       popupAnchor:  [0, -35] // point from which the popup should open relative to the iconAnchor
      });

      var mark_service = L.icon({
       iconUrl: '/static/img/pin_service.png',
       shadowUrl: '/static/img/pin_shadow.png',

       iconSize:     [45, 45], // size of the icon
       shadowSize:   [45, 45], // size of the shadow
       iconAnchor:   [10, 45], // point of the icon which will correspond to marker's location
       shadowAnchor: [10, 45],  // the same for the shadow
       popupAnchor:  [0, -35] // point from which the popup should open relative to the iconAnchor
      });

      var mark_sports = L.icon({
       iconUrl: '/static/img/pin_sports.png',
       shadowUrl: '/static/img/pin_shadow.png',

       iconSize:     [45, 45], // size of the icon
       shadowSize:   [45, 45], // size of the shadow
       iconAnchor:   [10, 45], // point of the icon which will correspond to marker's location
       shadowAnchor: [10, 45],  // the same for the shadow
       popupAnchor:  [0, -35] // point from which the popup should open relative to the iconAnchor
      });

      var mark_culture = L.icon({
       iconUrl: '/static/img/pin_culture.png',
       shadowUrl: '/static/img/pin_shadow.png',

       iconSize:     [45, 45], // size of the icon
       shadowSize:   [45, 45], // size of the shadow
       iconAnchor:   [10, 45], // point of the icon which will correspond to marker's location
       shadowAnchor: [10, 45],  // the same for the shadow
       popupAnchor:  [0, -35] // point from which the popup should open relative to the iconAnchor
      });

      var mark_product = L.icon({
       iconUrl: '/static/img/pin_product.png',
       shadowUrl: '/static/img/pin_shadow.png',

       iconSize:     [45, 45], // size of the icon
       shadowSize:   [45, 45], // size of the shadow
       iconAnchor:   [10, 45], // point of the icon which will correspond to marker's location
       shadowAnchor: [10, 45],  // the same for the shadow
       popupAnchor:  [0, -35] // point from which the popup should open relative to the iconAnchor
      });

      var mark_help = L.icon({
       iconUrl: '/static/img/pin_help.png',
       shadowUrl: '/static/img/pin_shadow.png',

       iconSize:     [45, 45], // size of the icon
       shadowSize:   [45, 45], // size of the shadow
       iconAnchor:   [10, 45], // point of the icon which will correspond to marker's location
       shadowAnchor: [10, 45],  // the same for the shadow
       popupAnchor:  [0, -35] // point from which the popup should open relative to the iconAnchor
      });


      var mark_broken = L.icon({
       iconUrl: '/static/img/pin_broken.png',
       shadowUrl: '/static/img/pin_shadow.png',

       iconSize:     [45, 45], // size of the icon
       shadowSize:   [45, 45], // size of the shadow
       iconAnchor:   [10, 45], // point of the icon which will correspond to marker's location
       shadowAnchor: [10, 45],  // the same for the shadow
       popupAnchor:  [0, -35] // point from which the popup should open relative to the iconAnchor
      });

      var popup = L.popup();

      function onMapClick2(e) {
         popup
            .setLatLng(e.latlng)
            .setContent("Estoy en chacao :D en: " + e.latlng.toString())
            //.setContent("No toy en Chacao :(")
            .openOn(map);
      }

      var polip = L.polygon([
         [10.54562, -426.87142],
         [10.55028, -426.86803],
         [10.55091, -426.86635],
         [10.54899, -426.86221],
         [10.54669, -426.85957],
         [10.54383, -426.85736],
         [10.54134, -426.85266],
         [10.53853, -426.8455],
         [10.53933, -426.84438],
         [10.53946, -426.83846],
         [10.53845, -426.83507],
         [10.5338, -426.83876],
         [10.5284, -426.83709],
         [10.51161, -426.83807],
         [10.50465, -426.83674],
         [10.50018, -426.84048],
         [10.49646, -426.84378],
         [10.48887, -426.84344],
         [10.48368, -426.84382],
         [10.4838, -426.8497],
         [10.48254, -426.85219],
         [10.48503, -426.86133],
         [10.48769, -426.86914],
         [10.49355, -426.87108],
         [10.50461, -426.86648],
         [10.52018, -426.86344],
         [10.53731, -426.87155],
         [10.54558, -426.87163]
      ], {
         stroke: true,
         weight: 1,
         color: 'Red',
         fillOpacity: 0,
         Opacity: 1
      })
      
      polip.addTo(map)

      function onMapClick(e) {
         popup
            .setLatLng(e.latlng)
            .setContent("You clicked the map at " + e.latlng.toString())
            //.setContent("No toy en Chacao :(")
            .openOn(map);
      }

      //polip.addTo(map).bindPopup("Estoy en chacao :D en: " );


      //Markers
      // L.marker([10.49802, -426.85181], {icon: mark_police}).addTo(map);
      // L.marker([10.49794, -426.85756], {icon: mark_street}).addTo(map);
      // L.marker([10.49769, -426.86502], {icon: mark_service}).addTo(map);
      // L.marker([10.49304, -426.86013], {icon: mark_sports}).addTo(map);
      // L.marker([10.53144, -426.84709], {icon: mark_culture}).addTo(map);
      // L.marker([10.51541, -426.8397], {icon: mark_product}).addTo(map);
      // L.marker([10.51853, -426.86245], {icon: mark_help}).addTo(map);
      // L.marker([10.48393, -426.84571], {icon: mark_broken}).addTo(map);

      var customOptions =
          {
          'maxWidth': '150',
          'className' : 'custom'
          }

      var myInput = { 'PR' : [ {"X":10.49802,"Y":-426.85181,"nombre":'hi',"descripcion":'hola, soy texto descripcion del marker', "tipo":"ZP", "id": 0, "VIP":true}], 
         'VI' : [ {"X":10.50089,"Y": -426.8573,"nombre":'hi2',"descripcion":'hola, soy texto descripcion del marker', "tipo":"DEL", "id": 0, "VIP":false}] };

      for (var key in myInput) {
        //alert(key)
        if (myInput.hasOwnProperty(key)) {

         var ACT = myInput[key];
         var auxl =  ACT.length;
         //var iconact = mark_product

         switch(key) {
                case "SE":
                    var iconact = mark_police;
                    break;
                case "VI":
                    var iconact = mark_street;
                    break;
                case "DS":
                    var iconact = mark_service;
                    break;
                case "DE":
                    var iconact = mark_sports;
                    break;
                case "CU":
                    var iconact = mark_culture;
                    break;
                case "PR":
                    var iconact = mark_product;
                    break;
                case "SP":
                    var iconact = mark_help;
                    break;
                case "DM":
                    var iconact = mark_broken;
                    break;
                default:
                    var iconact = mark_police;
                    break;
         }


         for (var i = 0; i<auxl; i++){
             var typei = ACT[i]["tipo"]
             //alert(typei)
             switch(typei){
                    case "ZP": 
                       var subcate="Zona Peligrosa"; 
                       break;
                    case "DEL": 
                       var subcate="Delito"; 
                       break;
                    case "AS": 
                       var subcate="Actividad Sospechosa"; 
                       break;
                    case "AC": 
                       var subcate="Accidente"; 
                       break;
                    case "EM": 
                       var subcate="Embotellamiento"; 
                       break;
                    case "PV": 
                       var subcate="Peligro en la Vía"; 
                       break;
                    case "PR": 
                       var subcate="Protesta"; 
                       break;
                    case "AM": 
                       var subcate="Asistencia médica"; 
                       break;
                    case "SA": 
                       var subcate="Servicio de Agua"; 
                       break;
                    case "SE": 
                       var subcate="Servicio Eléctrico"; 
                       break;
                    case "RRS": 
                       var subcate="Recolección de Residuos Solidos"; 
                       break;
                    case "MA": 
                       var subcate="Maratón"; 
                       break;
                    case "ED": 
                       var subcate="Encuentro Deportivo"; 
                       break;
                    case "BA": 
                       var subcate="Bailoterapia"; 
                       break;
                    case "YO": 
                       var subcate="Yoga"; 
                       break;
                    case "CD": 
                       var subcate="Clase Deportiva"; 
                       break;
                    case "CO": 
                       var subcate="Concierto"; 
                       break;
                    case "FE": 
                       var subcate="Feria"; 
                       break;
                    case "OT": 
                       var subcate="Obra de Teatro"; 
                       break;
                    case "EA": 
                       var subcate="Exposición de arte"; 
                       break;
                    case "JD": 
                       var subcate="Jornada de Documentación"; 
                       break;
                    case "VPE": 
                       var subcate="Venta de Producto Escaso"; 
                       break;
                    case "JE": 
                       var subcate="Jornada Electoral"; 
                       break;
                    case "DES": 
                       var subcate="Descuento"; 
                       break;
                    case "DS": 
                       var subcate="Donación de sangre"; 
                       break;
                    case "SM": 
                       var subcate="Solicitud de Medicamento"; 
                       break;
                    case "JV": 
                       var subcate="Jornada Veterinaria"; 
                       break;
                    case "SV": 
                       var subcate="Solicitud de Voluntarios"; 
                       break;
                    case "CA": 
                       var subcate="Calles y avenidas"; 
                       break;
                    case "AC": 
                       var subcate="Aceras"; 
                       break;
                    case "PC": 
                       var subcate="Patrimonio Cultural"; 
                       break;
                    case "TE": 
                       var subcate="Terreno";
                       break;
                    default :
                       var subcate="Zona Peligrosa"; 
                       break;
             }
            //alert('webo')
            //alert(ACT[i].X);
            //alert('webo')
            if (ACT[i]["VIP"]){
                var tempmark = L.circleMarker([ACT[i]["X"], ACT[i]["Y"]], {color: '#FF0033'}).addTo(map);
            }
            var tempmark = L.marker([ACT[i]["X"], ACT[i]["Y"]], {icon: iconact}).addTo(map);
            var popup = L.popup()
             .setLatLng([ACT[i]["X"], ACT[i]["Y"]])
             .setContent("<b><h3>"+subcate+"</h3></b><hr>"+ACT[i]["descripcion"]+"<br><br><font color=\"cyan\"><div align=\"right\"><a href=\"events/"+ACT[i]["id"]+"\">+ detalles</a></div></font>")
             //.openOn(map)
            tempmark.bindPopup(popup,customOptions);
         }
            //
        }
      }

      map.on('click', onMapClick);
      map.fitBounds(polip.getBounds()); // max zoom to see whole polygon
      map.setMaxBounds(polip.getBounds()); // restrict map view to polygon bounds
      //map.zoomToExtent(polip.getBounds())
      //map.options.minZoom = map.getZoom(); // restrict user to zoom out 
      map.options.maxZoom = 19;
      map.options.minZoom = 14;
   </script>