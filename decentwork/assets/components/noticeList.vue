<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th scope="col">Tytuł</th>
                            <th scope="col">Opis</th>
                            <th scope="col">Miasto</th>
                            <th scope="col">Profesja</th>
                        </tr>
                    </thead>
                    <tbody>
                        <img v-if="loading" src="./../images/loading.gif">
                        <tr 
                            @click="toNoticeDetail(notice.id)"
                            v-for="notice in notices"
                            :key="notice.id"
                            class="notice-row">
                            <td>{{ notice.title }}</td>
                            <td>{{ notice.description }}</td>
                            <td>{{ notice.city }}</td>
                            <td>{{ notice.profession }}</td>
                        </tr>
                    </tbody>
                </table>
                <button
                    class="primaryAction"
                    v-if="previousURL != null"
                    @click="getNotices(previousURL)">Poprzednia</button>
                <button
                    class="primaryAction"
                    v-if="nextURL != null"
                    @click="getNotices(nextURL)">Następna</button>
            </div>
        </div>
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
        needToken: Boolean,
    },
    created () {
        this.getNotices(this.startURL)
    },
    methods: {
        getNotices (URL) {
            this.notices = []
            this.loading = true

            var config = {}

            if (this.needToken) {
                config = {
                    headers: {'Authorization': 'Token ' + localStorage.getItem('token')},
                }
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
        toNoticeDetail (noticeId) {
            this.$router.push({ path: `/notice/details/${noticeId}`})
        }
    }
}
</script>