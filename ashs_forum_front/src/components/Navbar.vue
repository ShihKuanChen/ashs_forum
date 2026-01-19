<script setup>
  import axios from 'axios';
  import { ref } from 'vue';
  import { useLoginStore } from '../../stores/LoginStore';
  import { storeToRefs } from 'pinia';
  import { useRouter } from 'vue-router';

  const router = useRouter();
  
  const loginStore = useLoginStore();
  const { isLogin } = storeToRefs(loginStore);
  const { checkLogin } = loginStore;

  async function logout() {
    await axios.post('/api/logout');
    await checkLogin();
    
    router.replace('/');
  }

</script>

<template>
  <nav class="navbar">
    <h2 class="web_title"><RouterLink to="/" class="web_title_text">高師大附中匿名板</RouterLink></h2>

    <ul class="nav-links">
        <li><RouterLink to="/boards" class="nav-link">討論板</RouterLink></li>
        <li><RouterLink to="/write" class="nav-link">投稿</RouterLink></li>
        <li><RouterLink to="/about" class="nav-link">關於</RouterLink></li>
        <li>
          <RouterLink v-if="!isLogin" to="/login" class="nav-link">登入</RouterLink>
          <a v-else class="nav-link" @click="logout()">登出</a>
        </li>
    </ul>
  </nav>
</template>

<style scoped>
  h2 {
    font-size: 1rem;
  }
  
  .navbar {
    background-color: rgb(24, 24, 24);
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #3b3b3b;
    position: fixed;
    /* width: 80%; */
    top: 0;
    left: 1.55rem;
    right: 1.55rem;
    /* margin-bottom: 20rem; */
  }

  .nav-links {
    font-weight: 300;
    color: rgb(236, 236, 236);
    text-decoration: none;
    list-style: none;
    display: flex;
    padding-left: 0;
  }

  .nav-links li {
    font-size: 0.7rem;
    display: flex;
    align-items: center;
    margin-left: 1rem;
    cursor: pointer;
  }

  .nav-links .nav-link {
    font-weight: 300;
    color: rgb(236, 236, 236);
    text-decoration: none;
  }

  .web_title {
    display: flex;
    align-items: center;
  }

  .web_title_text {   
    color: rgb(236, 236, 236);
    text-decoration: none;
    /* margin-left: 1rem; */
  }
</style>