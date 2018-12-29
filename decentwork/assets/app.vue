<template id="app">
    <div>
        <p class="test">Hello world Vue</p>
        <form method="POST" action="/accounts/logout/">
            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
            <button class="btn btn-danger">Wyloguj</button>
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