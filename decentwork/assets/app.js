import 'bootstrap';

import Vue from 'vue';
import App from './app.vue';
import { store } from './store';
import { router } from './router';
import './scss/main.scss';

Vue.use(require('vue-cookies'));
Vue.component('navbar', require('./components/navbar.vue').default);

var app = new Vue({
    el: '#app',
    store,
    router,
    render: h => h(App)
});