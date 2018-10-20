<template>
  <div class="page signin">
    <p>signin</p>
  </div>
</template>

<script>
  import firebase from 'firebase'
  import 'firebase/auth'
  export default {
    name: "signin",
    mounted() {
      let provider = new firebase.auth.GoogleAuthProvider();
      firebase.auth().onAuthStateChanged((user) => {
        if (user) {
         this.$router.push('/sets')
        } else {
          firebase.auth().signInWithRedirect(provider);
        }
      });
    }
  }
</script>
