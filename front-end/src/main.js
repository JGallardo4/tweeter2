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

axios.defaults.baseURL = "http://127.0.0.1:5000/api";

axios.interceptors.response.use(
  function(response) {
    if (response.status.valueOf() === 401) {
      store.dispatch("logOut");
    } else {
      return response;
    }
  },
  function(error) {
    return Promise.reject(error);
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
