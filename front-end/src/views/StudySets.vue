<template>
  <div class="page sets">
    <div class="container">
      <br>
      <br>
      <div v-for="set in sets" class="set">
        <h1 class="set_heading__primary">{{set.name}}</h1>
        <br>
        <router-link :to='"/study/" + set.id' class="btn set_heading__secondary">Start Learning</router-link>
      </div>
    </div>
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
      fetch(this.$parent.baseURL + '/sets').then(response => response.json()).then(sets => {
        console.log(sets)
        for (let id in sets) {
          let name = sets[id]
          fetch(this.$parent.baseURL + '/set/'+id).then(response => response.json()).then(setData => {
            let set = {
              name: name,
              id: id,
              data: setData
            }
            this.sets.push(set)
          })
        }
      })

    }
  };
</script>
