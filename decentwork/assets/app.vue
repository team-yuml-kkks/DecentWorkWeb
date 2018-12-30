<template id="app">
    <div>
        <navbar />
        <p class="test">Hello world Vue</p>
        <router-view :key="$route.fullPath"></router-view>
    </div>
</template>