<template>
  <div class="container">
    <h2>
      Опрос: {{ voteId }}
    </h2>
    <p>
      {{ this.getVoteById(voteId).vote_text }}
    </p>
    <div class="form">
      <button @click="vote(true)" class="form__button" :disabled="plusDisabled">
        <span>Accept</span>
        <span>{{ this.getVoteById(voteId).plus }}</span>
      </button>
      <button @click="vote(false)" class="form__button" :disabled="minusDisabled">
        <span>Reject</span>
        <span>{{ this.getVoteById(voteId).minus }}</span>
      </button>
    </div>
  </div>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        name: "VoteText",
        props: ['voteId'],
        data(){
          return {
              plusDisabled: false,
              minusDisabled: false
          }
        },
        mounted(){
            this.plusDisabled = false;
            this.minusDisabled = false;
        },
        computed: {
            ...mapGetters(['getVoteById', 'getUserId'])
        },
        methods: {
            vote(plus){
                if (plus) {
                    this.$apiClient.vote(this.voteId, this.getUserId, 1)
                        .then(function (response) {
                            console.log(response)
                            // this.$store.commit('vote', {plus: true, voteId: this.voteId});
                            this.plusDisabled = true;
                            this.minusDisabled = false;
                        }.bind(this))
                        .then(() => {
                            this.$apiClient.getDocument(this.$route.params.documentId)
                                .then(function (response) {
                                    console.log(response)
                                    this.$store.commit('setVotes', response.data.votes);
                                    this.$store.commit('setChats', response.data.chats);
                                }.bind(this)).catch(error => {
                                console.log(error);
                            })
                        })
                } else {
                    this.$apiClient.vote(this.voteId, this.getUserId, -1)
                        .then(function (response) {
                            console.log(response)
                            // this.$store.commit('vote', {plus: false, voteId: this.voteId});
                            this.plusDisabled = false;
                            this.minusDisabled = true;
                        }.bind(this))
                        .then(() => {
                            this.$apiClient.getDocument(this.$route.params.documentId)
                                .then(function (response) {
                                    console.log(response)
                                    this.$store.commit('setVotes', response.data.votes);
                                    this.$store.commit('setChats', response.data.chats);
                                }.bind(this)).catch(error => {
                                console.log(error);
                            })
                        })
                }

            }
        }
    }
</script>

<style scoped>
  .container {
    padding: 16px;
  }

  .container > * {
    margin-bottom: 16px;
  }

  .container > p {
    text-align: left;
    font-size: 1.4rem;
  }

  .form {
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-end;
  }

  .form__button {
    flex: 0 0 25%;
    border-radius: 15px;
    min-height: 32px;
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-between;
    align-items: center;
    margin: 0 10px 10px;
    transition-duration: 0.1s;
    border: 2px solid var(--primary);
    color: #000;
    background-color: #fff;
  }

  .form__button:disabled {
    background-color: var(--primary);
    color: #fff;
  }

  .form__button:hover:not(.disabled),
  .form__button:active:not(.disabled) {
    background-color: var(--button-hover);
    color: #fff;
    cursor: pointer;
  }

  .form__button:active:not(.disabled) {
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.16);
  }

  .form__button.disabled {
    background-color: var(--button-disabled);
  }

  .form__button > span {
    font-size: 1.2rem;
    line-height: 1.6rem;
    font-weight: 500;
    margin: auto;
  }

  .form__button input {
    display: none;
  }
</style>
