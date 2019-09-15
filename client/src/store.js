import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';
const state = {
  login: '',
  password: '',
  documents: [],
  votes: [],
  chats: []
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
  },
  setVotes: (state, value) => {
    state.votes = value;
  },
  setChats: (state, value) => {
    state.chats = value;
  }
};

const getters = {
  getLogin: state => state.login,
  getPassword: state => state.password,
  getDocuments: state => state.documents,
  getVotes: state => state.votes,
  getVoteById: state => voteId => {
    return state.votes.filter(vote => vote.vote_id == voteId)[0];
  },
  getChats: state => state.chats,
  getChatById: state => chatId => {
    return state.chats.filter(chat => chat.chat_id == chatId)[0];
  },

};

export default new Vuex.Store({
  state: state,
  mutations: mutations,
  getters: getters,
  strict: !debug,
  devTools: debug
});
