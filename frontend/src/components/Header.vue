<template>
    <div class="p-2 w-full bg-green-800 text-white flex flex-row justify-between items-center">
        <h1 class="text-lg leading-5 font-medium">
            SpotiMix
        </h1>

        <div class="max-w-[50%]">
            <slot />
        </div>

        <div class="w-10 h-10 rounded-full bg-blue-100" />
    </div>
</template>

