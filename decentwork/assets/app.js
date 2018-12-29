import Vue from 'vue';
import App from './app.vue';
import { store } from './store';

Vue.use(require('vue-cookies'))

var app = new Vue({
    el: '#app',
    store,
    render: h => h(App)
});