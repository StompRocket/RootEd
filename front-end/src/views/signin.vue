<template>
  <div class="page signin">
    <h1>Sign in</h1>
  </div>
</template>

<script>
  import firebase from 'firebase/app'
  import 'firebase/auth'
  export default {
    name: "signin",
    mounted() {
      let provider = new firebase.auth.GoogleAuthProvider();
      firebase.auth().onAuthStateChanged((user) => {
        if (user) {
          this.$parent.user = {
            uid: user.uid,
            email: user.email
          }
          this.$router.push('/sets')

        } else {
          firebase.auth().signInWithRedirect(provider);
        }
      });
    }
  }
</script>
