<template id="app">
    <div>
        <navbar />
        <router-view :key="$route.fullPath"></router-view>
    </div>
</template>