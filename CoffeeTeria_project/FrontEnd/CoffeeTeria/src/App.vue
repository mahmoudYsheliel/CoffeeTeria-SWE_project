<script setup lang="ts">
import {  RouterView } from 'vue-router'
</script>

<template>
  <RouterView class="RouterView"/>
</template>

<style>
body,html{
  padding: 0;
  margin: 0;
  background-color: var(--primary);
  background-image: url("assets/hq1.jpg");
  background-size: cover;
  background-position: top 20% right 0%;
  width:  100%;
  height: 100vh;
}
h1 {
    font-size: 46px;
    line-height: 54px;
}
:root{
  --primary:#604227;
  --secondary:#FFEACE;
  --text:#2C2C2C;
  --accent1:#FFEACE;
  --accent2:#957255
}

</style>
