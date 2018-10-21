<template>
    
</template>

<script>
export default {
  name: "test",
  data() {
    return {
      words: {}
    };
  },
  created() {
    setTimeout(() => {
      let someting = {
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
      };
    }, 0.5);
  }
};
</script>

<style>
</style>
