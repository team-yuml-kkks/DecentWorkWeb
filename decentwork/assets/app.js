import 'bootstrap';

import Vue from 'vue';
import App from './app.vue';
import { store } from './store';
import './scss/main.scss';

Vue.use(require('vue-cookies'))


var app = new Vue({
    el: '#app',
    store,
    render: h => h(App)
});