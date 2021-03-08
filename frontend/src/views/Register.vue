<template>
  <body>
    <tweeter-header></tweeter-header>
    <main>
      <div id="register">
        <form action="" id="register__form">
          <fieldset id="register__fieldset">
            <legend>{{ isEdit ? "Update Profile" : "Register" }}</legend>

            <p id="email-input">
              <label for="email">Email</label>
              <input
                type="text"
                name="email"
                v-model="input.email"
                placeholder=""
              />
            </p>

            <p id="username-input">
              <label for="username">Username</label>
              <input
                type="text"
                name="username"
                v-model="input.username"
                placeholder=""
              />
            </p>

            <p id="bio-input">
              <label for="bio">Bio</label>
              <input
                type="text"
                name="bio"
                v-model="input.bio"
                placeholder=""
              />
            </p>

            <p id="birthdate-input">
              <label for="birthdate">Birthdate</label>
              <datepicker
                v-model="rawBirthdate"
                name="birthdate"
                class="birthday-input-picker"
              ></datepicker>
            </p>

            <p id="password-input" v-if="!isEdit">
              <label for="password">Password</label>
              <input
                type="password"
                name="password"
                v-model="input.password"
                placeholder=""
              />
            </p>

            <section id="buttons">
              <router-link to="/profile" v-if="isEdit">
                <button type="submit" id="back-button">
                  <span id="back-icon">
                    <font-awesome-icon icon="undo" />
                  </span>

                  <span id="back-button__text">Go Back</span>
                </button>
              </router-link>

              <button
                @click.prevent="isEdit ? updateProfile() : register()"
                id="submit-register"
              >
                {{ isEdit ? "Update Profile" : "Register" }}
              </button>
            </section>

            <p id="error-message" v-if="error">
              There was an error with your email and/or password.
            </p>
          </fieldset>
          <router-link v-if="!isEdit" to="login">
            <p>Login</p>
          </router-link>
        </form>
      </div>
    </main>
  </body>
</template>

<script>
import Datepicker from "vuejs-datepicker";
import TweeterHeader from "../components/TweeterHeader.vue";

export default {
  components: { TweeterHeader, Datepicker },
  name: "register",

  props: {
    isEdit: {
      type: Boolean,
      default() {
        return false;
      },
    },
  },

  data() {
    return {
      input: {
        email: "",
        username: "",
        birthdate: "",
        bio: "",
        password: "",
      },

      rawBirthdate: new Date(),

      error: false,
    };
  },

  mounted() {
    if (this.isEdit) {
      this.$axios
        .request({
          url: "/users",
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD",
          },
          params: { userId: this.$store.getters.getUserId },
        })
        .then((response) => {
          if (response.status === 200) {
            this.input.email = response.data[0].email;
            this.input.username = response.data[0].username;
            this.input.bio = response.data[0].bio;
            this.input.birthdate = response.data[0].birthdate;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },

  computed: {
    formattedBirthdate() {
      const mydate = `${this.rawBirthdate.toLocaleDateString("en-US", {
        year: "numeric",
      })}-${this.rawBirthdate.toLocaleDateString("en-US", {
        month: "2-digit",
      })}-${this.rawBirthdate.toLocaleDateString("en-US", {
        day: "2-digit",
      })}`;
      return mydate;
    },
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

    rawBirthdate() {
      this.input.birthdate = this.formattedBirthdate;
    },
  },

  created() {
    this.input.birthdate = this.formattedBirthdate;
  },

  methods: {
    register() {
      this.$store.dispatch("register", this.input).catch((response) => {
        this.input.password = "";
        this.error = true;
        console.log(response.status);
      });
    },

    updateProfile() {
      this.$axios
        .request({
          url: "/users",
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD",
          },
          data: {
            loginToken: this.$store.getters.getLoginToken,
            email: this.input.email,
            username: this.input.username,
            birthdate: this.input.birthdate,
            bio: this.input.bio,
          },
        })
        .then(this.$store.dispatch("logOut"))
        .catch((error) => {
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

#register {
  display: grid;
  place-items: center;
  min-height: 100vh;
  background: url("https://source.unsplash.com/random");
  background-size: cover;
  #register__form {
    padding: 0.5rem;
    border-radius: 10px;
    background-color: white;

    #register__fieldset {
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

      #buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
      }

      #birthday-input-picker {
        cursor: pointer !important;
        width: 100% !important;
        & > *,
        .vdp-datepicker * {
          cursor: pointer !important;
          width: 100% !important;
        }
      }

      #submit-register,
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

      #error-message {
        color: darkred;
      }

      #back-button__text {
        padding-left: 1rem;
      }
    }
  }
}
</style>
