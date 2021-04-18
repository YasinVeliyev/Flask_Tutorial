let mousePositionControl = new ol.control.MousePosition({
    coordinateFormat: ol.coordinate.createStringXY(4),
    projection: 'EPSG:4326',
    className: 'custom-mouse-position',
    target: document.getElementById('mouse-position'),
    undefinedHTML: '&nbsp;',
  })

function initialize(){
    new ol.Map({
        controls: ol.control.defaults().extend([mousePositionControl]),
        target: 'map-canvas',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([49.892, 40.3777]),
          zoom: 10
        })
      });
}

if (document.body){initialize()}

let projectionSelect = document.getElementById('projection');
projectionSelect.addEventListener('change', function (event) {
    mousePositionControl.setProjection(event.target.value);
});

let precisionInput = document.getElementById('precision');
precisionInput.addEventListener('change', function (event) {
    let format = ol.coordinate.createStringXY(event.target.valueAsNumber);
    mousePositionControl.setCoordinateFormat(format);
});

document.querySelector("#map-canvas").addEventListener('click',()=>{
    let LonLat = document.querySelector('.custom-mouse-position').innerHTML.split(', ')
    document.querySelector('#longitude').value = parseFloat(LonLat[0])
    document.querySelector('#latitude').value = parseFloat(LonLat[1])
})
