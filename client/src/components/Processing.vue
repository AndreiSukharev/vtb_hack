<template>
  <div>
    <h2>Choose the subject</h2>
<!--    <div>-->
<!--      <moon-loader-->
<!--        :loading="true"-->
<!--        color="#0A2896"-->
<!--        size="300"-->
<!--        class="spinner"-->
<!--      ></moon-loader>-->
<!--    </div>-->
  </div>
</template>

<script>
import MoonLoader from 'vue-spinner/src/MoonLoader.vue';
export default {
  name: 'Processing',
  components: {
    MoonLoader
  }
};
</script>

<style scoped>


</style>
