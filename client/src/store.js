import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';
const state = {
  login: '',
  password: '',
  userId: 0,
  documents: [],
  votes: [],
  chats: [],
  fullTime: 400,
  timePassed: 0
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
  },
  setUserId: (state, value) => {
    state.userId = value;
  },
  setVote: (state, value) => {
    if (value.plus) {
      state.votes.filter(votes => votes.vote_id == value.voteId)[0].plus += 1;
    }
    if (value.minus) {
      state.votes.filter(votes => votes.vote_id == value.voteId)[0].minus += 1;
    }
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
  getUserId: state => state.userId
};

export default new Vuex.Store({
  state: state,
  mutations: mutations,
  getters: getters,
  strict: !debug,
  devTools: debug
});
