import axios from 'axios';

const Client = {};
Client.install = function (Vue, options) {
  Vue.prototype.$apiClient = {
    createRequest(url, method = 'GET', data={}) {
      const config = {
        withCredentials: true,
        headers: {
         'Content-type': 'application/json'
        }
      };
      config.url = `http://localhost:4440${url}`;
      if (method === 'POST' || method === 'PUT'){
        data = JSON.stringify(data);
        config.data = data;
      }
      config.method = method;
      return axios.request(config);
    },
    login(login, password) {
      return this.createRequest('/api/signin', 'POST',{login: login, password: password});
    },
    logout(userId) {
      return this.createRequest(`/api/logout/${userId}`, 'DELETE');
    },
    getUser(userId) {
      return this.createRequest(`/api/users/${userId}`);
    },
    getChat(chatId) {
      return this.createRequest(`/api/chats/${chatId}`);
    },
    getDocuments() {
      return this.createRequest('/api/docs');
    },
    getDocument(documentId) {
      return this.createRequest(`/api/docs/${documentId}`);
    }
  }
}

export default Client;
