<template>
  <div class="wrapper">
    <article class="container votes">
      <h1>I'm here</h1>
    </article>
    <div class="container sidebar">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
    export default {
        name: "DocumentScreen"
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
    flex: 0 0 70%;
  }

  .sidebar {
    /*flex: 0 1 30%;*/
  }
</style>
