<template>
  <div id="app">
    <div v-if="loading" class="loading">
      <h1>Loading...</h1>
    </div>
    <nav class="app__nav">
      <router-link to="/sets" class="nav__brand">Rooted Vocab</router-link>
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
        baseURL: 'http://localhost:8081',
        loading: false
      }
    }
  }
</script>