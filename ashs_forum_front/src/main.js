import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import vue3GoogleLogin from 'vue3-google-login'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const app = createApp(App)
const pinia = createPinia();

pinia.use(piniaPluginPersistedstate);

app.use(router)
app.use(pinia)
app.use(vue3GoogleLogin, {
  clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID,
  idConfiguration: {
    hosted_domain: 'stu.nknush.kh.edu.tw'
  },
  buttonConfig: {
    // locale: "zh_TW",
    shape: 'pill',
    // theme: 'filled_black',
    // width: "300"
  }
})

app.mount('#app')

