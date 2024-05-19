// Importing necessary functions and libraries from Vue, Pinia, PrimeVue, App.vue file, and router
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primeicons/primeicons.css'
import App from './App.vue'
import router from './router'

// Creating the Vue application instance
const app = createApp(App)

// Adding PrimeVue plugin to the Vue application
app.use(PrimeVue);

// Adding Pinia plugin to the Vue application for state management
app.use(createPinia())

// Adding router plugin to the Vue application for routing
app.use(router)

// Mounting the Vue application to the DOM element with the id 'app'
app.mount('#app')
