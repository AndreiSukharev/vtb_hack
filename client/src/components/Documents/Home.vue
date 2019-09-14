<template>
  <div class="wrapper">
    <div class="container">
        <document v-for="document in this.getDocuments"
          v-bind:name="document.doc_name"
          v-bind:documentId="document.doc_id"
          v-bind:members="document.members"
        >
        </document>
    </div>
    <div v-show="this.showImg">
      <img src="assets/calendar.png" alt="">
    </div>
  </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import Document from "./Document.vue";
    export default {
        name: "Home",
        components: {Document},
        beforeMount() {
            this.$apiClient.getDocuments()
                .then(function(response) {
                    this.$store.commit('setDocuments', response.data);
                    console.log(response);
                }.bind(this))
                .catch(error => {
                   console.log(error)
                });
        },
        computed: {
            showImg() {
              return screen.width > 1000;
            },
            ...mapGetters(['getDocuments'])
        }
    }
</script>

<style scoped>
  .wrapper {
    text-align: center;
    display: flex;
    flex-direction: row;
    width: 100%;
    max-width: 1200px;
  }

  .container {
    display: flex;
    flex-direction: column;
  }

  .container__document {
    margin: 16px 32px;
    padding: 15px;
  }

  .container__document:first-child {
    margin-top: 0;
  }

  .wrapper div:nth-child(2) {
    margin-left: 32px;
  }
</style>
