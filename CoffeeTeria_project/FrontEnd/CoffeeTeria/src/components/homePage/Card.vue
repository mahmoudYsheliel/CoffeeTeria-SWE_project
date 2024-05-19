<script lang="ts" setup>
// Importing necessary components and utilities
import { useRouter } from 'vue-router';
import Button from 'primevue/button';

// Accessing router instance
const router = useRouter();

// Defining props for the component
defineProps(['cardInfo']);
</script>

<template>
    <main>
        <div class="container">
            <!-- Displaying card image -->
            <img :src="cardInfo?.image" alt="">

            <!-- Button with card title -->
            <Button :label="cardInfo.title" @click="router.push(cardInfo.to)"/>
        </div>
    </main>
</template>

<style scoped> 
.container{
    width: 16rem;
    height: 16rem;
    background-color: var(--accent1);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
}

img{
    width:61.75% ;
    aspect-ratio: 1/1;
}

button{
    width: 61.75%;
}
</style>
