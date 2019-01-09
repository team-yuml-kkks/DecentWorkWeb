<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12 notice">
                <p>Imię: {{ workerData.first_name }}</p>
                <p>Nazwisko: {{ workerData.last_name }}</p>
                <textarea v-model="workerData.description" readonly></textarea>
                <p>Miasto: {{ workerData.city }}</p>
                <p>Profesje: {{ workerData.professions }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            workerData: []
        }
    },
    mounted: function () {
        axios.get('/profiles/userProfiles/' + this.$route.params.workerId + '/')
            .then((response) => {
                this.workerData = response.data
                this.workerData.first_name = response.data.user.first_name
                this.workerData.last_name = response.data.user.last_name
                this.workerData.professions = this.workerData.professions.join(',')
            })
    }
}
</script>