<template>
  <body>
    <tweeter-header></tweeter-header>
    <main>
      <p>User profile</p>
    </main>
  </body>
</template>

<script>
import TweeterHeader from "../components/TweeterHeader.vue";

export default {
  name: "UserProfile",

  components: {
    TweeterHeader,
  },

  data() {
    return {
      user: {
        type: Object,
      },
    };
  },

  props: {
    userId: {
      type: Number,
    },
  },

  mounted() {
    this.refreshUser();
    console.log(this.user);
  },

  methods: {
    refreshUser() {
      this.$store.dispatch("getUsers", this.userId).then((response) => {
        if (response.status === 200) {
          this.user = response.data;
        }
      });
    },
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
</style>
