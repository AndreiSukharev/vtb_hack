<template>
  <div>
    <div class="messages" v-if="messages.length > 0">
      <div v-for="message in messages" :class="message.author == getLogin ? 'author': ''">
        {{message | filterMessage}}
      </div>
    </div>
    <h5 v-else>No message yet</h5>

    <div>
      <input type="text" v-model="dataToSend.text">
      <button class="form__button" @click="sendMessage"><span>Send</span></button>
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
      computed: {
        getClass(userId) {
            return userId == this.getUserId ? 'author' : '';
        },
          ...mapGetters([
              'getLogin', 'getUserId', 'getUserId'
          ]),
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
        let message = `${value.author} ${date} : ${value.text}`;
        return message
      }
    },
    methods: {
      getChat() {
        this.$apiClient.getChat(this.chatid)
          .then(data => {
            // console.log(data.data);
            this.messages = data.data;
          })
      },
      sendMessage() {
        this.dataToSend.author = this.getLogin;
        this.dataToSend.creation_date = new Date();
        this.dataToSend.chat_id = this.chatid;
        this.dataToSend.user_id = this.getUserId;
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
  .messages{
    display: flex;
    flex-flow: column nowrap;
  }

  .messages > * {
    align-self: flex-start;
    background-color: var(--secondary);
    color: #fff;
    padding: 15px;
    font-size: 1.2rem;
    font-weight: 500;
    border-radius: 5px;
    margin-bottom: 5px;
  }

  .author {
    align-self: flex-end;
    background-color: var(--primary);
  }

    .form {
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-end;
  }

    input{
      height: 32px;
    }

  .form__button {
    flex: 0 0 20%;
    height: 32px;
    width: 120px;
    align-items: center;
    margin: 0 10px 10px;
    transition-duration: 0.1s;
    border: 2px solid var(--primary);
    color: #fff;
    background-color: var(--primary);
  }

  .form__button:disabled {
    background-color: var(--primary);
    color: #fff;
  }

  .form__button:hover:not(.disabled),
  .form__button:active:not(.disabled) {
    background-color: var(--button-hover);
    color: #fff;
    cursor: pointer;
  }

  .form__button:active:not(.disabled) {
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.16);
  }

  .form__button.disabled {
    background-color: var(--button-disabled);
  }

  .form__button > span {
    font-size: 1.2rem;
    line-height: 1.6rem;
    font-weight: 500;
    margin: auto;
  }

  .form__button input {
    display: none;
  }
</style>
