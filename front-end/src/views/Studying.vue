<template>
  <div>
    <div class="flashcard-container">
      <flashcard front="vote no" back="on you"/>
    </div>
  </div>
</template>

<script>
import flashcard from "@/components/flashcard";
export default {
  name: "studying",
  data() {
    return {
      studySet: {
        words: {
          biology: {
            roots: ["bio", "logy"],
            definition:
              "The science of life and of living organisms, including their structure, function, growth, origin, evolution, and distribution. It includes botany and zoology and alltheir subdivisions."
          },
          biochemistry: {
            roots: ["bio", "chem"],
            definition:
              "The study of the chemical substances and vital processes occurring in living organisms; biological chemistry; physiological chemistry."
          }
        },
        roots: { bio: "Life", logy: "The study of", chem: "Small Atom Things" }
      }
    };
  },
  mounted() {
    let root = {
      root: this.studySet.roots["bio"],
      def: this.studySet.roots["bio"]
    };
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

