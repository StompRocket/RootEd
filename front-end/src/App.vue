<template>
  <div id="app">
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
        user: null
      }
    }
  }
</script>