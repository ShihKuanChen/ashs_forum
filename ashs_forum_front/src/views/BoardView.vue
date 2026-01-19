<script setup>
  import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router';
  import { computed, onMounted, ref } from 'vue';
  import { useInfiniteScroll } from '@vueuse/core';
  import axios from 'axios';

  const route = useRoute();
  const router = useRouter();
  const articles = ref([]);
  const scrollContainer = ref(null);

  // get board 
  const board = route.params.board;
  const board_zh = ref('');

  onMounted(async () => {
    // get board chinese title
    const newBoardTitle = await axios.get(`/api/board_zh`, {
      params: {
        board: board
      }
    });

    board_zh.value = newBoardTitle.data['board_zh'];
  });

  // set InfiniteScroll
  const hasMore = ref(true);
  const lastArticleId = ref(-1);

  useInfiniteScroll(
    scrollContainer, 
    async () => {
      console.log(`loading`);
      // pause();
      // get article titles and upload time
      await axios.get(`/api`, {
        params: {
          limit: 30, 
          board: board, 
          last_id: lastArticleId.value // must change
        }}).then(response => {
          console.log(response.data);
          if (response.data.length === 0) {
            console.log('no more articles');
            hasMore.value = false;
            
          } else {
            articles.value.push(...response.data);
            lastArticleId.value = articles.value[articles.value.length - 1].article_id;
            console.log(lastArticleId.value);
          }
        }).catch(error => {
          console.log(error);
        });

    // articles.value.push(...newArticles);
    },
    {
      distance: 20,
      canLoadMore: () => hasMore.value,
    });
  
  // set board and reset articles when route change
  onBeforeRouteUpdate((to, from) => {
    board.value = to.params.board;
    articles.value = [];
    hasMore.value = true;
    lastArticleId.value = -1;
  });

  function routeToArticle(id) {
    router.push(`/article/${id}`);
  }


</script>

<template>
  <h1 class="board-title">{{ board_zh }}</h1>
  <div ref="scrollContainer" class="scrollContainer">
    <div v-for="article in articles" id="articles" :key="article.article_id" @click="routeToArticle(article.article_id)">
      <article :id=article.article_id>
        <p class="article-title"> {{ article.article_title }} </p>
        <p class="article-time"> {{ article.article_upload_time }} </p>
      </article>
    </div>
    <div class="noMoreContainer">
      <p class="noMore">沒有更多文章了</p>
    </div>
  </div>
</template>

<style scoped>
  .noMoreContainer {
    display: grid;
  }

  .noMore {
    margin-top: 1rem;
    justify-self: center;
    font-size: 0.7rem;
    color: rgb(161, 161, 161);
  }

  .board-title {
    /* font-size: 1.5rem; */
    /* margin-top: 0; */
    margin-bottom: 0.8rem;
    /* padding-bottom: 0.1rem; */
    /* border-bottom: 1px solid #3b3b3b; */
  }

  .article-title {
    /* white-space: pre-wrap; */
    justify-self: start;
    align-self: start;

    margin-top: 0.5rem;
    margin-bottom: 0;
    font-size: 1.1rem;
    font-weight: 600;
  }

  .article-time {
    justify-self: end;
    align-self: end;

    margin-top: 0;
    margin-bottom: 0.5rem;
    font-size: 0.8rem;
    /* font-weight: 600; */
  }

  .scrollContainer {
    height: 100%;
    overflow-y: auto;
  }

  article {
    display: grid;
    flex-direction: column;
    /* justify-content: center; */
    border-bottom: 1px solid #3b3b3b;
    cursor: pointer;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    /* align-items: center; */
  }

  
</style>