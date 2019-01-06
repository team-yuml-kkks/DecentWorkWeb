<template>
    <div>
        <form @submit.prevent>
            <label for="first-name">Podaj imie: </label>
            <input type="text" id="first-name" v-model.trim="firstName"
                placeholder="Podaj imię">

            <label for="last-name">Podaj Nazwisko: </label>
            <input type="text" id="last-name" v-model.trim="lastName"
                placeholder="Podaj nazwisko">

            <textarea placeholder="Opis profilu" v-model.trim="description"></textarea>

            <cities-input />

            <profession-input />

            <button type="submit" @click="saveProfile" name="action">Zapisz</button>
        </form>

        <p>{{ status }}</p>
    </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import axios from 'axios'

export default {
    data () {
        return {
            status: '',
            STATUS_TEXTS: {
                ADDED: 'Profil zapisany',
                AUTH_ERROR: 'Błąd autoryzacji',
                WRONG_DATA_ERROR: 'Wprowadzone dane są nie poprawne',
                SOMETHING_WRONG: 'Coś poszło nie tak',
            }
        }
    },
    computed: { 
        ...mapState({
            choosenCity: state => state.choosenCity,
            choosenProfession: state => state.choosenProfession,
        }),
        ...mapGetters([
            'getUserId'
        ]),
        firstName: {
            get () {
                return this.$store.state.currentUser.userData.firstName
            },
            set (firstName) {
                this.setFirstName(firstName)
            }
        },
        lastName: {
            get () {
                return this.$store.state.currentUser.userData.lastName
            },
            set (lastName) {
                this.setLastName(lastName)
            }
        },
        description: {
            get () {
                return this.$store.state.currentUser.userData.description
            },
            set (description) {
                this.setDescription(description)
            }
        }
    },
    mounted: function () {
        this.setCurrentUser()
    },
    methods: {
        saveProfile () {
            let config = {
                headers: {'Authorization': 'Token ' + localStorage.getItem('token')},
            }

            let params = {
                'user': {
                    'first_name': this.firstName,
                    'last_name': this.lastName,
                },
                'description': this.description,
                'city': this.choosenCity,
                'professions': [this.choosenProfession]
            }

            axios.put('profiles/userProfiles/' + this.getUserId + '/', params, config)
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
        },
        ...mapActions([
            'setCity',
            'setFirstName',
            'setLastName',
            'setDescription',
            'setCurrentUser'
        ])
    }
}
</script>