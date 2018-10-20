<template>
  <div id="app">
    <router-view/>
  </div>

</template>

<script>
  import 'minireset.css'
  import '@/assets/scss/global.scss'
  export default {
    name: 'appContainer'
  }
</script>