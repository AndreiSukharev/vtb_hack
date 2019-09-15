<template>
  <article class="container">
    <vote-text :vote-id="$route.params.voteId"></vote-text>
    <vote-chat></vote-chat>
  </article>
</template>

<script>
    import VoteText from "../Vote/VoteText.vue";
    import VoteChat from "../Vote/VoteChat.vue";
    export default {
        name: "DocumentScreenSideBar",
        components: {VoteChat, VoteText}
    }
</script>

<style scoped>
  .container{
    display: flex;
    flex-direction: column;
    border: 2px solid var(--primary);
    border-radius: 5px;
    flex: 1 0 100%;
    align-self: stretch;
  }
</style>
