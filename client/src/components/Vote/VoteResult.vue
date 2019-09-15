<template>
  <article class="votes__subject">
    <h2>Vote № {{ voteId }}</h2>
    <div></div>
  </article>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        name: "VoteResult",
        props: ['documentId', 'voteId'],
        computed: {
            ...mapGetters(['getVoteById'])
        }
    }
</script>

<style scoped>
  .votes__subject {
    width: 90%;
    flex: 0 0 64px;
    padding: 16px;
    color: #fff;
    background-color: var(--primary);
    margin-bottom: 32px;
    border-radius: 5px;
    text-decoration: none;
    font-weight: 700;
    font-size: 2rem;
    text-align: left;
  }
</style>
