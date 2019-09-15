<template>
  <div class="app" ref="container">
    <landing-header></landing-header>
    <router-view></router-view>
    <landing-footer></landing-footer>
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
      console.log(this.$session.exists());
      if (!this.$session.exists()) {
          this.$router.push('/login');
      }
  },
  sockets: {
    connect: function () {
      console.log('socket connected');
    },
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
  --primary: #0A2896;
  --secondary: #9d397e;
  --button-hover: #091e6f;
  --header-background: #0A2896;
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
