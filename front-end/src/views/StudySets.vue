<template>
  <div class="page sets">
    sets
  </div>
</template>

<script>
  export default {
    name: 'StudySets',
    data() {
      return {
        sampleAPIReturn: {},
        sampleAPISetReturn: {},
        sets: {

        }
      }
    },
    created() {
      let idList  = this.requestIds()
      for (let key in idList) {
        let id = idList[key]
        this.sets[id] = this.requestSets()
      }
    },
    methods: {
      requestIds() {
        setTimeout(() => {
          return this.sampleAPIReturn
        }, 500)

      }, requestSets() {
        setTimeout(() => {
          return this.sampleAPISetReturn
        }, 500)

      }
    }
  }
</script>
