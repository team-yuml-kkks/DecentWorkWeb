<template>
    <div>
        <h1>Dodaj ogłoszenie</h1>
        <form @submit.prevent>
            <label for="title">Tytuł</label>
            <input type="text" id="title" required v-model.trim="title"
                placeholder="Podaj tytuł ogłoszenia(Wymagane)" autocomplete="off">

            <textarea placeholder="Opis ogłoszenia" v-model.trim="description"></textarea>

            <cities-input />

            <profession-input />
            
            <button type="submit" @click="addNotice" name="action">Zapisz ogłoszenie</button>
        </form>

        <p>{{ status }}</p>
    </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
import { not, required, sameAs, minLength } from 'vuelidate/lib/validators'

export default {
    data () {
        return {
            title: '',
            description: '',
            status: '',
            STATUS_TEXTS: {
                ADDED: 'Ogłoszenie dodane',
                AUTH_ERROR: 'Błąd autoryzacji',
                WRONG_DATA_ERROR: 'Wprowadzone dane są nie poprawne',
                SOMETHING_WRONG: 'Coś poszło nie tak',
            }
        }
    },
    computed: mapState({
        choosenCity: state => state.choosenCity,
        choosenProfession: state => state.choosenProfession,
    }),
    methods: {
        addNotice () {
            if (!this.$v.$invalid) {
                let config = {
                    headers: {'Authorization': 'Token ' + localStorage.getItem('token')},
                }

                let params = {
                    'title': this.title,
                    'description': this.description,
                    'city': this.choosenCity,
                    'profession': this.choosenProfession
                }

                axios.post('/notices/notices/', params, config)
                    .then((response) => this.status = this.STATUS_TEXTS.ADDED)
                    .catch((error) => {
                        if (error.response.status === 401) {
                            this.status = this.STATUS_TEXTS.AUTH_ERROR
                        } else if (error.response.status === 400) {
                            this.status = this.STATUS_TEXTS.WRONG_DATA_ERROR
                        } else {
                            this.status = this.STATUS_TEXTS.SOMETHING_WRONG
                        }
                    })
            }
        }
    },
    validations: {
        title: {
            required
        },
        choosenCity: {
            required
        }
    }
}
</script>