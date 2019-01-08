import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex);
Vue.use(require('vue-cookies'));

const store = new Vuex.Store({
    state: {
        csrf: $cookies.get('csrftoken'),
        choosenCity: '',
        choosenProfession: '',
        currentUser: {
            userData: {
                firstName: '',
                lastName: '',
                description: '',
            },
            userId: localStorage.getItem('id'),
        }
    },
    mutations: {
        updateCity (state, city) {
            state.choosenCity = city
        },
        updateProfession (state, profession) {
            state.choosenProfession = profession
        },
        updateFirstName (state, firstName) {
            state.currentUser.userData.firstName = firstName
        },
        updateLastName (state, lastName) {
            state.currentUser.userData.lastName = lastName
        },
        updateDescription (state, description) {
            state.currentUser.userData.description = description
        },
        updateCurrentUser (state, data) {
            state.currentUser.userData = data
        }
    },
    getters: {
        getUserId: () => localStorage.getItem('id'),
        axiosConfig () {
            return {
                headers: {'Authorization': 'Token ' + localStorage.getItem('token')},
            }
        }
    },
    actions: {
        setCity ({ commit, state }, city) {
            commit('updateCity', city)
        },
        setProfession ({ commit, state }, profession) {
            commit('updateProfession', profession)
        },
        setFirstName ({ commit, state }, firstName) {
            commit('updateFirstName', firstName)
        },
        setDescription ({ commit, state }, description) {
            commit('updateDescription', description)
        },
        setLastName ({ commit, state }, lastName) {
            commit('updateLastName', lastName)
        },
        setCurrentUser ({ commit, state }) {
            axios.get('/profiles/userProfiles/' + state.currentUser.userId + '/')
                .then((response) => {
                    let data = {
                        firstName: response.data.user.first_name,
                        lastName: response.data.user.last_name,
                        description: response.data.description
                    }
                    commit('updateCurrentUser', data)
                    commit('updateCity', response.data.city)
                    commit('updateProfession', response.data.professions[0])
                })
        },
    }
});

export { store };