import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const getters = {};
const debug = process.env.NODE_ENV !== 'production';

const state = {};

// mutations
const mutations = {};

export default new Vuex.Store({
  state: state,
  mutations: mutations,
  getters: getters,
  strict: !debug,
  devTools: debug
});
