<template>
    <div class="w-screen h-screen bg-gray-200">
        <div class="w-screen max-w-[500px] h-screen bg-gray-300 mx-auto flex flex-col">
            <Header />
        </div>
    </div>
</template>

<script setup lang="ts">
import Header from './Header.vue';

components: { Header };
</script>

