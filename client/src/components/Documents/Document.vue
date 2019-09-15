<template>
  <article class="container__document">
    <div class="container__document__logo">
      <img src="assets/Ellipse.png" alt="">
    </div>
    <div class="container__document__main">
      <h3>{{ name }}</h3>
      <hr>
      <p>Members: {{ members }}</p>
    </div>
    <div class="container__document__counter">
      <router-link :to="link">
        <img src="assets/arrow.png" alt="">
      </router-link>
      <button class="button">
        <span>Reject</span>
        <span>{{ this.getVoteById(voteId).minus }}</span>
      </button>
    </div>
  </article>
</template>

<script>
    export default {
        name: "Document",
        props: ['documentId', 'name', 'members'],
        computed: {
            link(){
                return `/document/${this.documentId}`;
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
</style>
