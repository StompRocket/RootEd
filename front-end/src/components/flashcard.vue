<template>
  <div class="flashcard" @click="frontshow = !frontshow;">
    <div class="front-text" v-if="frontshow">
      root: {{front}}
    </div>
    <div class="back-text" v-if="!frontshow">
      {{back}}
    </div>
  </div>
</template>
<script>
import Vue from "vue";
export default {
  name: "flashcard",
  props: ["front", "back"],
  data() {
    return {
      frontshow: true
    };
  },
  watch: {
    front(){
      this.frontshow = true;
    }
  }
};
</script>

<style>
.flashcard {
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 3px 1px -2px rgba(0, 0, 0, 0.12), 0 1px 5px 0 rgba(0, 0, 0, 0.2);
  height: 100%;
  width: 100%;
  cursor: pointer;
}
.flashcard div {
  position: relative;
  top: 50%;
  transform: perspective(1px) translateY(-50%);
  font-size: 4em;
  text-align: center;
}
.flashcard div::selection {
  background: transparent;
}
</style>
