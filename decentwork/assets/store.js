import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
Vue.use(require('vue-cookies'));

const store = new Vuex.Store({
    state: {
        csrf: $cookies.get('csrftoken'),
        choosenCity: '',
        choosenProfession: '',
    },
    mutations: {
        updateCity (state, city) {
            state.choosenCity = city
        },
        updateProfession (state, profession) {
            state.choosenProfession = profession
        }
    },
    getters: {

    },
    actions: {
        setCity ({ commit, state }, city) {
            commit('updateCity', city)
        },
        setProfession ({ commit, state}, profession) {
            commit('updateProfession', profession)
        }
    }
});

export { store };