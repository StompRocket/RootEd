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
      firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
         this.$router.push('/')
        } else {
          firebase.auth().signInWithRedirect(provider);
        }
      });
    }
  }
</script>
