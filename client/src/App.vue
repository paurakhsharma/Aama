<template>
  <div id="app">
    <Aama />
  </div>
</template>

<script>
import Aama from "./components/Aama.vue";

export default {
  name: "app",
  components: {
    Aama
  }
};
</script>

<style>
* {
  padding-left: 0;
  padding-right: 0;
  overflow-x: hidden;
}
</style>
