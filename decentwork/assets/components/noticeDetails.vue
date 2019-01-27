<template>
    <div class="container">
        <div class="row">
            <div v-if="!(noticeData.owner === userEmail)" class="col-md-8 notice">
                <label for="title">Tytuł: {{ noticeData.title }}</label>
                <br>
                <label for="owner">Zleceniodawca: {{ noticeData.owner }}</label>
                <br>
                <label for="profession">Profesja: {{ noticeData.profession }}</label>
                <br>
                <label for="city">Miasto: {{ noticeData.city }}</label>
                <br>
                <textarea v-model="noticeData.description" readonly></textarea>
                <br>
                <label>Stworzono: {{ noticeData.created }}</label>

                <div v-if="isLogged">
                    <button class="primaryAction" v-if="!isAssigned" @click="assign">Zgłoś się</button>
                    <button class="primaryAction" v-else @click="unassign">Anuluj zgłoszenie</button>
                </div>
            </div>
            <div v-else class="col-md-8 notice">
                <form @submit.prevent>
                    <p>{{ status }}</p>
                    <label for="title">Tytuł: </label>
                    <br>
                    <input class="input_data" type="text" v-model.trim="noticeData.title">
                    <br>
                    <profession-input v-bind:profession="noticeData.profession" />
                    <br>
                    <cities-input v-bind:city="noticeData.city" />
                    <br>
                    <textarea v-model.trim="noticeData.description"></textarea>
                    <br>
                    <button
                        type="submit"
                        class="primaryAction" 
                        @click="editNotice">Edytuj ogłoszenie</button>
                </form>

                <br>
                <div>
                    <button class="primaryAction" @click="closeNotice">Zamknij zgłoszenie</button>
                </div>
            </div>
            

            <div class="col-md-4 assigned">
                <div>
                    <p class="imporant_info">Liczba zgłoszonych pracowników: {{ this.assignedWorkers.length }}</p>
                </div>
                
                <div v-if="assignedWorkers.length != 0">
                    <h3>Zgłoszeni pracownicy:</h3>
                    <table>
                        <tbody>
                            <tr v-for="worker in assignedWorkers" :key="worker.user">
                                <td class="assigned-users" @click="toWorkerDetail(worker.user)">{{ worker.email }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
    data () {
        return {
            noticeData: {},
            assignedWorkers: [],
            isAssigned: false,
            status: '',
            STATUS_TEXTS: {
                NOTICE_SAVED: 'Ogłoszenie zostało zapisane.',
                NOTICE_CLOSED: 'Ogłoszenie zostało zamknięte.',
            },
            URLS: {
                GET_NOTICE: '/notices/notices/' + this.$route.params.noticeId + '/',
                GET_ASSIGNED_LIST: '/notices/assign/list/?notice='
                    + this.$route.params.noticeId,
                CHECK_USER_ASSIGN: '/notices/assign/check/?notice='
                    + this.$route.params.noticeId,
                ASSIGN_USER: '/notices/assign/user/',
                UNASSIGN_USER: '/notices/assign/user/'
                    + this.$route.params.noticeId + '/',
                EDIT_NOTICE: '/notices/notices/' + this.$route.params.noticeId + '/',
                CLOSE_NOTICE: '/notices/notices/'
                    + this.$route.params.noticeId + '/set_notice_done/',
            },
            isLogged: is_logged,
        }
    },
    computed: {
        ...mapState({
            choosenCity: state => state.choosenCity,
            choosenProfession: state => state.choosenProfession,
        }),
        ...mapGetters([
            'axiosConfig',
            'userEmail',
        ])
    },
    mounted: function () {
        axios.get(this.URLS.GET_NOTICE)
            .then((response) => {
                this.noticeData = response.data
                
                // Only date without time for now
                this.noticeData.created = this.noticeData.created.split('T')[0]
            })
            .catch((error) => console.log(error))

        axios.get(this.URLS.GET_ASSIGNED_LIST)
            .then((response) => response.data.map((worker) => this.assignedWorkers.push(worker)))

        if (this.isLogged) {
            axios.get(this.URLS.CHECK_USER_ASSIGN, this.axiosConfig)
                .then((response) => this.isAssigned = response.data.is_assigned)
        }
    },
    methods: {
        assign () {
            let params = {
                notice: this.$route.params.noticeId
            }

            axios.post(this.URLS.ASSIGN_USER, params, this.axiosConfig)
                .then((response) => this.isAssigned = true)
        },
        unassign () {
            axios.delete(this.URLS.UNASSIGN_USER, this.axiosConfig)
                .then((response) => this.isAssigned = false)
        },
        toWorkerDetail (workerId) {
            this.$router.push({ path: `/workers/details/${workerId}`})
        },
        editNotice () {
            let params = {
                'title': this.noticeData.title,
                'description': this.noticeData.description,
                'city': this.choosenCity,
                'profession': this.choosenProfession
            }

            axios.put(this.URLS.EDIT_NOTICE, params, this.axiosConfig)
                .then((response) => {
                    this.status = this.STATUS_TEXTS.NOTICE_SAVED
                })
        },
        closeNotice () {
            axios.post(this.URLS.CLOSE_NOTICE, {}, this.axiosConfig)
                .then((response) => {
                    this.status = this.STATUS_TEXTS.NOTICE_CLOSED
                })
        },
        ...mapActions([
            'setCity',
            'setProfession',
        ])
    }
}
</script>
