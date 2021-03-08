<template>
  <router-view />
</template>

<script>
export default {
  created() {
    this.$store.dispatch("checkLogin");
    this.$store.dispatch("initializeStore");
  },
};
</script>

<style lang="scss">
@mixin reset() {
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    &::before,
    &::after {
      box-sizing: border-box;
    }
  }
}

@include reset;
</style>
