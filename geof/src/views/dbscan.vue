<template>
  <div class="Home">
    <Header />
  <b-container-fluid>
    <b-row no-gutters>
    <b-col sm="2">
      <b-container>
        <b-form v-if="true">
          <b-form-group id="input-group-1" label-for="input-1" label="邻域半径">
            <b-form-input id="input-1" v-model="form.eps" type="text" maxlength="20" placeholder="浮点型"></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-2" label-for="input-2" label="最小样本">
            <b-form-input id="input-2" v-model="form.mins" type="text" maxlength="5" placeholder="整型"></b-form-input>
          </b-form-group>
            <b-button @click="submit" variant="dark">提交</b-button>
            <b-button @click="reset" variant="outline-primary">重置</b-button>
        </b-form>
        <b-card class="mt-3" header="聚类结果(黑色为噪声)">
        <pre class="m-0">{{ result }}</pre>
        </b-card>
      </b-container>
    </b-col>
    <b-col sm="10">
      <leaflet :data=allData></leaflet>
    </b-col>
    </b-row>
  </b-container-fluid>
  <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import leaflet from '@/components/Leaflet.vue'
import axios from 'axios'
export default {
  name: 'dbscan',
  components: {
    Header,
    Footer,
    leaflet
  },
  data () {
    return {
      form: {
        eps: '',
        mins: ''
      },
      result: '请输入参数',
      json: '',
      labels: '',
      allData: []
    }
  },
  methods: {
    submit () {
      axios.post('http://127.0.0.1:5000/dbscan', {
        eps: this.form.eps,
        mins: this.form.mins
      })
        .then(response => {
          this.result = response.data[0]
          this.json = response.data[1]
          this.labels = response.data[2]
          this.allData = response.data
        })
        .catch(error => console.log(error))
    },
    reset (evt) {
      evt.preventDefault()
      this.form.eps = ''
      this.form.mins = ''
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style scoped>

</style>
