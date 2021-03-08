<template>
  <body>
    <tweeter-header></tweeter-header>
    <main>
      <article id="profile">
        <dl id="user-data">
          <dt>Username:</dt>
          <dd>{{ user["username"] }}</dd>

          <dt>Email:</dt>
          <dd>{{ user["email"] }}</dd>

          <dt>Bio:</dt>
          <dd>{{ user["bio"] }}</dd>

          <dt>Birthdate:</dt>
          <dd>{{ user["birthdate"] }}</dd>
        </dl>

        <section id="buttons">
          <router-link to="/">
            <button type="submit" id="back-button">
              <span id="back-icon">
                <font-awesome-icon icon="undo" />
              </span>

              <span id="back-button__text">Go Back</span>
            </button>
          </router-link>
        </section>
      </article>
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

  computed: {
    userId() {
      return this.$route.params.userId;
    },
  },

  mounted() {
    this.refreshUser();
  },

  methods: {
    refreshUser() {
      this.$store.dispatch("getUser", this.userId).then((response) => {
        if (response.status === 200) {
          this.user = response.data[0];
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
@mixin formReset() {
  legend {
    padding: 0 0.5rem;
  }
  input {
    font-size: 16px;
    font-size: calc(max(16px, 1em));
    font-family: inherit;
    padding: 0.25em 0.5em;
    background-color: #fff;
    border: 1px solid black;
    border-radius: 5px;
    width: 100%;

    &:not(textarea) {
      line-height: 1;
      height: 2.25rem;
    }
  }
}

dt {
  float: left;
  clear: left;
  width: 6em;
  font-weight: bold;
}
dd {
  float: right;
}

main {
  display: grid;
  place-items: center;
  min-height: 100vh;
  background: url("https://source.unsplash.com/random");
  background-size: cover;
  #profile {
    display: grid;
    grid-template-rows: auto auto;
    gap: 1rem;
    padding: 1rem;
    border-radius: 10px;
    background-color: white;
    font-size: x-large;

    #user-data {
      grid-row: 1;
    }

    #buttons {
      grid-row: 2;
      display: flex;
      justify-content: center;
      gap: 1rem;
      #edit-button,
      #back-button {
        grid-row: 3;
        @include resetButton;
        border: 1px solid black;
        background-color: black;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        place-self: center;
        padding: 1rem 1.5rem;
        &:hover {
          background-color: white;
          color: black;
        }
        &.disabled {
          background-color: gray;
          color: black;
          cursor: not-allowed;
        }
        #back-button__text {
          padding-left: 1rem;
        }
      }
    }
  }
}
</style>
