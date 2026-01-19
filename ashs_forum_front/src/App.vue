<script setup>
  import {RouterView} from 'vue-router'
  import Navbar from './components/Navbar.vue'
  import { useLoginStore } from '../stores/LoginStore';

  const loginStore = useLoginStore();
  const { checkLogin } = loginStore;

  checkLogin();
</script>

<template>
  <header>
    <Navbar />
  </header>
  
  <div class="app-container">
    <main>
      <RouterView />
    </main>
  </div>
</template>

<style>
  :root {
    color: rgb(236, 236, 236);
    background-color:rgb(24, 24, 24);
    
    /* font setting */
    font-size: clamp(8px, 4vw, 24px);
    
    font-optical-sizing: auto;
    /* font-weight: <weight>; */
    font-style: normal;
  }

  * {
    font-family: "Chiron Hei HK", sans-serif;
    
  }

  button, input {
    background: rgb(37, 37, 37);
    color: rgb(236, 236, 236);
    border: 0;
    margin-right: 1rem;
    border-radius: 5px;
    font-size: 0.8rem;
    padding: 0.4rem 0.5rem;
  }

  .btnDisabled {
    color: rgb(80, 80, 80);
    cursor: default;
  }

  .btnEnabled {
    /* color: rgb(80, 80, 80); */
    cursor: pointer;
  }
  
</style>

<style scoped>
  .app-container {
    padding: 3rem 1.2rem 3rem 1.2rem;
  }

  h1 {
    font-size: 1.5rem;
  }

  h2 {
    font-size: 1rem;
  }

</style>
