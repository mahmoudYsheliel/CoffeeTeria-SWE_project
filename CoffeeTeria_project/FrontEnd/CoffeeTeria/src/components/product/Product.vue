<script setup lang="ts">
// Importing necessary components and utilities
import Button from "primevue/button";
import axios from "axios";
import { ref, defineProps } from "vue";

// Importing store for managing cart
import { useCart } from "@/stores/counter";

// Defining props for the component
const prop = defineProps(["id"]);

// Creating a reference for the product data
const product = ref();

// Accessing cart store
const cart = useCart();

// Fetching product data from the server
axios.post("/get_product", { product_id: prop.id }, {}).then((res: any) => {
  product.value = res.data.data.product;
});
</script>

<template>
  <main>
    <div class="container">
      <!-- Displaying product image -->
      <img :src="product?.image" alt="" />

      <div class="element">
        <!-- Displaying product name and price -->
        <h4>{{ product?.name }}</h4>
        <h4>{{ product?.price }}</h4>
      </div>

      <!-- Displaying product description -->
      <p>{{ product?.description }}</p>

      <!-- Button for adding product to cart -->
      <div class="button">
        <Button
          label="Add to Cart"
          @click="
            () => {
              cart.addProduct(product?.id);
            }
          "
        />
      </div>
    </div>
  </main>
</template>

<style scoped>
.container {
  color: var(--text);
  width: 15rem;
  height: 30rem;
  background-color: var(--accent1);
  border-radius: 8px;
  overflow: hidden;
}

.element {
  display: flex;
  width: 80%;
  margin-inline: auto;
  justify-content: space-between;
}

img {
  width: 100%;
  aspect-ratio: 1.625/1;
}

p {
  padding-left: 1rem;
  padding-block: 0;
  margin-block: 0rem;
}

.button {
  margin-top: 2rem;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
