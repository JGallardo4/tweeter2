<template>
  <article id="comments">
    <comment-editor :isEdit="false" :tweetId="tweetId"></comment-editor>
    <section id="comments-list">
      <tweet-comment
        v-for="(comment, id) in comments"
        :key="id"
        :comment="comment"
      ></tweet-comment>
    </section>
  </article>
</template>

<script>
import TweetComment from './TweetComment.vue';
import CommentEditor from './CommentEditor.vue';

export default {
  name: 'tweeter-comments',

  props: {
    tweetId: {
      type: Number,
    },
  },

  data() {
    return {
      comments: [],
    };
  },

  components: {
    TweetComment,
    CommentEditor,
  },

  mounted() {
    this.refreshComments();
  },

  methods: {
    refreshComments() {
      this.$axios
        .request({
          url: '/comments',
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'X-Api-Key': '1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD',
          },
          params: { tweetId: this.tweetId },
        })
        .then((response) => {
          if (response.status === 200) {
            this.comments = response.data;
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

@include formReset;

#comments {
  grid-column: 1 / 3;
}

#comments-list {
  .comment {
    padding: 0.5rem;
    border-top: dashed 1px black;
  }
}
</style>
