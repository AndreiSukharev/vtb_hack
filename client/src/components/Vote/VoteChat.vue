<template>
  <div>
    <div v-if="messages.length > 0">
      <div v-for="message in messages">
        {{message | filterMessage}}
      </div>
    </div>
    <h5 v-else>No message yet</h5>

    <div>
      <input type="text" v-model="dataToSend.text">
      <button @click="sendMessage">Send</button>
    </div>

  </div>
</template>

<script>
  import {mapGetters, mapState} from 'vuex';

  export default {
    name: "VoteChat",
    props: {
      chatid: ''
    },
    data() {
      return {
        messages: [],
        dataToSend: {
          text: '',
          chat_id: this.$route.params.id,
          author: '',
          creation_date: '',
          user_id: ''
        }
      }
    },
    watch: {
      chatid: function (val) {
        this.getChat()
        this.$socket.emit('join', val);
      }
    },
    // created () {
    //   this.getChat()
    //   this.$socket.emit('join', this.chatid);
    // },
    filters: {
      filterMessage: function (value) {
        let date = new Date(value.creation_date).toLocaleTimeString();
        let message = `${value.author} ${date}: ${value.text}`;
        return message
      }
    },
    methods: {
      ...mapGetters([
        'getLogin', 'getUserId', 'getUserId'
      ]),
      getChat() {
        this.$apiClient.getChat(this.chatid)
          .then(data => {
            // console.log(data.data);
            this.messages = data.data;
          })
      },
      sendMessage() {
        this.dataToSend.author = this.getLogin();
        this.dataToSend.creation_date = new Date();
        this.dataToSend.chat_id = this.chatid;
        this.dataToSend.user_id = this.getUserId();
        console.log(this.dataToSend)
        this.$socket.emit('message', this.dataToSend);
        this.dataToSend.text = '';
      },
    },
    sockets: {
      receive_message: function (message) {
        this.messages.push(message);
      }
    },
  }
</script>

<style scoped>

</style>
