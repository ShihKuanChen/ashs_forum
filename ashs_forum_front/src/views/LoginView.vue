<script setup>
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import { useLoginStore } from '../../stores/LoginStore';

  const router = useRouter();
  const loginStore = useLoginStore();
  const { checkLogin } = loginStore;


  const callback = async (response) => {
    console.log(response);

    // call login api
    await axios.post('/api/login', {
      token: response['credential']
    }).then(response => {
      router.replace('/');
    }).catch(error => {
      console.log(error);
    });

    // update login status
    checkLogin();
  }
</script>

<template>
  <h1>登入</h1>
  <p>請使用以下方式登入</p>
  <div class="google_login_container">
    <GoogleLogin :callback="callback"/>
  </div>
</template>

<style scoped>
  h1 {
    display: flex;
    justify-content: center;
  }

  p {
    display: flex;
    justify-content: center;
  }

  .google_login_container {
    display: flex;
    justify-content: center;
  }
</style>