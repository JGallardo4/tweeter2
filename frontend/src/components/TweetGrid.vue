<template>
  <section class="tweet-grid">
    <tweet v-for="(tweet, id) in tweets" :key="id" class="tweet" :tweet="tweet">
    </tweet>
  </section>
</template>

<script>
import Tweet from './Tweet.vue';

export default {
  name: 'tweet-grid',
  props: {
    tweets: {
      type: Array,
    },
  },
  components: {
    Tweet,
  },
};
</script>

<style lang="scss" scoped>
.tweet-grid {
  padding: 1rem;
  place-self: stretch;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
  gap: 2rem;
  place-items: stretch;

  .tweet {
    border: solid 1px black;
  }
}

@media screen and (max-width: 500px) {
  .tweet-grid {
    padding: 2px;
    gap: 2px;
    grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
  }
}
</style>
