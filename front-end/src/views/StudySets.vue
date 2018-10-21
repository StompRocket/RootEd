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
      sampleAPIReturn: {
        2345: "Bio Set",
        4232: "Second Set again"
      },
      sampleAPISetReturn: {
        words: {
          biology: {
            roots: ["bio", "logy"],
            definition:
              "The science of life and of living organisms, including their structure, function, growth, origin, evolution, and distribution. It includes botany and zoology and all their subdivisions."
          },
          biochemistry: {
            roots: ["bio", "chem"],
            definition:
              "The study of the chemical substances and vital processes occurring in living organisms; biological chemistry; physiological chemistry."
          }
        },
        roots: {
          bio: {
            def: "life",
            words: ["biology", "biochemistry"]
          },
          logy: {
            def: "the study of",
            words: ["biology", "psychology"]
          },
          chem: {
            def: "small atom thing",
            words: ["chemistry", "chemical"]
          }
        }
      },
      sets: {}
    };
  },
  created() {
    let idList = this.requestIds();
    console.log(idList);
    for (let id in idList) {
      let name = idList[id];
      console.log(id);
      this.sets[id] = {
        id: id,
        name: name,
        data: this.requestSets()
      };
    }
  },
  methods: {
    requestIds() {
      return this.sampleAPIReturn;
    },
    requestSets() {
      return this.sampleAPISetReturn;
    }
  }
};
</script>
