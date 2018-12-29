import Vue from 'vue';
import App from './app.vue';
import { store } from './store';

var app = new Vue({
    el: '#app',
    store,
    render: h => h(App)
});