<template>
  <div class="container">
    <h2>
      Опрос: {{ voteId }}
    </h2>
    <p>
      {{ this.getVoteById(voteId).vote_text }}
    </p>
    <form class="form">
      <label class="form__button">
        <span>Accept</span>
        <span>{{ this.getVoteById(voteId).plus }}</span>
        <input type="submit" ref="1" name="submit"/>
      </label>
      <label class="form__button">
        <span>Reject</span>
        <span>{{ this.getVoteById(voteId).minus }}</span>
        <input type="submit" ref="0" name="submit"/>
      </label>
    </form>
  </div>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        name: "VoteText",
        props: ['voteId'],
        computed: {
            ...mapGetters(['getVoteById'])
        }
    }
</script>

<style scoped>
  .container > * {
    margin-bottom: 16px;
  }

  .form {
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-end;
  }

  .form__button {
    flex: 0 0 25%;
    border-radius: 15px;
    min-height: 24px;
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-between;
    align-items: center;
    margin: 0 10px 10px;
    transition-duration: 0.1s;
    border: 2px solid var(--primary);
    color: var(--black);
  }

  .form__button:disabled {
    background-color: var(--primary);
    color: #fff;
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
    font-size: 1.2rem;
    line-height: 1.6rem;
    font-weight: 500;
    margin: auto;
  }

  .form__button input {
    display: none;
  }

</style>
