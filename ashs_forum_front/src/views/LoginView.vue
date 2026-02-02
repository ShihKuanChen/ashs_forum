<script setup>
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import { useUserInfoStore } from '../../stores/LoginStore';

  const router = useRouter();
  const userInfoStore = useUserInfoStore();
  const { updateUserInfo } = userInfoStore;

  console.log("Client id:")
  console.log(import.meta.env.VITE_GOOGLE_CLIENT_ID)


  const callback = async (response) => {
    console.log(response);

    // call login api
    await axios.post('/api/auth/login', {
      token: response['credential']
    }).then(response => {
      router.replace('/');
    }).catch(error => {
      console.log(error);
    });

    // update login status
    updateUserInfo();
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
    color: #3c4043;
  
    display: flex;
    justify-content: center;
  }
</style>