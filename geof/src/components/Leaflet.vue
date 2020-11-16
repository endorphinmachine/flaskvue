<template>
  <div id="mymap"></div>
</template>

<script>
import * as L from 'leaflet'
var mymap
var markers
// 创建icon
var yellow = L.divIcon({
  html: '<div style="width: 10px;height: 10px; background-color:#FFFF00;"></div>',
  className: 'icon'
})
var purple = L.divIcon({
  html: '<div style="width: 10px;height: 10px; background-color:#AFEEEE;"></div>',
  className: 'icon'
})
var black = L.divIcon({
  html: '<div style="width: 10px;height: 10px; background-color:#000000;"></div>',
  className: 'icon'
})
var navy = L.divIcon({
  html: '<div style="width: 10px;height: 10px; background-color:#000080;"></div>',
  className: 'icon'
})
var indigo = L.divIcon({
  html: '<div style="width: 10px;height: 10px; background-color:#4B0082;"></div>',
  className: 'icon'
})
var cyan = L.divIcon({
  html: '<div style="width: 10px;height: 10px; background-color:#E0FFFF;"></div>',
  className: 'icon'
})
var orange = L.divIcon({
  html: '<div style="width: 10px;height: 10px; background-color:#F4A460;"></div>',
  className: 'icon'
})
var red = L.divIcon({
  html: '<div style="width: 10px;height: 10px; background-color:#FF0000;"></div>',
  className: 'icon'
})
var iconLib = { '-1': black, 0: yellow, 1: purple, 2: navy, 3: indigo, 4: cyan, 5: orange, 6: red }
export default {
  name: 'mymap',
  props: ['data'],
  data () {
    return {
      mymap: null,
      OSMUrl: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    }
  },
  mounted () {
    var OSM = L.tileLayer(this.OSMUrl)
    markers = L.layerGroup()
    mymap = L.map('mymap', {
      center: [39.91, 116.40],
      zoom: 13,
      layers: [OSM, markers]
    })
    var baseLayer = { OSM: OSM }
    var overLayer = { markers: markers }
    L.control.layers(baseLayer, overLayer).addTo(mymap)
  },
  watch: {
    data: (n, o) => {
      let pointdata = []
      pointdata = n
      var coord = pointdata[1].coordinates
      var labels = pointdata[2]
      for (let i = 0; i < labels.length; i++) {
        var lat = coord[i][1]
        var lng = coord[i][0]
        var category = labels[i]
        var marker = L.marker([lat, lng], { icon: iconLib[category] }).addTo(markers).bindPopup('第' + category + '类')// eslint-disable-line no-unused-vars
      }
    }
  },

  methods: {
  }
}
</script>
<style scoped>
#mymap {
  width: 100%;
  height: 900px;
  margin: 0px;
}
</style>
