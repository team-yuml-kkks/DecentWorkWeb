<template>
    <nav class="navbar">
        <router-link class="navbar-brand" to="/">
            <img src="./../images/logo_x1.png" height="50" width="50">
        </router-link>
        <router-link class="nav-link" to="/notices">Ogłoszenia</router-link>
        <router-link class="nav-link" to="/workers">Pracownicy</router-link>
        <router-link v-if="logged" class="nav-link" to="/notices/add">Dodaj ogłoszenie</router-link>
        <div class="dropdown" v-if="logged">
            <button class="nav-link circle dropdown-toggle" id="profileDropdown"
                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <font-awesome-icon icon="user" /></button>
            <div class="dropdown-menu" aria-labelledby="profileDropdown">
                <router-link class="dropdown-item"
                    to="/user/profile">Mój profil</router-link>
                <router-link class="dropdown-item"
                    to="/user/password/change">Zmień hasło</router-link>
                <router-link class="dropdown-item"
                    to="/notices/my">Moje ogłoszenia</router-link> 
            </div>
        </div>
        <form v-if="logged" class="form-inline my-2" method="POST" action="/accounts/logout/">
            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
            <button class="btn btn-danger">Wyloguj</button>
        </form>
        <div v-else>
            <a href="/accounts/login/?next=/"><button class="btn btn-danger">Zaloguj</button></a>
        </div>
    </nav>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
    data () {
        return {
            logged: is_logged
        }
    },
    computed: {
        ...mapState({
            csrf: state => state.csrf
        }),
    }
}
</script>