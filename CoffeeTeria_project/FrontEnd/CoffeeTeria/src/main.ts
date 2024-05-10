
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primeicons/primeicons.css'
import App from './App.vue'
import router from './router'



const app = createApp(App)

app.use(PrimeVue);
app.use(createPinia())
app.use(router)

app.mount('#app')
