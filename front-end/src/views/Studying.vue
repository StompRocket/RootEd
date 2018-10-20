<template>
  <div>

  </div>
</template>

<script>
  export default {
    name: "studying",
    data() {
      return {
        studySet: {
          "words": {
            "biology": {
              "roots": ["bio", "logy"],
              "definition": "The science of life and of living organisms, including their structure, function, growth, origin, evolution, and distribution. It includes botany and zoology and alltheir subdivisions."
            }, "biochemistry": {
              "roots": ["bio", "chem"],
              "definition": "The study of the chemical substances and vital processes occurring in living organisms; biological chemistry; physiological chemistry."
            }
          },
          "roots": {"bio": "Life", "logy": "The study of", "chem": "Small Atom Things"}
        }
      }
    },
    mounted() {
      let root = {
        root: this.studySet.roots["bio"],
        def: this.studySet.roots["bio"]
      }

    }
  };
</script>
