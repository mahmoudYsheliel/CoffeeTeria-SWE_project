<script setup lang="ts">
import Button from "primevue/button";
import axios from "axios";
import { ref } from "vue";

import { useCart } from "@/stores/counter";
const cart = useCart();

const prop = defineProps(["id"]);
const product = ref();

axios.post("/get_product", { product_id: prop.id }, {}).then((res: any) => {
  product.value = res.data.data.product;
});
</script>

<template>
  <main>
    <div class="container">
      <img :src="product?.image" alt="" />
      <div class="element">
        <h4>{{ product?.name }}</h4>
        <h4>{{ product?.price }}</h4>
      </div>
      <p>{{ product?.description }}</p>
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
