import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import SignIn from './views/signin.vue'
import studySets from './views/StudySets.vue'
import Studying from './views/Studying.vue'
Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/sets',
      name: 'Study Sets',
      component: studySets
    },
    {
      path: '/study/:id',
      name: 'studying',
      component: Studying
    }
  ]
})
