<template>
  <router-link :to="link" class="votes__subject">
    Опрос: {{ voteId }}
  </router-link>
</template>

<script>
    export default {
        name: "VoteSubject",
        props: ['documentId', 'voteId'],
        computed: {
            link(){
                return `/document/${this.documentId}/vote/${this.voteId}`
            }
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
