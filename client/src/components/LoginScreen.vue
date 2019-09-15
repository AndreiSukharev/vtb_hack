<template>
  <form
    class="form"
    v-on:submit="postLogin"
  >
    <h1>Log in to see the Documents</h1>
    <label
      class="form__field"
    >
      <span class="label">login</span>
      <input
        type="text"
        v-model="login"
      />
    </label>
    <label
      class="form__field"
    >
      <span class="label">Password</span>
      <input
        type="password"
        v-model="password"
      />
    </label>
    <label class="form__button">
      <span>Log in</span>
      <input type="submit" name="submit"/>
    </label>
  </form>
</template>

<script>
    import { mapGetters } from 'vuex';
    export default {
        name: "LoginScreen",
        computed: {
            login: {
                get() {
                    return this.getLogin;
                },
                set(value) {
                    this.$store.commit('setLogin', value)
                }
            },
            password: {
                get() {
                    return this.getPassword;
                },
                set(value) {
                    this.$store.commit('setPassword', value)
                }
            },
            ...mapGetters(['getLogin', 'getPassword'])
        },
        methods: {
            postLogin (event) {
                event.preventDefault();
                console.log(this.$session);
                this.$apiClient.login(this.getLogin, this.getPassword)
                    .then(function (response) {
                        console.log(response);
                        if (response.data.id !== undefined) {
                            this.$session.start();
                            this.$session.set('login', this.getLogin);
                            this.$session.set('userId', response.data.id);
                            this.$store.commit('setLogin', this.$session.get('login'));
                            this.$store.commit('setUserId', this.$session.get('userId'));
                            this.$router.push('/');
                        } else {
                            this.$toasted.error('Wrong credentials');
                        }
                    }.bind(this)).catch(err => {
                      console.log('err', err)
                    });
            }
        }
    }
</script>

<style scoped>
  .form__field {
    flex: 1 0 90%;
  }

  .form {
    display: flex;
    flex-direction: column;
    padding: 0 16px;
  }

  .form > div {
    display: flex;
    flex-wrap: wrap;
  }

  .form > * {
    margin-bottom: 32px;
  }
  .form__field {
    border-color: var(--inactive-border);
    color: var(--inactive);
    border: 2px solid;
    border-radius: 2px;
    margin: 10px 10px 16px;
    position: relative;
    box-shadow: none;
    transition-duration: 0.1s;
  }

  .form__field:focus,
  .form__field:focus-within {
    border-color: var(--black);
    color: var(--black);
    box-shadow: none;
  }

  .form__field > span.label {
    position: absolute;
    font-size: 0.8rem;
    top: -0.7em;
    left: 12px;
    background-color: #fff;
    color: var(--black);
    padding: 0 0.3rem;
    font-weight: 500;
  }

  .form__field input,
  .form__field > input:focus,
  .form__field > input:focus-within {
    color: inherit;
    border: none;
    outline: none;
    box-shadow: none;
    padding: 10px;
    width: 100%;
    height: auto;
    font-size: 1.2rem;
  }

  .form__button input {
    display: none;
  }

  .form__button {
    border-radius: 4px;
    background-color: var(--primary);
    min-height: 60px;
    display: flex;
    justify-items: center;
    align-items: center;
    margin: 0 10px 10px;
    transition-duration: 0.1s;
  }

  .form__button:hover:not(.disabled),
  .form__button:active:not(.disabled) {
    background-color: var(--button-hover);
    cursor: pointer;
  }

  .form__button:active:not(.disabled) {
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.16);
  }

  .form__button.disabled {
    background-color: var(--button-disabled);
  }

  .form__button > span {
    color: #fff;
    font-size: 1.2rem;
    line-height: 1.6rem;
    font-weight: 500;
    margin: auto;
  }
</style>
