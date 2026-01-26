<script setup>
  import { useRouter, useRoute } from 'vue-router';
  import axios from 'axios';
  import { useUserInfoStore } from '../../stores/LoginStore';
  import { ref, onMounted, computed } from 'vue';
  import { storeToRefs } from 'pinia';


  // get login status
  const userInfoStore = useUserInfoStore();
  const { isLogin, isManager } = storeToRefs(userInfoStore);

  const router = useRouter();
  const route = useRoute();

  const boards = ref([]);

  // article
  const articleTitle = ref('');
  const articleContent = ref('');
  const selectedBoard = ref(route.query.board || '');
  const pinned = ref(false);
  // const btnEnabled = ref(false);

  const isTitleOrContentEmpty = computed(() => {
    // console.log(articleTitle.value.trim() !== '' && articleContent.value.trim() !== '')
    return articleTitle.value.trim() === '' || articleContent.value.trim() === '';
  })

  const submitArticle = async () => {
    if (!isTitleOrContentEmpty.value) {
      console.log(`is pinned: ${pinned.value}`);
      axios.post('/api/article/write', {
        article_board: selectedBoard.value,
        article_title: articleTitle.value,
        article_content: articleContent.value,
        pinned: pinned.value
      }).then(response => {
        router.replace(`/${selectedBoard.value}`);
      }).catch(error => {
        alert('發生未知錯誤');
        console.log(error);
      });
    } else {
      alert('標題或內容不得為空');
    }
  }
  
  // check login status and get boards and check if user is manager
  onMounted(async () => {
    if (!isLogin.value) {
      router.replace('/login');
    }

    const newBoards = await axios.get('/api/board/boards_info');
    boards.value = newBoards.data;
    selectedBoard.value = boards.value[0].board_eng;
  });

  // manager button colors
  const pinnedBtnColor = computed(() => {
    console.log(pinned.value)
    return pinned.value ? "#345e2e" : "#252525"
  });

</script>

<template>
  <label>標題 (限25字)</label>
  <div class="titleareaContainer">
    <input v-model="articleTitle" class="inputArea" placeholder="請在此輸入標題" maxlength="25" minlength="0"/>
  </div>

  <label>內容</label>
  <div class="contentareaContainer">
    <textarea v-model="articleContent" placeholder="請在此輸入內容" class="inputArea" rows="20"></textarea>
  </div>

  <label>討論版</label>
  <select v-model="selectedBoard" class="inputArea">
    <option v-for="board in boards" :value="board.board_eng">{{ board.board_zh }}</option>
  </select>

  <!-- manager options -->
  <label v-if="isManager">管理員選項</label>
  <div v-if="isManager" class="manager-options-container">
    <button class="manager-btn" @click="pinned=!pinned">置頂</button>
    <!-- <p v-if="isManager" class="manager-options-p">置頂</p> -->
    <!-- <input v-model="pinned" v-if="isManager" class="manager-options-checkbox" type="checkbox"> -->
  </div>

  <button
    :disabled="isTitleOrContentEmpty"
    :class="{'btnDisabled': isTitleOrContentEmpty, 'btnEnabled': !isTitleOrContentEmpty}"
    class="inputArea"
    @click="submitArticle()"
  >提交
  </button>

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
    /* color: rgb(236, 236, 236); */
    background: rgb(37, 37, 37);
    
    resize: none;
    font-size: 0.8rem;
    width: 100%;
    box-sizing: border-box;

    padding: 0.4rem 0.5rem;
    border-radius: 7px;
    border-color: transparent;

    margin-bottom: 1rem;

    outline: none;
  }

  .manager-btn {
    cursor: pointer;

    justify-self: start;
    align-self: start;
    background: v-bind(pinnedBtnColor);

    font-size: 0.7rem;
    margin-bottom: 0.5rem;
    margin-top: 0.5rem;
    margin-left: 0.5rem;
    padding: 5px 15px;
    width: max-content;
    height: max-content;

    transition: background 0.2s ease;
  }

  select {
    cursor: pointer;
    appearance: none;
  }

  .manager-options-container {
    display: grid;
    grid-template-columns: auto auto;
    width: 4rem;
  }

  .manager-options-p {
    /* display: inline; */
    justify-self: start;
    align-self: center;
    font-size: 0.8rem;
  }

  .manager-options-checkbox {
    /* background-color: rgb(37, 37, 37); */
    margin-left: 0.5rem;
    /* display: inline; */
    justify-self: start;
    align-self: center;
    height: 0.8rem;
    width: 0.8rem;
  }
</style>