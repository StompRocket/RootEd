<template>
  <div class="page sets">
    <div v-for="set in sets" :key="set.id" class="set">
      <h1 class="set__name">{{set.name}}</h1>
      <hr>
      <router-link :to="'/study/'+set.id">Learn Set</router-link>
      <div class="set__rootContainer" v-for="(rootData, root) in set.data.roots">
        <div class="set__root__wordsContainer">
          <p v-for="word in rootData.words">{{word}}</p>
        </div>
        <h1 class="set__root">{{root}}</h1>

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
      this.$parent.loading = true
      fetch(this.$parent.baseURL + '/sets').then(response => response.json()).then(data => {
        console.log(data);
        let idList = data
        for (let id in idList) {
          let name = idList[id];
          console.log(name)
          console.log(id);
          fetch(this.$parent.baseURL + '/set/' + id).then(response => response.json()).then(setData => {
            this.sets.push({
              id: id,
              name: name,
              data: setData
            })
            this.$parent.loading = false
          })

        }
      })

    },
    methods: {
      requestIds() {
        return this.sampleAPIReturn;
      },
      requestSets(setid) {

      }
    }
  };
</script>
