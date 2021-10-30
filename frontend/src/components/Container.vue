<template>
    <div class="w-screen h-screen bg-gray-200">
        <div class="w-screen h-screen bg-gray-300 mx-auto flex flex-col">
            <Header>
                <input
                    class="px-4 py-3 rounded-md bg-green-700 w-full text-white placeholder-white leading-4 text-sm"
                    placeholder="Buscar..."
                    v-model="search"
                />
            </Header>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref, Ref, watch } from 'vue';

import Header from './Header.vue';

components: { Header };

const search: Ref<string> = ref('');
let searchInterval: any = null;

const host = `${location.protocol}//${location.hostname}:4444`;

watch(search, newValue => {
    clearInterval(searchInterval);

    searchInterval = setTimeout(() => {
        searchSongs(newValue);
    }, 200);
});

const searchSongs = async (value: string): Promise<void> => {
    const result = await axios({
        url: `${host}/search`,
        method: 'POST',
        data: JSON.stringify({ value }),
    });

    console.log(result);
}

</script>

