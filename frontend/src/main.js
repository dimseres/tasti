import 'normalize.css';
import './assets/fonts/Montserrat/font.css';
import './assets/fonts/Roboto/font.css';
import './assets/styles/app.scss';
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

createApp(App).use(store).use(router).mount("#app");
