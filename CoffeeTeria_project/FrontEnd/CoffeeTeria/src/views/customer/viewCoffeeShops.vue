<script lang="ts" setup>
import { ref } from "vue";
import axios from "axios";


import Navbar from "@/components/homePage/Navbar.vue";
import CoffeeCard from "@/components/coffeeShops/CoffeeCard.vue";
const shops = ref();
axios
  .post("http://127.0.0.1:8000/get_all_coffee_shops", {}, {})
  .then((res: any) => {
    shops.value = res.data.data.coffee_shop;
    console.log(shops);
  });


</script>

<template>
  <main>
    <Navbar />
    <div class="container">
        <CoffeeCard v-for="shop in shops" :shop="shop"/>
    </div>
  </main>
</template>

<style scoped>
.container {
  padding-top: 5rem;
  padding-inline: 20%;
  margin-inline: auto;
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  align-items: center;
}
</style>
