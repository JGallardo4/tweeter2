<template>
  <section id="new-tweet">
    <form action="" id="tweet__form" @submit.prevent="postTweet()">
      <fieldset id="tweet__fieldset">
        <legend>New Tweet</legend>

        <p id="tweet-content">
          <textarea
            rows="5"
            cols="40"
            name="tweet-content"
            v-model="input"
          ></textarea>
        </p>

        <p id="character-count" :class="{ overLimit: isOverLimit }">
          {{ totalCharacters }} / {{ characterLimitInclusive }} characters
        </p>

        <button
          :disabled="isOverLimit"
          :class="{ disabled: isOverLimit }"
          type="submit"
          id="submit-tweet"
        >
          Post New Tweet
        </button>
      </fieldset>
    </form>
  </section>
</template>

<script>
export default {
  name: 'new-tweet',

  data() {
    return {
      input: '',
      characterLimitInclusive: 200,
    };
  },

  computed: {
    totalCharacters() {
      return this.input.length;
    },

    isOverLimit() {
      return this.input.length > this.characterLimitInclusive;
    },
  },

  methods: {
    postTweet() {
      this.$store.dispatch('postTweet', this.input);
      this.input = '';
    },
  },
};
</script>

<style lang="scss" scoped>
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

#new-tweet {
  display: grid;
  place-items: center;
  height: 80vh;
  background: url("https://source.unsplash.com/random");
  background-size: cover;
  #tweet__form {
    padding: 0.5rem;
    border-radius: 10px;
    background-color: white;

    #tweet__fieldset {
      padding: 1rem;
      display: grid;
      grid-template-columns: 1fr;
      grid-template-rows: 1fr auto;
      gap: 1rem;
      border-radius: 10px;
      border-style: solid;
      border-width: 1px;
      border-color: black;

      fieldset {
        border: 0;
        display: grid;
      }

      textarea {
        padding: 1rem;
        font-size: 15pt;
      }

      #character-count {
        justify-self: right;
        &.overLimit {
          color: red;
        }
      }

      #submit-tweet {
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
      }

      #error-message {
        color: darkred;
      }
    }
  }
}

@media screen and (max-width: 500px) {
  #new-tweet {
    #tweet__form {
      padding: 0;
      #tweet__fieldset {
        padding: 3px 0 3px 0;
        gap: 2px;
        textarea {
          padding: 2px;
          font-size: 13pt;
          width: 97vw;
          height: 16rem;
        }
      }
    }
  }
}
</style>
