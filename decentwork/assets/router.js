import VueRouter from 'vue-router'
import Vue from 'vue'
import Vuelidate from 'vuelidate'

Vue.use(VueRouter)
Vue.use(Vuelidate)

const routes = [
    {
        path: '/',
        component: require('./components/home.vue').default
    },
    {
        path: '/notices',
        component: require('./components/noticeList.vue').default,
        props: { startURL: '/notices/notices/' }
    },
    {
        path: '/workers',
        component: require('./components/workerList.vue').default
    },
    {
        path: '/notices/add',
        component: require('./components/addNotice.vue').default
    },
    {
        path: '/notices/my',
        component: require('./components/noticeList.vue').default,
        props: { startURL: '/notices/user/notices/' }
    },
    {
        path: '/user/password/change',
        component: require('./components/changePassword.vue').default
    },
];

const router = new VueRouter({
    routes,
});

export { router };