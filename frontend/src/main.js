import 'normalize.css';
import './assets/fonts/Montserrat/font.css';
import './assets/fonts/Roboto/font.css';
import './assets/styles/app.scss';
import {createApp} from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";


axios.defaults.baseURL = process.env.VUE_APP_BASE_URL;
createApp(App)
    .use(store)
    .use(router)
    .use(VueAxios, axios)
    .mount("#app");
