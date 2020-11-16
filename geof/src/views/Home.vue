<template>
  <div class="Home">
    <Header />
  <b-container-fluid>
  <b-row no-gutters>
    <b-col sm=2>
      <b-container>
        <h1 align="center">时空分析</h1>
        <b-button block v-b-toggle.collapse-a.collapse-b>CLASS A</b-button>
        <b-collapse id="collapse-a" class="mt-2">
         <b-button pill href='/#/dbscan' variant="outline-dark" block="true">DBSCAN</b-button>
        </b-collapse>
        <b-collapse id="collapse-b" class="mt-2">
         <b-button pill variant="outline-dark" block="true">METHOD</b-button>
        </b-collapse>
        <b-button block v-b-toggle.collapse-c.collapse-d>CLASS B</b-button>
        <b-collapse id="collapse-c" class="mt-2">
         <b-button pill variant="outline-dark" block="true">METHOD1</b-button>
        </b-collapse>
        <b-collapse id="collapse-d" class="mt-2">
         <b-button pill variant="outline-dark" block="true">METHOD2</b-button>
        </b-collapse>
      </b-container>
    </b-col>
    <b-col sm=10  col-md-offset-1>
    <Leaflet :msg=markmsg></Leaflet>
    </b-col>
  </b-row>
  </b-container-fluid>
  <Footer />
  </div>
</template>
<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import Leaflet from '@/components/Leaflet.vue'
export default {
  name: 'Home',
  components: {
    Header,
    Footer,
    Leaflet
  },
  data () {
    return {
      markmsg: '天安门'
    }
  },
  methods: {
  }
}
</script>

<style scoped>
h1 {
  font-size:30px;
  font: '微软雅黑';
}
</style>
