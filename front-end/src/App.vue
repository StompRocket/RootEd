<template>
  <div id="app">
    <div v-if="loading" class="loading">
      <h1>Loading...</h1>
    </div>
    <nav class="app__nav">
      <router-link to="/sets" class="nav__brand"><img src="@/assets/img/WordMark.png" alt="Rooted"></router-link>
    </nav>
    <router-view/>

  </div>

</template>

<script>
  import 'minireset.css'
  import '@/assets/scss/global.scss'
  export default {
    name: 'appContainer',
    data() {
      return {
        user: null,
        baseURL: 'http://178.128.71.36:80',
        loading: false
      }
    }
  }
</script>