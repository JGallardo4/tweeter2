<template>
  <section id="my-tweets">
    <tweet-grid :tweets="likedTweets"></tweet-grid>
  </section>
</template>

<script>
import TweetGrid from "./TweetGrid.vue";
import { mapState } from "vuex";

export default {
  name: "my-liked-tweets",

  computed: mapState(["likedTweets"]),

  created() {
    this.$store.dispatch("loadLikedTweets");
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
