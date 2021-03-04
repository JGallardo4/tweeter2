<template>
  <section id="my-tweets">
    <tweet-grid :tweets="tweets"></tweet-grid>
  </section>
</template>

<script>
import TweetGrid from "./TweetGrid.vue";

export default {
  name: "from-users-i-follow",

  computed: {
    tweets() {
      return this.$store.getters.getAllTweets.filter((tweet) =>
        this.$store.getters.getFollows.includes(tweet.userId)
      );
    },
  },

  mounted() {
    this.$store.dispatch("refreshTweets");
    this.$store.dispatch("refreshFollows");
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

#my-tweets {
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
