<template>
  <div class="login">
    <Header />
    <b-container fuild style="width:60%;height:700px;align:center">
      <b-form v-if="show">

      <b-form-group id="input-group-1" label-for="input-1" label="用户名" description=" ">
        <b-form-input id="input-1" v-model="form.username" type="text" maxlength="20"></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label-for="input-2" label="密码" >
        <b-form-input id="input-2" v-model="form.password" type="password" maxlength="20"></b-form-input>
      </b-form-group>
      <b-button @click="onSubmit" variant="success">登录</b-button>
      <b-button @click="onReset" variant="outline-primary">重置</b-button>
      </b-form>
      <b-card class="mt-3" header="登录状态">
      <pre class="m-0">{{ message }}</pre>
      </b-card>
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import axios from 'axios'
export default {
  name: 'login',
  components: {
    Header,
    Footer
  },
  data () {
    return {
      form: {
        username: '',
        password: ''
      },
      show: true,
      message: '您尚未登录'
    }
  },
  methods: {
    onSubmit () {
      axios.post('http://127.0.0.1:5000/login', {
        username: this.form.username,
        password: this.form.password
      })
        .then(response => {
          this.message = response.data
        })
        .catch(error => console.log(error))
    },
    onReset (evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.username = ''
      this.form.password = ''
      // Trick to reset/clear native browser form validation state
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
