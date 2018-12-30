<template>
    <div class="container">
        <form @submit.prevent>
            <div>{{ error }}</div>
            <div>Pole jest wymagane</div>
            <div>Hasło musi mieć 8 znaków</div>
            <label for="id_oldpassword">Obecne hasło:</label>
            <input type="password" name="oldpassword" v-model.trim="oldPassword"
                placeholder="Obecne hasło" required id="id_oldpassword">

            <div>Pole jest wymagane</div>
            <div>Hasło musi mieć 8 znaków</div>
            <label for="id_password1">Nowe hasło:</label>
            <input type="password" name="password1" v-model.trim="password"
                placeholder="Nowe hasło" required id="id_password1">

            <div>Hasła muszą się zgadzać</div>
            <label for="id_password2">Potwierdź nowe hasło: </label>
            <input type="password" name="password2" v-model.trim="repeatPassword"
                placeholder="Potwierdź nowe hasło" required id="id_password2">
            <button type="submit" @click="changePassword" name="action">Zmień hasło</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
import { not, required, sameAs, minLength } from 'vuelidate/lib/validators'

export default {
    data () {
        return {
            oldPassword: '',
            password: '',
            repeatPassword: '',
            error: '',
        }
    },
    validations: {
        oldPassword: {
            required,
            minLength: minLength(8)
        },
        password: {
            required,
            minLength: minLength(8)
        },
        repeatPassword: {
            sameAsPassword: sameAs('password'),
            notSameAsOld: not(sameAs('oldPassword'))
        }
    },
    methods: {
        changePassword () {
            if (!this.$v.$invalid) {
                this.error = 'Loading...'
                let config = {
                    headers: {
                        'Authorization': 'Token ' + localStorage.getItem('token'),
                    },
                }

                let params = {
                    'oldpassword': this.oldPassword,
                    'password1': this.password,
                }

                axios.post('/common/user/password/change/', params, config)
                    .then((response) => this.error = 'Hasło zostało zmienione')
                    .catch((error) => {
                        if (error.response.status === 401) {
                            this.error = 'Wprowadź poprawne obecne hasło'
                        } else if (error.response.status === 400) {
                            this.error = 'Wprowadź poprawne nowe hasło'
                        } else {
                            this.error = 'Coś poszło nie tak'
                        }
                    })
            }
        },
    }
}
</script>