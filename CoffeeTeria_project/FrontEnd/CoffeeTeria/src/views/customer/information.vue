<script setup lang="ts">
import Navbar from "@/components/homePage/Navbar.vue";
import { useRoute } from "vue-router";
import { ref } from "vue";
import Accordion from "primevue/accordion";
import AccordionTab from "primevue/accordiontab";
import axios from "axios";
const route = useRoute();
const information = ref<any[]>();
axios.post("/get_information", {}, {}).then((res) => {
  let infos = [];
  for (const info of res.data.data.information) {
    if (info.type == route.params.type) {
      infos.push({ title: info.title, description: info.description });
    }
  }
  information.value = infos;
  console.log(infos);
});
</script>

<template>
  <Navbar />
  <div class="container">
    <h1 style="color: var(--secondary)">{{ route.params.type }}</h1>
    <Accordion class="con" :activeIndex="-1">
      <AccordionTab
        v-for="info in information"
        class="title"
        :header="info.title"
        :pt="{
          headerAction: {
            style: {
              'background-color': 'var(--accent1)',
            },
          },
          content: {
            style: {
              'background-color': 'var(--accent3)',
              'padding-top': '0.5rem',
            },
          },
        }"
      >
        <p class="m-0 description">
          {{ info.description }}
        </p>
      </AccordionTab>
    </Accordion>
  </div>
</template>

<style scoped>
.container {
  margin-top: 10vh;
  width: 80%;
  margin-inline: auto;
}
.con {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.description {
  margin: 4px;
  border-radius: 8px;
  overflow: hidden;
}
</style>
