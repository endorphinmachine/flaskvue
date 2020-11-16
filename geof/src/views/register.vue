<template>
    <div class="register">
    <Header />
    <b-container fuild style="width:60%;height:700px;align:center">
        <b-form v-if="show">
        <b-form-group id="input-group-1" label-for="input-1" label="用户名" description="不超过20个字符">
          <b-form-input id="input-1" v-model="form.username" type="text" maxlength="20"></b-form-input>
        </b-form-group>
          <b-form-group id="input-group-2" label-for="input-2" label="密码" description="不超过20个字符">
        <b-form-input id="input-2" v-model="form.password" type="password" maxlength="20"></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-2" label-for="input-2" label="确认密码" description="">
          <b-form-input id="input-2" v-model="form.cpassword" type="password" maxlength="20"></b-form-input>
        </b-form-group>
        <b-button @click="submit" variant="success">注册</b-button>
        <b-button @click="onReset" variant="outline-primary">重置</b-button>
        </b-form>
        <b-card class="mt-3" header="">
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
  name: 'register',
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
      message: ''
    }
  },
  methods: {
    submit () {
      axios.post(
        'http://127.0.0.1:5000/register',
        {
          username: this.form.username,
          password: this.form.password,
          cpassword: this.form.cpassword
        })
        .then(response => { this.message = response.data })
        .catch(error => console.log(error))
    },
    onReset (evt) {
      evt.preventDefault()
      // Reset form values
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
