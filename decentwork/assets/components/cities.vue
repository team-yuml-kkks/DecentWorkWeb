<template>
    <div class="autocomplete">
        <label for="city">Miasto</label>
        <br>
        <input class="input_data" type="text" id="city" @input="cityAutocomplete" 
            required v-model.trim="choosenCity"
            placeholder="Podaj miasto(Wymagane)" autocomplete="off">
        <ul class="autocomplete-results">
            <li
                class="autocomplete-result"
                v-for="city in results"
                :key="city.id"
                @click="setCity(city.name)">{{ city.name }}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'

export default {
    data () {
        return {
            cities: [],
            results: [],
        }
    },
    props: {
        city: String,
    },
    mounted: function () {
        this.getCities()
        this.setCity(this.city)
    },
    computed: {
        choosenCity: {
            get () {
                return this.$store.state.choosenCity
            },
            set (city) {
                this.setCity(city)
            }
        }
    },
    methods: {
        getCities () {
            axios.get('/cities/cities/')
                .then((response) => response.data.map((city) => this.cities.push(city)))
                .then(() => this.results = this.cities)
        },
        cityAutocomplete () {
            this.results = this.cities.filter(city => city.name.startsWith(this.choosenCity))
        },
        ...mapActions([
            'setCity'
        ])
    }
}
</script>