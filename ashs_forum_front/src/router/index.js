import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import BoardView from '@/views/BoardView.vue'
import LoginView from '@/views/LoginView.vue'
import ArticleView from '@/views/ArticleView.vue'
import BoardsView from '@/views/BoardsView.vue'
import axios from 'axios'
import WriteView from '@/views/WriteView.vue'
import { useLoginStore } from '../../stores/LoginStore'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [{
    path: '/',
    name: 'home',
    component: HomeView
  }, {
    path: '/about',
    name: 'about',
    component: AboutView
  }, {
    path: '/login',
    name: 'login',
    component: LoginView
  }, {
    path: '/logout',
    name: 'logout',
    beforeEnter: (to, from) => {
      console.log('logout');
      const loginStore = useLoginStore();
      const { checkLogin } = loginStore;

      axios.post('/api/logout');
      
      checkLogin();
    },
    redirect: '/'
  }, {
    path: '/boards',
    name: 'boards',
    component: BoardsView
  }, {
    path: '/:board',
    name: 'board',
    component: BoardView
  }, {
    path: '/article/:id',
    name: 'article',
    component: ArticleView
  }, {
    path: '/write',
    name: 'write',
    component: WriteView
  }, , { 
    path: '/:pathMatch(.*)*', 
    redirect: '/' 
  }],
})

export default router
