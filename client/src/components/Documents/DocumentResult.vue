<template>
    <article class="container votes">
      <h1>The vote for document {{ this.$route.params.documentId }} has ended</h1>
      <vote-result
        v-for="vote in this.getVotes"
        v-bind:document-id="vote.doc_id"
        v-bind:vote-id="vote.vote_id"
      >
      </vote-result>
    </article>
</template>

<script>
    import VoteResult from "../Vote/VoteResult.vue";

    export default {
        name: "DocumentResult",
        components: {VoteResult},
        computed: {
            getVotes(){
                return this.$store.state.votes;
            },
            getTime(){
                return this.$store.state.timePassed;
            }
        },
        mounted() {
            this.$apiClient.getDocument(this.$route.params.documentId)
                .then(function (response) {
                    console.log(response)
                    this.$store.commit('setVotes', response.data.votes);
                    this.$store.commit('setChats', response.data.chats);
                    this.$store.commit('setTimePassed', response.data.time)
                }.bind(this)).catch(error => {
                console.log(error);
            })
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

  h1 {
    margin-bottom: 16px;
  }
</style>
