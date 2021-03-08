<template>
  <section id="discover">
    <section id="tabs-container">
      <div id="tabs">
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="['tab-button', { active: currentTab === tab }]"
          v-on:click="currentTab = tab"
        >
          {{ tab }}
        </button>
      </div>

      <component :is="currentTabComponent" class="tab"></component>
    </section>
  </section>
</template>

<script>
import MyTweets from './MyTweets.vue';
import FromUsersIFollow from './FromUsersIFollow.vue';
import MyLikedTweets from './MyLikedTweets.vue';

export default {
  name: 'my-stream',

  data() {
    return {
      currentTab: 'From Users I Follow',
      tabs: ['From Users I Follow', 'My Liked Tweets', 'My Tweets'],
    };
  },

  computed: {
    currentTabComponent() {
      return this.currentTab
        .toLowerCase()
        .split(' ')
        .join('-');
    },
  },

  methods: {
    refresh() {
      this.$store.dispatch('refreshTweets');
    },
  },

  components: {
    FromUsersIFollow,
    MyTweets,
    MyLikedTweets,
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
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: auto 1fr;
  gap: 1rem;
}

#tabs-container {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: auto 1fr;

  #tabs {
    grid-row: 1;
    display: flex;
    justify-content: right;
    border-bottom: solid 1px black;
    button {
      @include resetButton;
      padding: 1rem;
      border-left: solid 1px black;

      &:hover {
        background-color: gainsboro;
      }

      &.active {
        background-color: lightblue;
      }
    }
  }

  .tab {
    grid-row: 2;
    min-height: 50vh;
    display: grid;
  }
}
</style>
