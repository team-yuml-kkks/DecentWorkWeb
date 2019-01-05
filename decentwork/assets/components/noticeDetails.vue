<template>
    <div>
        <div>
            <label for="title">Tytuł: </label>
            <p id="title">{{ noticeData.title }}</p>
            <label for="owner">Zleceniodawca: </label>
            <p id="owner">{{ noticeData.owner }}</p>
            <label for="profession">Profesja: </label>
            <p id="profession">{{ noticeData.profession }}</p>
            <label for="city">Miasto: </label>
            <p id="city">{{ noticeData.city }}</p>
            <textarea v-model="noticeData.description" readonly></textarea>
            <label>Stworzono: </label>
            <p>{{ noticeData.created }}</p>
        </div>

        <div>
            <p>Liczba zgłoszonych pracowników: {{ this.assignedWorkers.length }}</p>
        </div>
        
        <div v-if="assignedWorkers.length != 0">
            <h1>Zgłoszeni pracownicy:</h1>
            <table>
                <tbody>
                    <tr v-for="worker in assignedWorkers" :key="worker.user">
                        <td>{{ worker.email }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            noticeData: {},
            assignedWorkers: []
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
    }
}
</script>
