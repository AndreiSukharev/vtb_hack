<template>
  <header>
    <p>Header</p>
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
  border-bottom: 6px solid var(--secondary);
  text-align: left;
  padding: 0 16px;
}

header > * {
  margin: 16px 10px 10px;
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
