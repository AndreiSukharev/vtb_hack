<template>
  <div class="app" ref="container">
    <landing-header></landing-header>
    <router-view></router-view>
    <landing-footer bank="TCB"></landing-footer>
  </div>
</template>

<script>
import LandingHeader from './components/LandingHeader.vue';
import LandingFooter from './components/LandingFooter.vue';

export default {
  name: 'App',
  components: {
    LandingFooter,
    LandingHeader
  },
  mounted() {
    this.$root.$store.commit('setIsLoading', false);
  }
};
</script>

<style>
:root {
  font-size: 14px;
  --inactive-border: #dddfe0;
  --inactive: #d1d4d8;
  --black: #696969;
  --button-disabled: rgba(20, 154, 154, 0.6);
  --primary: #18b7b7;
  --secondary: #9d397e;
  --button-hover: #149a9a;
  --header-background: #282b33;
  --footer-background: #f6f7f9;
  --footer: #ccc;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  margin: 0;
  font-family: Roboto, Helvetica, Arial, sans-serif;
}

.app {
  color: #444;
  max-width: 600px;
  text-align: center;
  display: flex;
  align-items: center;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
}

.app > * {
  margin-bottom: 32px;
}

</style>
