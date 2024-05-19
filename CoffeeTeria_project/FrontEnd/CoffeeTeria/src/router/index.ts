import { createRouter, createWebHistory } from 'vue-router'

// Importing views
import homePage from '../views/customer/homePage.vue'
import login from '../views/customer/login.vue'
import signup from '../views/customer/signup.vue'
import viewCoffeeShops from '../views/customer/viewCoffeeShops.vue'
import products from '../views/customer/products.vue'
import ViewCart from '@/views/customer/ViewCart.vue'
import information from '@/views/customer/information.vue'

// Creating router instance
const router = createRouter({
  // Using web history mode
  history: createWebHistory(import.meta.env.BASE_URL),
  // Defining routes
  routes: [
    {
      path: '/',
      name: 'home',
      component: homePage // Home page route
    },
    {
      path: '/login',
      name: 'login',
      component: login // Login page route
    },
    {
      path: '/signup',
      name: 'signup',
      component: signup // Signup page route
    },
    {
      path: '/viewCoffeeShops',
      name: 'viewCoffeeShops',
      component: viewCoffeeShops // View coffee shops route
    },
    {
      path: '/products/:shopId',
      name: 'products',
      component: products // Products page route
    },
    {
      path: '/cart/:shopId',
      name: 'cart',
      component: ViewCart // View cart route
    },
    {
      path: '/information/:type',
      name: 'information',
      component: information // Information page route
    },
  ]
})

export default router
