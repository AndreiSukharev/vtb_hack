import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';
const state = {
  login: '',
  password: '',
  documents: []
};

// mutations
const mutations = {
  setLogin: (state, value) => {
    state.login = value;
  },
  setPassword: (state, value) => {
    state.password = value;
  },
  setDocuments: (state, value) => {
    state.documents = value;
  }
};

const getters = {
  getLogin: state => state.login,
  getPassword: state => state.password,
  getDocuments: state => state.documents
};

export default new Vuex.Store({
  state: state,
  mutations: mutations,
  getters: getters,
  strict: !debug,
  devTools: debug
});
