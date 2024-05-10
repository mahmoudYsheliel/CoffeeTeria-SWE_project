<script lang="ts" setup>
import Button from "primevue/button";
defineProps(["shop"]);
import { useRouter } from "vue-router";
const router =useRouter()
</script>

<template>
  <main>
    <div class="container">
      <img :src="shop.image" alt="" />
      <h2>{{ shop.name }}</h2>
      <h3>Location:</h3>
      <p>{{ shop.city_name }} {{ shop.location }}</p>
      <h3>Contact:</h3>
      <p>{{ shop.contact_number }}</p>
      <h3>Work Time:</h3>
      <p>{{ shop.open_time }}:00 - {{ shop.close_time }}:00</p>
      <div class="button"><Button label="orderNow" @click="router.push(`/products/${shop.id}`)"/></div>
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
img {
  width: 100%;
  aspect-ratio: 1.625/1;
}
h2 {
  text-transform: capitalize;
  margin-left: 2rem;
  padding-block: 0;
  margin-block: 0.5rem;
}

h3,
p {
  padding-left: 1rem;
  padding-block: 0;
  margin-block: 0rem;
}
h3 {
  margin-top: 1rem;
}
p{
    margin-left: 2rem;
}
.button {
    margin-top: 2rem;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
