import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
Vue.use(require('vue-cookies'));

const store = new Vuex.Store({
    state: {
        csrf: $cookies.get('csrftoken'),
    },
    mutations: {

    },
    getters: {

    },
    actions: {

    }
});

export { store };