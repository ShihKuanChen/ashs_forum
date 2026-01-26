<script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';

  const router = useRouter();

  // const isManager = ref(false);

  const checkManager = async () => {
    const response = await axios.get('/api/auth/is_manager');
    return response.data.is_manager;
    // console.log(response.data);
  }

  onMounted(async () => {
    if (!await checkManager()) {
      router.replace('/');
    }
  });

  const inputValues = ref({
    create_board_eng: '',
    create_board_zh: '',
    rm_board_eng: '',
    article_id: '',
    ban_user_id: '',
    unban_user_id: ''
  });

  const createBoard = async () => {
    try {
      await axios.post('/api/manage/create_board', {
        board_eng: inputValues.value.create_board_eng,
        board_zh: inputValues.value.create_board_zh
      });
      alert('新增成功');
      inputValues.value.create_board_eng = '';
      inputValues.value.create_board_zh = '';
    } catch (error) {
      console.log(error);
      alert('新增失敗')
    }
  }

  const removeBoard = async () => {
    try {
      await axios.post('/api/manage/remove_board', {
        board_eng: inputValues.value.rm_board_eng
      });
      alert('刪除成功');
      inputValues.value.rm_board_eng = '';
    } catch (error) {
      console.log(error);
      alert(`刪除失敗`)
    }
  }

  const removeArticleAndComments = async () => {
    try {
      await axios.post('/api/manage/remove_article_and_comments', {
        article_id: inputValues.value.article_id
      });
      alert('刪除成功');
      inputValues.value.article_id = '';
    } catch (error) {
      console.log(error);
      alert(`刪除失敗`)
    }
  }

  const banUser = async () => {
    try {
      await axios.post('/api/manage/ban_user', {
        user_id: inputValues.value.ban_user_id
      });
      alert('封鎖成功');
      inputValues.value.ban_user_id = '';
    } catch (error) {
      console.log(error);
      alert(`封鎖失敗`)
    }
  }

  const unbanUser = async () => {
    try {
      await axios.post('/api/manage/unban_user', {
        user_id: inputValues.value.unban_user_id
      });
      alert('解除封鎖成功');
      inputValues.value.unban_user_id = '';
    } catch (error) {
      console.log(error);
      alert(`解除封鎖失敗`)
    }
  }


</script>

<template>
  <h1>管理員選項</h1>
  <label>新增討論版</label>
  <div class="inputArea">
    <input v-model="inputValues.create_board_eng" type="text" placeholder="請輸入英文板名"/>
    <input v-model="inputValues.create_board_zh" type="text" placeholder="請輸入中文板名"/>
    <button @click="createBoard()">新增</button>
  </div>
  <label>刪除討論版</label>
  <div class="inputArea">
    <input v-model="inputValues.rm_board_eng" type="text" placeholder="請輸入英文板名"/>
    <button @click="removeBoard()">刪除</button>
  </div>
  <label>刪除文章及留言區</label>
  <div class="inputArea">
    <input v-model="inputValues.article_id" type="text" placeholder="請輸入文章id"/>
    <button @click="removeArticleAndComments()">刪除</button>
  </div>
  <label>封鎖用戶</label>
  <div class="inputArea">
    <input v-model="inputValues.ban_user_id"  type="text" placeholder="請輸入用戶id"/>
    <button @click="banUser()">封鎖</button>
  </div>
  <label>解除封鎖</label>
  <div class="inputArea">
    <input v-model="inputValues.unban_user_id" type="text" placeholder="請輸入用戶id"/>
    <button @click="unbanUser()">解除</button>
  </div>
</template>

<style scoped>
  label {
    display: block;
    font-size: 0.8rem;
    font-weight: 500;
    margin-bottom: 0.2rem;
    margin-top: 0.1rem;
  }
  
  .inputArea {
    margin-bottom: 1rem;
  }
  /* button {
    background: rgb(37, 37, 37);
    color: rgb(236, 236, 236);
  } */
</style>