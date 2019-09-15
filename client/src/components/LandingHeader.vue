<template>
  <header>
    <router-link to="/"><h2>Home</h2></router-link>
<!--    <router-link>Chat</router-link>-->
<!--    <router-link>Huyat</router-link>-->
  </header>
</template>

<script>

export default {
  name: 'LandingHeader'
};
</script>

<style scoped>
header {
  background-color: var(--header-background);
  color: #fff;
  width: 100%;
  align-self: start;
  min-height: 96px;
  display: flex;
  align-content: space-between;
  justify-content: space-between;
  text-align: left;
  padding: 0 16px;
}

header > * {
  margin: 16px 10px 10px;
  color: #fff;
  text-decoration: none;
}

h3 {
  font-size: 1.2rem;
  font-weight: 400;
}

h2 {
  margin-top: 10px;
  font-size: 1.8rem;
  font-weight: 900;
}
</style>
