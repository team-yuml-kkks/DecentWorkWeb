<template>
    <nav class="navbar">
        <router-link class="navbar-brand" to="/">
            <img src="./../images/logo_x1.png" height="50" width="50">
        </router-link>
        <router-link class="nav-link" to="/notices">Ogłoszenia</router-link>
        <router-link class="nav-link" to="/workers">Pracownicy</router-link>
        <router-link class="nav-link" to="/notices/add">Dodaj ogłoszenie</router-link>
        <div class="dropdown">
            <button class="nav-link circle dropdown-toggle" id="profileDropdown"
                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <font-awesome-icon icon="user" /></button>
            <div class="dropdown-menu" aria-labelledby="profileDropdown">
                <a class="dropdown-item" href="#">Zobacz profil</a>
                <router-link class="dropdown-item"
                    to="/user/password/change">Zmień hasło</router-link>
                <router-link class="dropdown-item"
                    to="/notices/my">Moje ogłoszenia</router-link> 
            </div>
        </div>
        <form class="form-inline my-2" method="POST" action="/accounts/logout/">
            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
            <button class="btn btn-danger">Wyloguj</button>
        </form>
    </nav>
</template>

<script>
import { mapState } from 'vuex'

export default {
    computed: mapState({
        csrf: state => state.csrf
    })
}
</script>