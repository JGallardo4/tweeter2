import Vue from "vue";
import Vuex from "vuex";
import VuexPersistence from "vuex-persist";
import router from "../router/index.js";
import axios from "axios";

Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
});

export default new Vuex.Store({
  state: {
    userId: "",
    userName: "",
    loginToken: "",
    follows: [],
    allTweets: [],
  },

  getters: {
    getUserName(state) {
      return state.userName;
    },

    getUserId(state) {
      return state.userId;
    },

    getLoginToken(state) {
      return state.loginToken;
    },

    getAllTweets(state) {
      return state.allTweets;
    },

    getFollows(state) {
      return state.follows;
    },
  },

  mutations: {
    SET_USERID(state, payload) {
      state.userId = payload;
    },

    SET_LOGIN_TOKEN(state, payload) {
      state.loginToken = payload;
    },

    SET_USERNAME(state, payload) {
      state.userName = payload;
    },

    DELETE_USERDATA(state) {
      state.userId = "";
      state.userName = "";
      state.loginToken = "";
    },

    SET_TWEETS(state, payload) {
      state.allTweets = payload;
    },

    SET_FOLLOWS(state, payload) {
      state.follows = payload;
    },
  },

  actions: {
    logIn({ commit }, payload) {
      return new Promise((resolve, reject) => {
        axios
          .post("/login", payload)
          .then((response) => {
            if (response.status === 201) {
              var _user = response.data[0];
              commit("SET_LOGIN_TOKEN", _user.loginToken);
              commit("SET_USERID", _user.userId);
              commit("SET_USERNAME", _user.username);
              resolve(response);
            } else {
              reject(response);
            }
          })
          .catch((error) => {
            reject(error);
          });
      });
    },

    logOut({ commit, dispatch }) {
      commit("DELETE_USERDATA");
      dispatch("redirect", "/login");
    },

    checkLogin({ dispatch }) {
      if (this.getters.getLoginToken !== "") {
        dispatch("redirect", "/");
      } else {
        dispatch("logOut");
      }
    },

    register({ commit, dispatch }, payload) {
      return new Promise((resolve, reject) => {
        axios
          .post("/users", payload)
          .then((response) => {
            if (response.status === 201) {
              commit("SET_AUTHENTICATED", true);
              commit("SET_USERID", response.data.userId);
              commit("SET_USERNAME", response.data.username);
              commit("SET_LOGIN_TOKEN", response.data.loginToken);
              dispatch("redirect", "/");
              resolve(response);
            } else {
              reject(response);
            }
          })
          .catch((error) => {
            reject(error);
          });
      });
    },

    initializeStore({ state }) {
      if (window.localStorage.getItem("vuex")) {
        this.replaceState(
          Object.assign(state, JSON.parse(window.localStorage.getItem("state")))
        );
      }
    },

    postTweet({ getters }, payload) {
      axios
        .post("/tweets", {
          loginToken: getters.getLoginToken,
          content: payload,
        })
        .catch((response) => console.log(response));
    },

    refreshTweets({ commit, state }) {
      axios
        .get("/tweets", { params: { userId: state.userId } })
        .then((response) => {
          if (response.status === 200) {
            commit("SET_TWEETS", response.data);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    refreshFollows({ state, commit }) {
      axios
        .get("/follows", { params: { userId: state.userId } })
        .then((response) => {
          if (response.status === 200) {
            commit(
              "SET_FOLLOWS",
              response.data.map((user) => user.userId)
            );
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deleteTweet(state, payload) {
      axios.delete("/tweets", { data: payload });
    },

    followUser({ dispatch }, payload) {
      axios
        .request({
          url: "/follows",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD",
          },
          data: payload,
        })
        .then(dispatch("refreshFollows"))
        .catch((error) => {
          console.log(error);
        });
    },

    unfollowUser({ dispatch }, payload) {
      axios
        .request({
          url: "/follows",
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD",
          },
          data: payload,
        })
        .then(dispatch("refreshFollows"))
        .catch((error) => {
          console.log(error);
        });
    },

    getUsers() {
      axios
        .get("/users")
        .then((response) => response.data.map((user) => user.userId))
        .then(console.log)
        .catch((error) => {
          console.log(error);
        });
    },

    likeTweet(state, payload) {
      axios
        .request({
          url: "/tweet-likes",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD",
          },
          data: payload,
        })
        .catch((error) => {
          console.log(error);
        });
    },

    refreshLikes() {
      axios
        .get("/tweet-likes")
        .then((response) => response.data.map((user) => user.userId))
        .then((response) => (this.likedBy = response))
        .catch(console.log);
    },

    unlikeTweet(state, payload) {
      axios
        .request({
          url: "/tweet-likes",
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD",
          },
          data: payload,
        })
        .catch((error) => {
          console.log(error);
        });
    },

    redirect(state, route) {
      if (router.currentRoute !== route) {
        router.push(route).catch((error) => {
          if (
            error.name !== "NavigationDuplicated" &&
            !error.message.includes(
              "Avoided redundant navigation to current location"
            )
          ) {
            console.log(error);
          }
        });
      }
    },
  },

  plugins: [vuexLocal.plugin],
});
