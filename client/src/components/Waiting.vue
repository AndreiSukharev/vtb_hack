<template>
          <moon-loader
            :loading="true"
            color="#0A2896"
            size="300"
            class="spinner"
          ></moon-loader>
</template>

<script>
    import MoonLoader from 'vue-spinner/src/MoonLoader.vue';
    export default {
        name: 'Waiting',
        components: {
            MoonLoader
        }
    };
</script>

<style scoped>


</style>
