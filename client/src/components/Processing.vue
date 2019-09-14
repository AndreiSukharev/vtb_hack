<template>
  <div>
    <moon-loader
      :loading="true"
      color="#0A2896"
      size="300"
      class="spinner"
    ></moon-loader>
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
