<template>
  <header>
    <router-link to="/" id="logo">
      <div id="tweeter-icon">
        <font-awesome-icon icon="crow" />
      </div>
      <p id="site-title">Tweeter</p>
    </router-link>
    <section v-if="isLoggedIn" id="user-menu">
      <router-link to="/profile" id="user-link">
        <div id="user-icon"><font-awesome-icon icon="user" /></div>

        <p id="username">{{ userName }}</p>
      </router-link>
      <button id="logout-button" @click="logOut()">Logout</button>
    </section>
  </header>
</template>

<script>
export default {
  name: "tweeter-header",

  computed: {
    isLoggedIn() {
      return this.$store.getters.getLoginToken !== "";
    },
    userName() {
      return this.$store.getters.getUserName;
    },
  },

  methods: {
    logOut() {
      this.$store.dispatch("logOut");
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

@mixin resetLink() {
  color: inherit;
  text-decoration: none;
  &:hover {
    color: inherit;
    text-decoration: none;
  }

  &:active {
    color: inherit;
    text-decoration: none;
  }

  &:visited {
    color: inherit;
    text-decoration: none;
  }
}

header {
  display: flex;
  justify-content: space-between;

  #logo {
    @include resetLink();

    display: grid;
    align-items: center;
    padding: 1rem;

    #tweeter-icon {
      font-size: xx-large;
    }
  }
  #user-menu {
    display: flex;
    justify-content: right;
    padding: 1rem;
    gap: 1rem;
    #user-link {
      @include resetLink();
      display: flex;
      align-items: center;
      #user-icon {
        padding: 0.4rem;
      }
      #username {
        display: grid;
        place-items: center;
      }
    }
    #logout-button {
      @include resetButton;
      border: 1px solid black;
      background-color: black;
      color: white;
      font-weight: bold;
      border-radius: 10px;
      padding: 1rem;
      &:hover {
        background-color: white;
        color: black;
      }
    }
  }
}
</style>
