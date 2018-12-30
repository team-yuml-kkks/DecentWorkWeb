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
        <button v-if="previousURL != null" @click="getNotices(previousURL)">Poprzednia</button>
        <button v-if="nextURL != null" @click="getNotices(nextURL)">Następna</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            notices: [],
            loading: false,
            nextURL: null,
            previousURL: null,
        }
    },
    props: {
        startURL: String,
    },
    created () {
        this.getNotices(this.startURL)
    },
    methods: {
        getNotices (URL) {
            this.notices = []
            this.loading = true

            let config = {
                headers: {'Authorization': 'Token ' + localStorage.getItem('token')},
            }

            axios.get(URL, config)
                .then((response) => {
                        response.data.results
                            .map((notice) => this.notices.push(notice))
                        this.nextURL = response.data.next
                        this.previousURL = response.data.previous
                    })
                .catch((error) => {
                    console.log(error)
                })
                .then(() => this.loading = false)
        },
    }
}
</script>