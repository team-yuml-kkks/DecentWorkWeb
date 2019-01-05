<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <table class="table table-striped">
                    <thead class="thead-dark">
                        <tr>
                            <th scope="col">Imię</th>
                            <th scope="col">Nazwisko</th>
                            <th scope="col">Miasto</th>
                            <th scope="col">Profesje</th>
                        </tr>
                    </thead>
                    <tbody>
                        <img v-if="loading" src="./../images/loading.gif">
                        <tr
                            @click="toWorkerDetail(worker.user.id)"
                            v-for="worker in workers"
                            :key="worker.user.id"
                            class="notice-row">
                            <td>{{ worker.user.first_name }}</td>
                            <td>{{ worker.user.last_name }}</td>
                            <td>{{ worker.city }}</td>
                            <td>{{ worker.professions }}</td>
                        </tr>
                    </tbody>
                </table>
                <button v-if="previousURL != null" @click="getWorkers(previousURL)">Poprzednia</button>
                <button v-if="nextURL != null" @click="getWorkers(nextURL)">Następna</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            workers: [],
            loading: false,
            nextURL: null,
            previousURL: null,
        }
    },
    created () {
        this.getWorkers('/profiles/withProfession/')
    },
    methods: {
        getWorkers (URL) {
            this.workers = []
            this.loading = true

            axios.get(URL)
                .then((response) => {
                    response.data.results
                        .map((worker) => this.workers.push(worker))
                    this.nextURL = response.data.next
                    this.previousURL = response.data.previous
                })
                .catch((error) => {
                    console.log(error)
                })
                .then(() => this.loading = false)
        },
        toWorkerDetail (workerId) {
            this.$router.push({ path: `/workers/details/${workerId}`})
        }
    }
}
</script>