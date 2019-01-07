<template>
    <!-- I will probably join it with cities.vue when more time available -->
    <div class="autocomplete">
        <label for="profession">Profesja</label>
        <br>
        <input class="input_data" type="text" id="profession" @input="professionAutocomplete" 
            required v-model.trim="choosenProfession"
            placeholder="Podaj profesje" autocomplete="off">
        <ul class="autocomplete-results">
            <li
                class="autocomplete-result"
                v-for="profession in results"
                :key="profession.id"
                @click="setProfession(profession.name)">{{ profession.name }}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'

export default {
    data () {
        return {
            professions: [],
            results: [],
        }
    },
    mounted: function () {
        this.getProfessions()
        this.setProfession('')
    },
    computed: {
        choosenProfession: {
            get () {
                return this.$store.state.choosenProfession
            },
            set (profession) {
                this.setProfession(profession)
            }
        }
    },
    methods: {
        getProfessions () {
            axios.get('/professions/professions/')
                .then((response) => response.data
                    .map((profession) => this.professions.push(profession)))
                .then(() => this.results = this.professions)
        },
        professionAutocomplete () {
            this.results = this.professions
                .filter(profession => profession.name
                    .startsWith(this.choosenProfession))
        },
        ...mapActions([
            'setProfession'
        ])
    }
}
</script>