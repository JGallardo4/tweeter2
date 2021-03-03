<template>
  <body>
    <tweeter-header></tweeter-header>
    <main>
      <div id="login">
        <form action="" id="login__form">
          <fieldset id="login__fieldset">
            <legend>Login</legend>

            <p id="email-input">
              <label for="email">Email</label>
              <input type="text" name="email" v-model="input.email" />
            </p>

            <p id="password-input">
              <label for="password">Password</label>
              <input type="password" name="password" v-model="input.password" />
            </p>

            <button @click.prevent="logIn()" id="submit-login">Log In</button>

            <p id="error-message" v-if="error">
              There was an error with your email and/or password.
            </p>
          </fieldset>

          <router-link to="/register">
            <p>Register</p>
          </router-link>
        </form>
      </div>
    </main>
  </body>
</template>

<script>
import TweeterHeader from "../components/TweeterHeader.vue";

export default {
  components: { TweeterHeader },
  name: "Login",

  data() {
    return {
      input: {
        email: "",
        password: "",
      },

      error: false,
    };
  },

  beforeCreate() {
    this.$store.dispatch("checkLogin");
  },

  watch: {
    "input.email": function() {
      this.error = false;
    },

    "input.password": function() {
      if (this.input.password != "") {
        this.error = false;
      }
    },
  },

  methods: {
    logIn() {
      this.$store
        .dispatch("logIn", this.input)
        .then(() => this.$store.dispatch("redirect", "/"))
        .catch((error) => {
          this.input.password = "";
          this.error = true;
          console.log(error);
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
  #login__form {
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

#login {
  display: grid;
  place-items: center;
  min-height: 100vh;
  background: url("https://source.unsplash.com/random");
  background-size: cover;
  #login__form {
    padding: 0.5rem;
    border-radius: 10px;
    background-color: white;

    #login__fieldset {
      padding: 1rem;
      display: grid;
      grid-template-columns: 1fr;
      grid-template-rows: 1fr 1fr 1fr;
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

      #email-input {
        grid-row: 1;
      }

      #password-input {
        grid-row: 2;
      }

      #submit-login {
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
      }

      #error-message {
        color: darkred;
      }
    }
  }
}
</style>
