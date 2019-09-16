<template>
  <article class="container__document">
    <div class="container__document__logo">
      <img :src="src" alt="">
    </div>
    <div class="container__document__main">
      <h3>{{ name }}</h3>
      <hr>
      <p>Members: {{ members }}</p>
      <div class="votes-container">
        <div v-for="vote in votes">
          <p>Vote {{ vote.vote_id }}</p>
          <p>Accept: {{ vote.plus }}</p>
          <p>Reject: {{ vote.minus}}</p>
        </div>
      </div>
    </div>
    <div class="container__document__counter">
      <router-link :to="link">
        <img src="assets/arrow.png" alt="">
      </router-link>
      <button @click="activate" class="button">
        <span>Activate</span>
      </button>
      <button @click="finish" class="button">
        <span>Finish</span>
      </button>
      <a href="/assets/report.txt"  class="button" download>
        <span>Result</span>
      </a>
    </div>
  </article>
</template>

<script>
    export default {
        name: "Document",
        props: ['documentId', 'name', 'members'],
        data(){
            return {
                votes: []
            }
        },
        mounted(){
            this.$apiClient.getDocument(this.documentId)
                .then(function (response) {
                    this.votes = response.data.votes;
                }.bind(this));
        },
        computed: {
            link(){
                return `/document/${this.documentId}`;
            },
            linkToResult(){
                return `/result/${this.documentId}`
            },
            src(){
                return `/assets/${this.documentId}.png`
            }
        },
        methods: {
            activate(){
                this.$toasted.info('Please, wait. Emails are being sent');
                // this.$router.push('/waiting')
                this.$apiClient.activateDocument(this.documentId)
                    .then(function (response) {
                        console.log(response);
                      this.$router.push(this.link);
                    }.bind(this));
            },
            finish(){
                this.$toasted.success('The vote has concluded');
            },
            getVoteResults(){

            }
        }
    }
</script>

<style scoped>
  .container__document {
    display: flex;
    flex-flow: row nowrap;
    border: 2px solid var(--primary);
    height: auto;
    min-height: 64px;
    align-items: center;
  }

  .container__document__logo {
    flex: 0 0 15%
  }
  .container__document__main {
    flex: 0 0 70%;
    display: flex;
    flex-flow: column nowrap;

  }
  .container__document__counter {
    flex: 0 0 15%;
  }

  .container__document__main > *:not(:last-child) {
    margin-bottom: 16px;
  }

  .container__document__counter img {
    width: 100%;
  }

  .button {
    width: 100%;
    border-radius: 15px;
    min-height: 24px;
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-self: stretch;
    transition-duration: 0.1s;
    border: 2px solid var(--primary);
    background-color: var(--primary);
    color: #fff;
    margin-bottom: 5px;
  }

  .button:disabled {
    background-color: var(--primary);
    color: #fff;
  }

  .button:hover:not(.disabled),
  .button:active:not(.disabled) {
    background-color: var(--button-hover);
    cursor: pointer;
  }

  .button:active:not(.disabled) {
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.16);
  }

  .button.disabled {
    background-color: var(--button-disabled);
  }

  .button > span {
    font-size: 1.2rem;
    line-height: 1.6rem;
    font-weight: 500;
    margin: auto;
  }

  .votes-container {
    display: flex;
    text-align: left;
    justify-content: space-evenly;
  }

</style>
