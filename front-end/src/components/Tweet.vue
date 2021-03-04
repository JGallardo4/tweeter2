<template>
  <article class="tweet">
    <button
      v-if="userId == tweet.userId"
      @click="deleteTweet()"
      id="delete-button"
    >
      <div id="delete-icon"><font-awesome-icon icon="times" /></div>
    </button>

    <p id="tweet-content">{{ tweet.content }}</p>

    <section id="tweet-info">
      <form @submit.prevent="editTweet()" v-if="userId == tweet.userId">
        <router-link
          :to="{
            name: 'Edit',
            params: { tweetId: this.tweet.tweetId },
          }"
        >
          <button type="submit" id="edit-button" title="Edit this Tweet">
            <div id="edit-icon">
              <font-awesome-icon icon="pen" />
            </div>
          </button>
        </router-link>
      </form>

      <form @submit.prevent="toggleFollow()" v-if="tweet.userId != userId">
        <button
          type="submit"
          id="follow-button"
          :title="isFollowed ? 'Unfollow this user' : 'Follow this user'"
          @mouseover="isHoverFollow = true"
          @mouseleave="isHoverFollow = false"
        >
          <div id="follow-icon">
            <font-awesome-icon
              :icon="
                isFollowed
                  ? isHoverFollow
                    ? 'user-times'
                    : 'user-check'
                  : 'user-plus'
              "
              :class="['follow-icon', { followed: isFollowed }]"
            />
          </div>
        </button>
      </form>

      <form @click.prevent="toggleLikeTweet()" v-if="userId != tweet.userId">
        <button
          type="submit"
          id="like-button"
          :title="isLiked ? 'Unlike this tweet' : 'Like this tweet'"
          @mouseover="isHoverLike = true"
          @mouseleave="isHoverLike = false"
        >
          <div id="like-icon">
            <font-awesome-icon
              icon="heart"
              :class="['like-icon', { liked: isLiked }]"
            />
            <span id="likes-counter">{{ numberOfLikes }}</span>
          </div>
        </button>
      </form>

      <button
        type="submit"
        id="comment-button"
        @click="
          () => {
            isComments = !isComments;
          }
        "
      >
        <div id="comment-icon">
          <font-awesome-icon icon="comment" />
          <span id="comments-counter">{{ numberOfComments }}</span>
        </div>
      </button>

      <p id="tweet-author">{{ tweet.username }}</p>
      <p id="tweet-date">{{ tweet.createdAt }}</p>
    </section>

    <tweeter-comments v-if="isComments" id="comments" :tweetId="tweet.tweetId">
    </tweeter-comments>
  </article>
</template>

<script>
import TweeterComments from "./TweeterComments.vue";

export default {
  name: "Tweet",

  data() {
    return {
      likedBy: [],
      isHoverLike: false,
      isHoverFollow: false,
      isComments: false,
      numberOfComments: 0,
    };
  },

  props: {
    tweet: {
      type: Object,
    },
  },

  components: {
    TweeterComments,
  },

  computed: {
    loginToken() {
      return this.$store.getters.getLoginToken;
    },
    userId() {
      return this.$store.getters.getUserId;
    },
    isFollowed() {
      return this.$store.getters.getFollows.includes(this.tweet.userId);
    },
    isLiked() {
      return this.likedBy.includes(this.$store.getters.getUserId);
    },
    numberOfLikes() {
      return this.likedBy.length;
    },
  },

  mounted() {
    this.refreshLikedBy();
    this.refreshComments();
  },

  methods: {
    deleteTweet() {
      this.$store.dispatch("deleteTweet", {
        loginToken: this.loginToken,
        tweetId: this.tweet.tweetId,
      });

      this.$store.dispatch("refreshTweets");
    },

    toggleFollow() {
      this.isFollowed
        ? this.$store.dispatch("unfollowUser", {
            loginToken: this.loginToken,
            followId: this.tweet.userId,
          })
        : this.$store.dispatch("followUser", {
            loginToken: this.loginToken,
            followId: this.tweet.userId,
          });
    },

    toggleLikeTweet() {
      this.isLiked
        ? this.$store.dispatch("unlikeTweet", {
            loginToken: this.loginToken,
            tweetId: this.tweet.tweetId,
          })
        : this.$store.dispatch("likeTweet", {
            loginToken: this.loginToken,
            tweetId: this.tweet.tweetId,
          });

      this.refreshLikedBy();
    },

    editTweet() {
      this.$store.dispatch("redirectAction", "edit");
    },

    refreshLikedBy() {
      this.$axios
        .get("/tweet-likes", { params: { tweetId: this.tweet.tweetId } })
        .then((response) => {
          if (response.status === 200) {
            this.likedBy = response.data.map((user) => user.userId);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    refreshComments() {
      this.$axios
        .request({
          url: "/comments",
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD",
          },
          params: { tweetId: this.tweet.tweetId },
        })
        .then((response) => {
          if (response.status === 200) {
            this.numberOfComments = response.data.length;
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

.tweet {
  display: grid;
  grid-template-columns: 1fr auto;
  grid-template-rows: 3rem 8rem 3rem auto;
  height: min-content;

  #delete-button {
    grid-column: 2;
    grid-row: 1;
    @include resetButton;
    padding: 1rem;

    &:hover {
      background-color: lightpink;
    }
  }
  #tweet-content {
    grid-column: 1 / 3;
    grid-row: 2;
    padding: 1rem;
    place-self: center;
  }

  #tweet-info {
    grid-column: 1 / 3;
    grid-row: 3;
    display: flex;
    justify-content: right;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
  }

  #like-icon {
    .liked {
      color: rgb(214, 76, 99);
    }
  }

  #follow-icon {
    .followed {
      color: rgb(79, 165, 79);
      &:hover {
        color: rgb(214, 76, 99);
      }
    }
  }

  #like-button,
  #follow-button,
  #comment-button {
    @include resetButton;
  }

  #comments-counter,
  #likes-counter {
    padding-left: 0.4rem;
  }

  #edit-button {
    @include resetButton;
  }

  #comments {
    grid-row: 4;
  }
}

@media screen and (max-width: 600px) {
  .tweet {
    #delete-button {
      padding: 10px;
    }
    #tweet-content {
      padding: 2px;
    }
  }
}
</style>
