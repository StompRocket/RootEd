<template>
  <div id="app">
    <div v-if="loading" class="loading">
      <h1 class="loading__header">Loading...</h1>
    </div>
    <nav class="app__nav">
      <router-link to="/sets" class="nav__brand"><img src="@/assets/img/WordMark.png" alt="Rooted"></router-link>
      <button class="btn btn__small logout btn__dark" @click="logout">Logout</button>
    </nav>
    <router-view/>

  </div>

</template>

<script>
  import 'minireset.css'
  import '@/assets/scss/global.scss'
  import firebase from 'firebase/app'
  import 'firebase/auth'

  export default {
    name: 'appContainer',
    data() {
      return {
        user: null,
        baseURL: 'http://rootedserver.stomprocket.io',
       // baseURL: 'http://localhost:8081',
        loading: false
      }
    },
    methods: {
      logout() {
        firebase.auth().signOut().then(() => {
          // Sign-out successful.
          this.$router.push('/')
        }).catch(function (error) {
          console.log(error)
          // An error happened.
        });
      }
    }
  }
</script>