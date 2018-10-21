<template>
  <div>
    <div class="flashcard-container" v-if="curent.def">
      <flashcard :front="curent.root" :back="curent.def"/>
    </div>
    <div class="controls">
      <button @click="shift('left')">left</button><button @click="shift('right')">right</button>
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
      curent: {},
      flashid: 0
    };
  },
  mounted() {
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
  },
  methods: {
    shift(dir) {
      console.log(dir);
      if (dir == "left" && this.flashid > 0) {
        this.flashid--;
      } else if (
        dir == "right" &&
        this.flashid < this.studySet.proroots.length - 1
      ) {
        this.flashid++;
      }
      this.curent = this.studySet.proroots[this.flashid];
      //console.log(this.flashid);
    }
  },
  components: {
    flashcard
  }
};
</script>

<style>
.flashcard-container {
  padding: 40px;
  height: 600px;
}
</style>

