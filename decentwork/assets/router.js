import VueRouter from 'vue-router'
import Vue from 'vue'

Vue.use(VueRouter)

const routes = [
    { path: '/', component: require('./components/home.vue').default },
    { path: '/notices', component: require('./components/noticeList.vue').default },
    { path: '/workers', component: require('./components/workerList.vue').default },
    { path: '/notices/add', component: require('./components/addNotice.vue').default }
];

const router = new VueRouter({
    routes,
});

export { router };