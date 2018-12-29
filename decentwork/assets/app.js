import 'bootstrap';

import Vue from 'vue';
import VueSession from 'vue-session'
import App from './app.vue';
import { store } from './store';
import { router } from './router';
import './scss/main.scss';

Vue.use(require('vue-cookies'));
Vue.use(VueSession);
Vue.component('navbar', require('./components/navbar.vue').default);

var app = new Vue({
    el: '#app',
    store,
    router,
    render: h => h(App)
});