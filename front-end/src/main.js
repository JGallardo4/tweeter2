import Vue from "vue";
import axios from "axios";
import cookies from "vue-cookies";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faUser,
  faUserTimes,
  faUserCheck,
  faUserPlus,
  faTimes,
  faCrow,
  faHeart,
  faPen,
  faUndo,
  faComment,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import router from "./router/index.js";
import App from "./App.vue";
import store from "./store";

library.add(
  faUser,
  faUserTimes,
  faUserCheck,
  faUserPlus,
  faTimes,
  faCrow,
  faHeart,
  faPen,
  faUndo,
  faComment
);

Vue.component("font-awesome-icon", FontAwesomeIcon);

axios.defaults.headers.common["X-Api-Key"] =
  "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD";
axios.defaults.headers.common["Content-Type"] = "application/json";

axios.defaults.baseURL = "https://ravenblogs.tk/api";

// Log user out when token expires
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      console.log("invalid token!");
      store.dispatch("logOut");
      return Promise.reject(error);
    } else {
      throw error;
    }
  }
);

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;

window.vm = new Vue({
  router,
  store,
  axios,
  cookies,
  render: (h) => h(App),
}).$mount("#app");
