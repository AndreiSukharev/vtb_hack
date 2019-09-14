import Vue from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';
import VueSession from 'vue-session'
import Client from './client';

Vue.use(VueSession,{ persist: true })
Vue.use(Client);
Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app');

Vue.config.devtools = process.env.NODE_ENV !== 'production';
