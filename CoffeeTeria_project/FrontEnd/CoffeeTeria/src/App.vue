<script setup lang="ts">
// Importing the RouterView component from vue-router
import { RouterView } from 'vue-router'
</script>

<template>
  <!-- Using the RouterView component to render the routes -->
  <RouterView class="RouterView"/>
</template>

<style>
/* Styling for the body and html */
body,html{
  padding: 0;
  margin: 0;
  background-color: var(--primary); /* Setting background color */
  background-image: url("/images/hq1.jpg"); /* Setting background image */
  background-size: cover; /* Covering the entire viewport */
  background-position: top 20% right 0%; /* Positioning the background image */
  width:  100%; /* Full width */
  height: 100vh; /* Full height */
}
/* Styling for h1 elements */
h1 {
    font-size: 46px;
    line-height: 54px;
}
/* Defining CSS variables */
:root{
  --primary:#604227; /* Primary color */
  --secondary:#FFEACE; /* Secondary color */
  --text:#2C2C2C; /* Text color */
  --accent1:#FFEACE; /* Accent color 1 */
  --accent2:#957255; /* Accent color 2 */
  --accent3:#F4C9A9; /* Accent color 3 */
}

</style>
