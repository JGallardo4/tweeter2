<template>
  <section id="post-comment">
    <form
      id="post-comment__form"
      action=""
      @submit.prevent="isEdit ? updateComment() : postComment()"
    >
      <fieldset id="post-comment__fieldset">
        <legend>New Comment</legend>

        <p id="comment-content">
          <textarea
            rows="4"
            cols="30"
            name="tweet-content"
            v-model="input"
          ></textarea>
        </p>

        <p id="character-count" :class="{ overLimit: isOverLimit }">
          {{ totalCharacters }} / {{ characterLimitInclusive }} characters
        </p>
        <section id="buttons">
          <button
            v-if="isEdit"
            type="submit"
            id="cancel-edit"
            @click="cancelEdit()"
          >
            <span id="cancel-icon">
              <font-awesome-icon icon="undo" />
            </span>

            <span id="cancel-edit__text">Cancel</span>
          </button>

          <button
            :disabled="isOverLimit"
            :class="{ disabled: isOverLimit }"
            type="submit"
            id="submit-comment"
          >
            {{ isEdit ? "Update Comment" : "Post New Comment" }}
          </button>
        </section>
      </fieldset>
    </form>
  </section>
</template>

<script>
export default {
  name: 'comment-editor',
  props: {
    isEdit: {
      type: Boolean,
      default() {
        return false;
      },
    },
    comment: {
      type: Object,
    },
    tweetId: {
      type: Number,
    },
  },
  mounted() {
    if (this.isEdit) {
      this.input = this.comment.content;
    }
  },

  data() {
    return {
      input: '',
      characterLimitInclusive: 150,
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
    postComment() {
      this.$axios
        .request({
          url: '/comments',
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-Api-Key': '1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD',
          },
          data: {
            loginToken: this.$store.getters.getLoginToken,
            tweetId: this.tweetId,
            content: this.input,
          },
        })
        .then((response) => {
          if (response.status == 201) {
            this.$router.go(0);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    updateComment() {
      this.$axios
        .request({
          url: '/comments',
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json',
            'X-Api-Key': '1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD',
          },
          data: {
            loginToken: this.$store.getters.getLoginToken,
            commentId: this.comment.commentId,
            content: this.input,
          },
        })
        .then((response) => {
          if (response.status === 200) {
            this.$router.go(0);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    cancelEdit() {
      this.$router.go(0);
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

#post-comment {
  padding: 0.5rem;
  #post-comment__fieldset {
    padding: 0.5rem;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr auto;
    gap: 1rem;

    #comment-content {
      textarea {
        width: 100%;
        max-width: 100%;
        padding: 1rem;
        font-size: 15pt;
      }
    }

    #character-count {
      justify-self: right;
      &.overLimit {
        color: red;
      }
    }
    #buttons {
      place-self: center;
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      #submit-comment,
      #cancel-edit {
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
      #cancel-edit {
        #cancel-edit__text {
          padding-left: 0.5rem;
        }
      }
    }
  }
}
</style>
