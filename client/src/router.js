import Vue from 'vue';
import VueRouter from 'vue-router'
import Home from "./components/Documents/Home.vue";
import LoginScreen from "./components/LoginScreen.vue";
import DocumentScreen from "./components/Documents/DocumentScreen.vue";
import Processing from "./components/Processing.vue";
import DocumentScreenSideBar from "./components/Documents/DocumentScreenSideBar.vue";
import Waiting from "./components/Waiting.vue";

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: LoginScreen},
  { path: '/waiting', components: Waiting},
  { path: '/document/:documentId', component: DocumentScreen, children: [
      {path: '', component: Processing},
      {path: 'vote/:voteId', component: DocumentScreenSideBar}
    ]}
];


const router = new VueRouter({ mode: 'history', routes: routes, base: '/' });

export default router;
