<template>
  <div class="page study">
    <div v-if="current.type == 'root'" id="flashcard">
      <div class="full_height__minus_nav place_center">
        <h1 class="study__heading">{{current.root}}</h1>
        <b class="stick__bottom light">Scroll to view definition</b>
      </div>

      <div class="full_height place_center padding_thin">
        <div class="container">
          <h1 class="study__heading roots__def">{{current.root}}: <b class="dark">{{current.def}}</b></h1>
        </div>
        <div>

          <a class="btn btn__dark" @click="studyAgain">Study Again</a>
          <br>
          <a class="btn" @click="right">I got it right</a>

        </div>
      </div>
    </div>
    <div v-if="current.type == 'word'" id="quiz">

      <div v-if="!submited" class="full_height__minus_nav place_center">
        <h1 class="study__heading dark">{{current.word}}</h1>
        <div v-if="answers" class="study__optionsGrid">
          <div class="study__optionContainer" v-for="(i, answer) in answers">
            <button @click="evaluate(answer, i)" class="studyOption btn">{{answer}}</button>

          </div>
        </div>

      </div>

      <div v-if="submited" class="full_height place_center">
        <div class="container">
          <h1 class="study__heading">{{current.word}}: <b class="dark">{{current.def}}</b></h1>

          <h2 class="study__wrong" v-if="userDef">You Said: {{userDef}}</h2>
        </div>
        <div>

          <a class="btn" @click="run">Continue</a>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import firebase from 'firebase/app'
  import 'firebase/database'

  export default {
    name: "studying",
    data() {
      return {
        set: {},
        combined: {},
        current: [],
        answers: [],
        firstRun: true,
        userDef: false,
        submited: false,
        correct: true
      }
    },
    created() {
      this.$parent.loading = true
      firebase.database().ref('/userStates/' + firebase.auth().currentUser.uid + '/').once('value').then(snap => {
        if (snap.val()) {
          this.combined = snap.val()
          this.fistRun = false
          this.$parent.loading = false
          console.log('loaded from server')
          this.run()
        } else {
          fetch(this.$parent.baseURL + '/set/' + this.$route.params.id).then(response => response.json()).then(data => {
            this.set = data;
            this.$parent.loading = false
            console.log('loaded from new')
            this.run()
          })
        }
      })

    },
    methods: {
      evaluate(answer, i) {
        console.log(answer, i);
        this.answers = [];
        this.submited = true;

        if (i) {
          this.correct = true
          for (let index in this.current.roots) {
            let root = this.current.roots[index]
            this.combined[root].weight--;
            // console.log(this.combined[this.current.root].weight, this.combined[this.current.root])
            fetch(this.$parent.baseURL + '/root/' + root).then(res => res.json()).then(wordList => {
              // console.log(wordList)
              for (let index in wordList) {
                let word = wordList[index]
                if (this.combined[word]) {
                  //console.log('weight decreased', word)
                  this.combined[word].weight--;
                }
                // console.log(word, this.combined[word].weight)

                //console.log(this.combined[word].weight)

              }

            })
          }


        } else {
          this.userDef = answer
          this.correct = false

        }
        window.scrollTo(0, document.body.scrollHeight)
      },
      run() {
        this.submited = false
        window.scrollTo(0, 0)
        if (this.firstRun) {
          this.compute()
          this.firstRun = false
          console.log('computning')
        }
        firebase.database().ref('/userStates/' + firebase.auth().currentUser.uid + '/').set(this.combined)
        this.userDef = false

        this.current = this.getWeightedQuestion()

      },
      getWeightedQuestion() {
        let weighted = []
        for (let index in this.combined) {
          console.log(this.combined[index], 'item')
          if (this.combined[index].weight > 0) {
            for (let i = 0; i < this.combined[index].weight; i++) {
              weighted.push(this.combined[index])
            }
          }


        }
        console.log(weighted, 'weighted')
        // console.log(weighted)
        let randomNumber = Math.floor(Math.random() * (weighted.length - 1)) + 0
        let word = weighted[randomNumber]
        if (typeof word == 'object') {
          //console.log(word, randomNumber, weighted.length)
          if (word.type == 'word') {
            fetch(this.$parent.baseURL + '/possible/' + word.word).then(res => res.json()).then(possibleDefs => {
            //  console.log(possibleDefs)

              //item.answers = possibleDefs

              this.answers = possibleDefs

            })
            return word
          } else {
            return word
          }
        }



        //console.log(item)

      },
      studyAgain() {
        if (this.current.type === 'root') {
          this.combined[this.current.root].weight++;
          // console.log(this.combined[this.current.root].weight, this.combined[this.current.root])
          fetch(this.$parent.baseURL + '/root/' + this.current.root).then(res => res.json()).then(wordList => {
            // console.log(wordList)
            for (let index in wordList) {
              let word = wordList[index]
              if (this.combined[word]) {
                //console.log('weight decreased', word)
                this.combined[word].weight--;
              }
              // console.log(word, this.combined[word].weight)

              //console.log(this.combined[word].weight)

            }
            this.run()
          })
        }
      },
      right() {
        if (this.current.type === 'root') {
          this.combined[this.current.root].weight--;
          // console.log(this.combined[this.current.root].weight, this.combined[this.current.root])
          fetch(this.$parent.baseURL + '/root/' + this.current.root).then(res => res.json()).then(wordList => {
            // console.log(wordList)
            for (let index in wordList) {
              let word = wordList[index]
              if (this.combined[word]) {
                //console.log('weight decreased', word)
                this.combined[word].weight++;
              }
              // console.log(word, this.combined[word].weight)

              //console.log(this.combined[word].weight)

            }
            this.run()
          })
        }
      },
      compute() {
        for (let root in this.set.roots) {
          let def = this.set.roots[root]
          let rootData = {
            root: root,
            def: def,
            weight: 5,
            type: 'root'
          }
          if (root != '') {
            this.combined[root] = rootData
          }

        }
        for (let word in this.set.words) {
          let def = this.set.words[word].definition
          let roots = this.set.words[word].roots
          let wordData = {
            word: word,
            roots: roots,
            def: def,
            weight: 0,
            type: 'word'
          }
          this.combined[word] = wordData
        }
      }
    }
  }
</script>

