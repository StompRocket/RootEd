<template>
  <div class="page sets">
    <h1 class="sets__percentDone">85%</h1>
    <p class="sets__encouragingStatement">You're almost there!</p>
    <button class="btn sets__continue">Continue</button>
  </div>
</template>

<script>
  import "@/assets/scss/sets.scss";

  export default {
    name: "StudySets",
    data() {
      return {
        sets: []
      };
    },
    created() {


    }
  };
</script>
