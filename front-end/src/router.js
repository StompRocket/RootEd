import Vue from 'vue'
import Router from 'vue-router'
import SignIn from './views/signin.vue'
import studySets from './views/StudySets.vue'
import Studying from './views/Studying.vue'
import Test from './views/Test.vue'
import firebase from 'firebase/app'
import 'firebase/auth'
Vue.use(Router)

let router =  new Router({
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
      component: studySets,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/study/:id',
      name: 'studying',
      component: Studying,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/test',
      name: 'test',
      component: Test,
      meta: {
        requiresAuth: true
      }
    }
  ]
})
router.beforeEach((to, from, next) => {
 if (to.meta.requiresAuth) {
   if (firebase.auth().currentUser) {
     next()
   } else {
     next('/')
   }
 } else {
   next()
 }
})
export default router
