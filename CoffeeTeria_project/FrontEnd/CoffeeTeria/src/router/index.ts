import { createRouter, createWebHistory } from 'vue-router'
import homePage from '../views/customer/homePage.vue'
import login from '../views/customer/login.vue'
import signup from '../views/customer/signup.vue'
import viewCoffeeShops from'../views/customer/viewCoffeeShops.vue'
import products from '../views/customer/products.vue'
import ViewCart from '@/views/customer/ViewCart.vue'
import information from '@/views/customer/information.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: homePage
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/signup',
      name: 'signup',
      component: signup
    },
    {
      path: '/viewCoffeeShops',
      name: 'viewCoffeeShops',
      component: viewCoffeeShops
    },
    {
      path: '/products/:shopId',
      name: 'products',
      component: products
    },
    {
      path: '/cart/:shopId',
      name: 'cart',
      component: ViewCart
    },
    {
      path: '/information/:type',
      name: 'information',
      component: information
    },
  
  ]
})

export default router
