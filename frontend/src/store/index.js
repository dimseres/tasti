import {createStore} from "vuex";
import course from './modules/course';
import account from "./modules/account";

export default createStore({
    state: {},
    mutations: {},
    actions: {},
    modules: {course, account},
});
