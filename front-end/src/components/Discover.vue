<template>
  <section id="discover">
    <tweet-grid :tweets="tweets"></tweet-grid>
  </section>
</template>

<script>
import TweetGrid from "./TweetGrid.vue";

export default {
  name: "discover",

  computed: {
    tweets() {
      return this.$store.getters.getAllTweets;
    },
  },

  methods: {
    refresh() {
      this.$store.dispatch("refreshTweets");
    },
  },

  components: {
    TweetGrid,
  },
};
</script>

<style lang="scss" scoped>
@mixin resetButton() {
  background: none;
  color: inherit;
  border: none;
  padding: 0;
  font: inherit;
  cursor: pointer;
  outline: inherit;
}

#discover {
  grid-template-rows: auto 1fr;
  #refresh-button {
    justify-self: right;
    @include resetButton;
    padding: 1rem;
    border-left: solid 1px black;
    border-bottom: solid 1px black;

    &:hover {
      background-color: lightgreen;
    }
  }
}
</style>
