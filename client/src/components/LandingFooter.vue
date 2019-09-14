<template>
  <footer>
    <p>vtb-hack</p>
  </footer>
</template>

<script>
export default {
  name: 'LandingFooter'
};
</script>

<style scoped>
footer {
  background-color: var(--footer-background);
  color: var(--footer);
  width: 100%;
  align-self: end;
  min-height: 132px;
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  margin: auto 0 0;
  border-top: 2px solid #dedfe1;
}

footer p {
  font-size: 1rem;
  line-height: 1.6rem;
  padding: 0 10px;
}
</style>
