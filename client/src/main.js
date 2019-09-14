import Vue from 'vue';
import App from './App.vue';
import store from './store';
import VueRouter from 'vue-router';
import Agreements from "./components/Agreements.vue";

Vue.config.productionTip = false;

// Initializing router

const routes = [
  { path: '/', component: Agreements },
];

Vue.use(VueRouter);

const router = new VueRouter({ mode: 'history', routes: routes, base: '/' });

new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app');

Vue.config.devtools = process.env.NODE_ENV !== 'production';
