<template>
  <article class="comment">
    <p v-if="!isEdit" id="comment-content">{{ comment.content }}</p>
    <comment-editor
      v-if="isEdit"
      :isEdit="true"
      :comment="comment"
      :tweetId="comment.tweetId"
    ></comment-editor>

    <section id="comment-info">
      <!-- Edit -->
      <section v-if="isEdit" id="edit-comment">
        <p>hello world</p>
      </section>

      <!-- Delete -->
      <button
        v-if="userId == comment.userId"
        @click="deleteComment()"
        id="delete-button"
      >
        <div id="delete-icon"><font-awesome-icon icon="times" /></div></button
      ><button
        v-if="userId == comment.userId"
        @click.prevent="() => (isEdit = !isEdit)"
        id="edit-button"
        title="Edit this Comment"
      >
        <div id="edit-icon">
          <font-awesome-icon icon="pen" />
        </div>
      </button>

      <p id="comment-author">{{ comment.username }}</p>
      <p id="comment-date">{{ comment.createdAt }}</p>
    </section>
  </article>
</template>

<script>
import CommentEditor from './CommentEditor.vue';

export default {
  components: { CommentEditor },

  name: 'tweet-comment',

  data() {
    return {
      isEdit: false,
    };
  },

  computed: {
    userId() {
      return this.$store.getters.getUserId;
    },
  },

  props: {
    comment: {
      type: Object,
    },
  },

  methods: {
    deleteComment() {
      this.$axios
        .request({
          url: '/comments',
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
            'X-Api-Key': '1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD',
          },
          data: {
            loginToken: this.$store.getters.getLoginToken,
            commentId: this.comment.commentId,
          },
        })
        .then((response) => {
          if (response.status === 204) {
            this.$router.go(0);
          }
        })
        .catch((error) => {
          console.log(error);
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

.comment {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr auto;
  height: min-content;

  #tweet-content {
    grid-column: 1 / 3;
    grid-row: 2;
    padding: 1rem;
    place-self: center;
  }

  #comment-info {
    grid-row: 2;
    display: flex;
    justify-content: right;
    align-items: center;
    gap: 1rem;
    padding: 1rem;

    #edit-button {
      @include resetButton;
    }

    #delete-button {
      @include resetButton;
      &:hover {
        color: rgb(214, 76, 99);
      }
    }
  }
}
</style>
