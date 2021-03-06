import Vue from "vue";
import VueRouter from "vue-router";
import TweeterMain from "../views/TweeterMain.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import EditTweet from "../views/EditTweet.vue";
import Profile from "../views/Profile.vue";
import UserProfile from "../views/UserProfile.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Main",
    component: TweeterMain,
  },

  {
    path: "/login",
    name: "Login",
    component: Login,
  },

  {
    path: "/register",
    name: "Register",
    component: Register,
    props: true,
  },

  {
    path: "/edit",
    name: "Edit",
    component: EditTweet,
    props: true,
  },

  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },

  {
    path: "/user-profile",
    name: "UserProfile",
    component: UserProfile,
  },
];

const router = new VueRouter({
  mode: "hash",
  routes,
});

export default router;
