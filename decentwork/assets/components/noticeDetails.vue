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

                <div>
                    <button class="primaryAction" v-if="!isAssigned" @click="assign">Zgłoś się</button>
                    <button class="primaryAction" v-else @click="unassign">Anuluj zgłoszenie</button>
                </div>
            </div>
            <div v-else class="col-md-8 notice">
                <form @submit.prevent>
                    <p>{{ status }}</p>
                    <label for="title">Tytuł: </label>
                    <input type="text" v-model.trim="noticeData.title">
                    <br>
                    <profession-input v-bind:profession="noticeData.profession" />
                    <br>
                    <cities-input v-bind:city="noticeData.city" />
                    <br>
                    <textarea v-model.trim="noticeData.description"></textarea>

                    <button
                        type="submit"
                        class="primaryAction" 
                        @click="editNotice">Edytuj ogłoszenie</button>
                </form>

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
            userEmail: localStorage.getItem('email'),
            status: '',
        }
    },
    computed: {
        ...mapState({
            choosenCity: state => state.choosenCity,
            choosenProfession: state => state.choosenProfession,
        }),
        ...mapGetters([
            'axiosConfig',
        ])
    },
    mounted: function () {
        axios.get('/notices/notices/' + this.$route.params.noticeId + '/')
            .then((response) => {
                this.noticeData = response.data
                
                // Only date without time for now
                this.noticeData.created = this.noticeData.created.split('T')[0]
            })
            .catch((error) => console.log(error))

        axios.get('/notices/assign/list/?notice=' + this.$route.params.noticeId)
            .then((response) => response.data.map((worker) => this.assignedWorkers.push(worker)))

        axios.get('/notices/assign/check/?notice=' + this.$route.params.noticeId, this.axiosConfig)
            .then((response) => this.isAssigned = response.data.is_assigned)
    },
    methods: {
        assign () {
            let params = {
                notice: this.$route.params.noticeId
            }

            axios.post('/notices/assign/user/', params, this.axiosConfig)
                .then((response) => this.isAssigned = true)
        },
        unassign () {
            axios.delete('/notices/assign/user/' + this.$route.params.noticeId + '/', this.axiosConfig)
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

            axios.put('/notices/notices/' + this.$route.params.noticeId + '/', params, this.axiosConfig)
                .then((response) => {
                    this.status = 'Ogłoszenie zostało zapisane.'
                })
        },
        closeNotice () {
            axios.post('/notices/notices/' + this.$route.params.noticeId + '/set_notice_done/', {}, this.axiosConfig)
                .then((response) => {
                    this.status = 'Ogłoszenie zostało zamknięte.'
                })
        },
        ...mapActions([
            'setCity',
            'setProfession',
        ])
    }
}
</script>
