<script lang="ts" setup>
// Importing components
import Card from "@/components/homePage/Card.vue";
import Navbar from "@/components/homePage/Navbar.vue";

// Array containing information about cards
let cardsInfo = [
  {
    id: 0,
    image: "/images/image 3.png",
    title: "Search",
    to: '/viewCoffeeShops'
  },
  {
    id: 1,
    image: "/images/image 4.png",
    title: "Tips and Hints",
    to: '/information/Hints and Tips'
  },
  {
    id: 2,
    image: "/images/image 5.png",
    title: "Historical Facts",
    to: '/information/Historical Facts'
  },
  {
    id: 3,
    image: "/images/image 6.png",
    title: "Recipes",
    to: '/information/Coffee Recipes'
  },
  {
    id: 4,
    image: "/images/image 7.png",
    title: "Information",
    to: '/information/Interesting Coffee Facts'
  },
];
</script>

<template>
  <main>
    <!-- Navbar component -->
    <Navbar/>
    <!-- Container for cards -->
    <div class="container">
      <!-- Render each card component with data -->
      <Card v-for="card in cardsInfo" :key="card.id" :card-info="card" />
    </div>
  </main>
</template>

<style scoped>
.container {
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
