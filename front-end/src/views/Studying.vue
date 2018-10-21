<template>
  <div>
    <div class="flashcard-container">
      <flashcard :front="current.name" :back="current.def"/>
    </div>
    <div class="controls">
      <button @click="shift(0)">left</button>
      <button @click="shift(1)">right</button>
    </div>
  </div>
</template>

<script>
  import flashcard from "@/components/flashcard";

  export default {
    name: "studying",
    data() {
      return {
        studySet: {},
        flashId: 0,
        rootsArray: []
      };
    },
    created() {
      let setid = this.$route.params.id
      console.log(setid, 'setId')
      this.studySet = this.fetchSet()
      for (let index in this.studySet.roots) {
        this.rootsArray.push({
          name: index,
          def: this.studySet.roots[index].def,
          words: this.studySet.roots[index].words
        })
      }

      /*
      setTimeout(() => {
        let unprocessed = {
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
          roots: { bio: "Life", logy: "The study of", chem: "Small Atom Things" }
        };
        this.studySet.words = unprocessed.words;
        this.studySet.roots = unprocessed.roots;
        this.studySet.proroots = [];
        for (let elem in unprocessed.roots) {
          this.studySet.proroots.push({
            root: elem,
            def: unprocessed.roots[elem]
          });
        }
        this.curent = this.studySet.proroots[this.flashid];
      }, 500);
      */
    },
    methods: {
      fetchSet() {
        return {
          "words": {
            "biology": {
              "roots": [
                "bio",
                "logy"
              ],
              "definition": "The science of life and of living organisms, including their structure, function, growth, origin, evolution, and distribution. It includes botany and zoology and all their subdivisions."
            },
            "biochemistry": {
              "roots": [
                "bio",
                "chem"
              ],
              "definition": "The study of the chemical substances and vital processes occurring in living organisms; biological chemistry; physiological chemistry."
            }
          },
          "roots": {
            "bio": {
              def: 'life',
              words: ['biology', 'biochemistry']
            },
            "logy": {
              def: 'the study of',
              words: ['biology', 'psychology']
            },
            "chem": {
              def: 'small atom thing',
              words: ['chemistry', 'chemical']
            }
          }
        }
      },
      shift(dir) {
        if (dir === 0) {

          if (0 == this.flashId) {
            this.flashId = this.rootsArray.length -1
          } else {
            this.flashId--
          }

        } else {
         
          if (this.rootsArray.length === this.flashId + 1) {
            this.flashId = 0
          } else {
            this.flashId++
          }

        }
      }
    },
    components: {
      flashcard
    },
    computed: {
      current() {
        return this.rootsArray[this.flashId]
      }
    }

  };
</script>

<style>
  .flashcard-container {
    padding: 40px;
    height: 600px;
  }
</style>

