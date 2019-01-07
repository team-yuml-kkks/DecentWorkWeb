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
        props: { startURL: '/notices/notices/', needToken: false }
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
        props: { startURL: '/notices/user/notices/', needToken: true }
    },
    {
        path: '/user/password/change',
        component: require('./components/changePassword.vue').default
    },
    {
        path: '/user/profile',
        component: require('./components/editProfile.vue').default
    },
    {
        path: '/notice/details/:noticeId',
        component: require('./components/noticeDetails.vue').default
    },
    {
        path: '/workers/details/:workerId',
        component: require('./components/profileDetails.vue').default
    }
];

const router = new VueRouter({
    mode: 'history',
    routes,
});

export { router };