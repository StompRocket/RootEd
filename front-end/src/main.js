import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './registerServiceWorker'
import firebase from 'firebase/app'
import 'firebase/auth'
Vue.config.productionTip = false
const config = {
  apiKey: "AIzaSyAjbBohnGzAnv7GKMPHHj1r7ivkvMfwr6E",
  authDomain: "rooted-vocab.firebaseapp.com",
  databaseURL: "https://rooted-vocab.firebaseio.com",
  projectId: "rooted-vocab",
  storageBucket: "",
  messagingSenderId: "863843373217"
};
firebase.initializeApp(config);
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
