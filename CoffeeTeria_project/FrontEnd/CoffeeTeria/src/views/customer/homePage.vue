<script lang="ts" setup>
import Card from "@/components/homePage/Card.vue";
import Navbar from "@/components/homePage/Navbar.vue";
let cardsInfo = [
  {
    id: 0,
    image: "src/assets/image 3.png",
    title: "Search",
    to:'/viewCoffeeShops'
  },
  {
    id: 1,
    image: "src/assets/image 4.png",
    title: "Tips and Hints",
    to:''
  },
  {
    id: 2,
    image: "src/assets/image 5.png",
    title: "Historical Facts",
    to:''
  },
  {
    id: 3,
    image: "src/assets/image 6.png",
    title: "Recipes",
    to:''
  },
  {
    id: 4,
    image: "src/assets/image 7.png",
    title: "Information",
    to:''
  },
];
</script>

<template>
  <main>
    <Navbar/>
    <div class="container">
        
      <Card v-for="card in cardsInfo" :card-info="card" />
    </div>
  </main>
</template>

<style scoped>
.container{
    padding-top: 5rem;
    padding-inline: 20%;
    margin-inline:auto ;
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    justify-content: center;
    align-items: center;
}
</style>
