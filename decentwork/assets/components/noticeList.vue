<template>
    <div>
        <table class="table">
            <thead class="thead-light">
                <tr>
                    <th scope="col">Tytuł</th>
                    <th scope="col">Opis</th>
                    <th scope="col">Miasto</th>
                    <th scope="col">Profesja</th>
                </tr>
            </thead>
            <tbody>
                <img v-if="loading" src="./../images/loading.gif">
                <tr v-for="notice in notices" :key="notice.id">
                    <td>{{ notice.title }}</td>
                    <td>{{ notice.description }}</td>
                    <td>{{ notice.city }}</td>
                    <td>{{ notice.profession }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            notices: [],
            loading: false,
        }
    },
    created () {
        this.getNotices()
    },
    methods: {
        getNotices () {
            this.loading = true
            axios.get('/notices/notices')
                .then((response) => response.data.results.map(
                    (notice) => this.notices.push(notice)))
                .then(() => this.loading = false)
        }
    }
}
</script>