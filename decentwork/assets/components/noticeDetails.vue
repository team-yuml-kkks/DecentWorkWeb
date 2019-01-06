<template>
    <div class="container">
        <div class="row">
            <div class="col-md-8 notice">
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

                <div v-if="!(noticeData.owner === userEmail)">
                    <button class="primaryAction" v-if="!isAssigned" @click="assign">Zgłoś się</button>
                    <button class="primaryAction" v-else @click="unassign">Anuluj zgłoszenie</button>
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

export default {
    data () {
        return {
            noticeData: {},
            assignedWorkers: [],
            isAssigned: false,
            userEmail: localStorage.getItem('email'),
        }
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

        let config = {
            headers: {'Authorization': 'Token ' + localStorage.getItem('token')},
        }

        axios.get('/notices/assign/check/?notice=' + this.$route.params.noticeId, config)
            .then((response) => this.isAssigned = response.data.is_assigned)
    },
    methods: {
        assign () {
            let config = {
                headers: {'Authorization': 'Token ' + localStorage.getItem('token')},
            }

            let params = {
                notice: this.$route.params.noticeId
            }

            axios.post('/notices/assign/user/', params, config)
                .then((response) => this.isAssigned = true)
        },
        unassign () {
            let config = {
                headers: {'Authorization': 'Token ' + localStorage.getItem('token')},
            }

            axios.delete('/notices/assign/user/' + this.$route.params.noticeId + '/', config)
                .then((response) => this.isAssigned = false)
        },
        toWorkerDetail (workerId) {
            this.$router.push({ path: `/workers/details/${workerId}`})
        }
    }
}
</script>
