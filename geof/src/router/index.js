import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import login from '../views/login.vue'
import register from '../views/register.vue'
import dbscan from '../views/dbscan.vue'
import Leaflet from '@/components/Leaflet.vue'

Vue.use(VueRouter)
Vue.use(Leaflet)
export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/dbscan',
      name: 'dbscan',
      component: dbscan
    }
  ]
})
