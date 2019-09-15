<template>
  <div class="wrapper">
    <article class="container votes">
      <h1>{{ this.getTime | filterTime }}</h1>
      <vote-subject
        v-for="vote in this.getVotes"
        v-bind:document-id="vote.doc_id"
        v-bind:vote-id="vote.vote_id"
      >
      </vote-subject>
    </article>
    <div class="container sidebar">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
    import VoteSubject from "../Vote/VoteSubject.vue";

    export default {
        name: "DocumentScreen",
        components: {VoteSubject},
        props: ['documentId'],
        beforeMount() {
          this.$apiClient.getDocument(this.$route.params.documentId)
              .then(function (response) {
                  console.log(response)
                  this.$store.commit('setVotes', response.data.votes);
                  this.$store.commit('setChats', response.data.chats);
                  this.$store.commit('setTimePassed', response.data.time)
              }.bind(this)).catch(error => {
                  console.log(error);
          })
        },
        computed: {
            getVotes(){
                return this.$store.state.votes;
            },
            getTime(){
                return this.$store.state.timePassed;
            }
        },
        filters: {
            filterTime: function (value) {
                if (value == -1) return 'Vote hasn\'t started yet';
                return ((60*20 - value) / 60) > 0? `There is ${Math.floor((60*20 - value) / 60)} minutes left` : 'No time left';
            }
        }
    }
</script>

<style scoped>
  .wrapper {
    text-align: center;
    display: flex;
    flex-flow: row nowrap;
    width: 100%;
    max-width: 1200px;
    height: auto;
    min-height: 400px;
  }

  .container {
    display: flex;
    flex-direction: column;
  }

  .votes {
    flex: 0 0 40%;
    display: flex;
    flex-flow: column nowrap;
  }

  .sidebar {
    flex: 0 0 60%;
    align-items: center;
    justify-content: center;
  }

  h1 {
    margin-bottom: 16px;
  }

  @media screen and (max-width: 600px) {
    .votes > *{
      text-align: center;
    }

    .votes {
      flex: 0 0 25%;
    }

    .sidebar {
      flex: 0 0 75%;
    }
  }
</style>
