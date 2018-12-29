<template>
    <div class="container">
        <nav class="navbar navbar-light bg-light border border-dark">
            <router-link class="navbar-brand" to="/">
                <img src="./../images/logo_x1.png" height="50" width="50">
            </router-link>
            <router-link class="nav-link" to="/notices">Ogłoszenia</router-link>
            <router-link class="nav-link" to="/workers">Pracownicy</router-link>
            <router-link class="nav-link" to="/notices/add">Dodaj ogłoszenie</router-link>
            <div class="dropdown">
                <button class="nav-link circle dropdown-toggle" id="profileDropdown"
                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></button>
                <div class="dropdown-menu" aria-labelledby="profileDropdown">
                    <a class="dropdown-item" href="#">Zobacz profil</a>
                    <a class="dropdown-item" href="#">Zmień hasło</a>
                    <router-link class="dropdown-item"
                        to="/notices/my">Moje ogłoszenia</router-link> 
                </div>
            </div>
            <form class="form-inline my-2" method="POST" action="/accounts/logout/">
                <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                <button class="btn btn-danger">Wyloguj</button>
            </form>
        </nav>
    </div>
</template>

<script>
export default {
    data() {
        return {
            csrf: $cookies.get('csrftoken')
        }
    }
}
</script>