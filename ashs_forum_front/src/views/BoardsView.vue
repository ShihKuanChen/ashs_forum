<script setup>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';

  const router = useRouter();
  
  const boards = ref([]);

  onMounted(async () => {
    const newBoards = await axios.get('/api/boards');
    // console.log(boards.data);
    boards.value = newBoards.data;
  });

  function routeToBoard(board) {
    router.push(`/${board}`);
  }
</script>


<template>
  <div v-for="board in boards" id="articles" :key="board.board_id" @click="routeToBoard(board.board_eng)">
    <div class="boardCard">
      <p class="board-title">{{ board.board_zh }}</p>
      <p class="board-count">共{{ board.board_n_articles }}篇文章</p>
      <p class="board-update_time">上次更新: {{ board.board_last_time === null ? '無' : board.board_last_time}}</p>
      <!-- <p class="article-time"> {{ board.article_upload_time }} </p> -->
    </div>
  </div>
</template>

<style scoped>
  p {
    margin: 0;
  }

  .boardCard {
    border-radius: 10px;
    background-color:rgb(37, 37, 37);
    /* border: 1px solid #3b3b3b; */
    padding: 0.5rem 0.6rem;
    cursor: pointer;
    margin-bottom: 0.2rem;
    display: grid;
    /* justify-content: space-between; */

  }

  .board-title {
    margin: 0rem;
    font-weight: 700;
    font-size: 1.2rem;
    justify-self: start;
    align-self: start;
  }

  .board-count {
    /* margin-top: 0.5rem; */
    /* font-weight: 700; */
    font-size: 0.7rem;
    justify-self: start;
    align-self: start;
  }

  .board-update_time {
    /* margin-top: 0.5rem; */
    /* font-weight: 700; */
    font-size: 0.7rem;
    justify-self: end;
    align-self: end;
  }
</style>