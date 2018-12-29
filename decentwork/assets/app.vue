<template id="app">
    <div>
        <p>Hello world Vue</p>
        <form method="POST" action="/accounts/logout/">
            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
            <button>Wyloguj</button>
        </form>
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