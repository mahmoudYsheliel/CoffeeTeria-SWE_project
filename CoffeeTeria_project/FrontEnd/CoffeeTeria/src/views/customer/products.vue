<script lang="ts" setup>
import Navbar from "@/components/homePage/Navbar.vue";
import Button from "primevue/button";
import Product from "@/components/product/Product.vue";
import axios from "axios";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";

// Initializing variables and hooks
const shop = ref();
const route = useRoute();
const router = useRouter();

// Fetching coffee shop data from the backend
axios
  .post("/get_coffee_shop", { coffee_shop_id: route.params.shopId }, {})
  .then((res: any) => {
    shop.value = res.data.data.coffee_shop;
    console.log(shop);
  });
</script>

<template>
  <main>
    <!-- Navbar component -->
    <Navbar />
    <div class="container">
      <!-- Rendering products component for each product in the shop -->
      <Product v-for="product in shop?.products" :id="product" />
    </div>
    <!-- Button to navigate to view cart -->
    <Button
      label="View Cart"
      @click="router.push(`/cart/${route.params.shopId}`)"
    />
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

button {
  position: relative;
  margin-top: 2rem;
  left: 90%;
}
</style>
</html>
