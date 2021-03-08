<template>
  <body>
    <tweeter-header></tweeter-header>
    <main>
      <div id="delete">
        <form action="" id="delete__form">
          <fieldset id="delete__fieldset">
            <legend>Delete Account</legend>

            <p id="password-input">
              <label for="password">Password</label>
              <input
                type="password"
                name="password"
                v-model="password"
                placeholder=""
              />
            </p>

            <section id="buttons">
              <router-link to="/profile">
                <button type="submit" id="back-button">
                  <span id="back-icon">
                    <font-awesome-icon icon="undo" />
                  </span>

                  <span id="back-button__text">Go Back</span>
                </button>
              </router-link>

              <button @click.prevent="deleteAccount()" id="submit-delete">
                Delete Account
              </button>
            </section>

            <p id="error-message" v-if="error">
              Incorrect password.
            </p>
          </fieldset>
        </form>
      </div>
    </main>
  </body>
</template>

<script>
import TweeterHeader from "../components/TweeterHeader.vue";

export default {
  components: { TweeterHeader },
  name: "DeleteAccount",

  data() {
    return {
      password: "",

      error: false,
    };
  },

  watch: {
    password: function() {
      if (this.password != "") {
        this.error = false;
      }
    },
  },

  methods: {
    deleteAccount() {
      this.$store
        .dispatch("deleteAccount", {
          loginToken: this.$store.getters.getLoginToken,
          password: this.password,
        })
        .catch((response) => {
          if (response.status === 400) {
            this.password = "";
            this.error = true;
          } else {
            console.log(response);
          }
        });
    },
  },
};
</script>

<style lang="scss" scoped>
$tablet-min: 769px;
$desktop-min: 1024px;
$widescreen-min: 1216px;
$fullhd-min: 1216px;

@mixin mobile-layout {
}

@mixin desktop-layout {
  width: 40vw;
  input {
    place-self: stretch;
  }
}

@media screen and (min-width: $desktop-min) {
  #register__form {
    @include desktop-layout;
  }
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

@mixin resetButton() {
  background: none;
  color: inherit;
  border: none;
  padding: 0;
  font: inherit;
  cursor: pointer;
  outline: inherit;
}
@include formReset;

#delete {
  display: grid;
  place-items: center;
  min-height: 100vh;
  background: url("https://source.unsplash.com/random");
  background-size: cover;
  #delete__form {
    padding: 0.5rem;
    border-radius: 10px;
    background-color: white;

    #delete__fieldset {
      padding: 1rem;
      display: grid;
      grid-template-columns: 1fr;
      grid-template-rows: 1fr 1fr;
      gap: 1rem;
      border-radius: 10px;
      border-style: solid;
      border-width: 1px;
      border-color: black;

      fieldset {
        border: 0;
        display: grid;
      }

      input {
        padding: 1rem;
      }

      #buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
      }

      #submit-delete,
      #back-button {
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
      }

      #back-button__text {
        padding-left: 1rem;
      }

      #error-message {
        color: darkred;
      }
    }
  }
}
</style>
