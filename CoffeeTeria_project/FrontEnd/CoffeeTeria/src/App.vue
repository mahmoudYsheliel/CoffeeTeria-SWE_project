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
  background-color: var(--primary)
}
:root{
  --primary:#604227;
  --secondary:#00C9AD;
  --text:#2C2C2C;
  --accent1:#FFEACE;
  --accent2:#957255
}

</style>
