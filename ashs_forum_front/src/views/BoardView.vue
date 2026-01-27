<script setup>
  import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router';
  import { computed, onMounted, ref } from 'vue';
  import { useInfiniteScroll } from '@vueuse/core';
  import { useUserInfoStore } from '../../stores/LoginStore';
  import { storeToRefs } from 'pinia';
  import axios from 'axios';

  const route = useRoute();
  const router = useRouter();
  const scrollContainer = ref(null);

  // get board 
  const board = route.params.board;
  const board_zh = ref('');

  // manager status
  const userInfoStore = useUserInfoStore();
  const { isManager } = storeToRefs(userInfoStore);

  onMounted(async () => {
    // get board chinese title
    try {
      const newBoardTitle = await axios.get(`/api/board/board_zh`, {
        params: {
          board: board
        }
      });
      board_zh.value = newBoardTitle.data['board_zh'];
    } catch (error) {
      console.log(error);
      router.replace('/');
    }
  });

  // set InfiniteScroll
  const hasMore = ref(true);
  const lastArticleId = ref(-1);
  const articles = ref([]);

  useInfiniteScroll(
    scrollContainer, 
    async () => {
      console.log(`loading`);
      // pause();
      // get article titles and upload time
      await axios.get(`/api/article/articles_info`, {
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

  const removeArticleAndComments = async (article_id) => {
    try {
      // router.replace(`/${board.value}`);
      await axios.post('/api/manage/remove_article_and_comments', {
        article_id: article_id
      });
      hasMore.value = true;
      articles.value = [];
      lastArticleId.value = -1;
      alert('刪除成功');
      // console.log(`board: ${board.value}`);
      
    } catch (error) {
      console.log(error);
      alert(`刪除失敗`);
    }
  }

</script>

<template>
  <h1 class="board-title">{{ board_zh }}</h1>
  <!-- <router-link class="write-link" :to="{path: '/write', query: {board: board}}">我要投稿</router-link> -->
  <div ref="scrollContainer" class="scrollContainer">
    <div v-for="article in articles" id="articles" :key="article.article_id" @click="routeToArticle(article.article_id)">
      <article :id=article.article_id>
        <p class="article-title"> {{ article.article_title }} </p>
        <button v-if="isManager" @click.stop="handler" @click="removeArticleAndComments(article.article_id)" class="manager-btn">刪除</button>
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
    /* grid-column: span 2; */
    justify-self: start;
    align-self: start;

    margin-top: 0.5rem;
    margin-bottom: 0;
    font-size: 1.1rem;
    font-weight: 600;
  }

  .article-time {
    grid-column: span 2;
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

  .manager-btn {
    cursor: pointer;

    justify-self: end;
    align-self: end;
    background: rgb(94, 46, 46);

    font-size: 0.6rem;
    margin-bottom: 0.5rem;
    margin-top: 0.5rem;
    margin-left: 0.5rem;
    padding: 5px 10px;
    width: max-content;
    height: max-content;
  }

  article {
    display: grid;
    flex-direction: column;
    grid-template-columns: auto max-content;
    /* justify-content: center; */
    border-bottom: 1px solid #3b3b3b;
    cursor: pointer;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    /* align-items: center; */
  }

  
</style>