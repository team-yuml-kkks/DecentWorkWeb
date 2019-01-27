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
            email: localStorage.getItem('email'),
            token: localStorage.getItem('token'),
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
        updateCurrentUser (state, data, city, profession) {
            state.currentUser.userData = data
            state.choosenCity = city
            state.choosenProfession = profession
        }
    },
    getters: {
        userId: state => state.currentUser.userId,
        axiosConfig (state) {
            return {
                headers: {'Authorization': 'Token ' + state.currentUser.token},
            }
        },
        userEmail: state => state.currentUser.email,
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
                    commit('updateCurrentUser', data,
                        response.data.city, response.data.professions[0])
                })
        },
    }
});

export { store };