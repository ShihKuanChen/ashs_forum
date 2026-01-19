<script setup>
  import axios from 'axios';
  import { useRoute, useRouter } from 'vue-router';
  import { computed, ref } from 'vue';
  
  // get title, content here

  const route = useRoute();
  const router = useRouter();
  const article_id = route.params.id;

  // var article_title;
  // var article_content;
  // var article_upload_time;


  // get article 
  const article_title = ref('');
  const article_content = ref('');
  const article_upload_time = ref('');

  axios.get(`/api/article/${article_id}`)
  .then(response => {
    article_title.value = response.data.article_title;
    article_content.value = response.data.article_content;
    article_upload_time.value = response.data.article_upload_time;
    console.log(response.data);
  })
  .catch(error => {
      router.replace('/');
  });

  // get article comments

  const comments = ref([]);
  const getComments = async () => {
    axios.get(`/api/comments/${article_id}`)
    .then(response => {
      comments.value = response.data;
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    });
  }

  getComments();

  const isBtnDisabled = computed(() => {
    console.log(comment.value.trim() === '');
    return comment.value.trim() === '';
  })

  // user comment
  const comment = ref('');
  const submitComment = async () => {
    if (!isBtnDisabled.value) {
      axios.post('/api/write_comment', {
        article_id: article_id,
        comment_content: comment.value
      })
      .then(response => {
        getComments();
        comment.value = '';
      })
      .catch(error => {
        console.log(error);
      });
    } 
  }
</script>

<template>
  <div class="articleHead">
    <h1 class=articleTitle>{{ article_title }}</h1>
    <p class=articleUploadTime>{{ article_upload_time }}</p>
  </div>
  
  <p class=articleContent>{{ article_content }}</p>
  
  <hr/>
  <h1 class=commentTitle>留言區</h1>

  <div class="commentInputContainer">
    <textarea v-model="comment" class="commentInput inputArea" placeholder="請在此輸入留言" rows="5"/>
    <button
      :disabled="isBtnDisabled"
      :class="{'btnDisabled': isBtnDisabled, 'btnEnabled': !isBtnDisabled}"
      class="inputArea btn"
      @click="submitComment()" >送出
    </button>
  </div>

  <!-- add comments here -->
  <div class="commentsContainer" v-for="comment in comments" :key="comment.comment_id">
    <p class="commentContent">{{ comment.comment_content }}</p>
    <p class="commentUploadTime">{{ comment.comment_upload_time }}</p>
  </div>
</template>

<style scoped>
  hr {
    border: 0;
    border-top: 1px solid rgb(87, 87, 87);
  }

  .commentsContainer {
    grid-template-columns: auto auto;
    display: grid;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgb(87, 87, 87);
  }

  .commentContent {
    margin: 0;
    white-space: pre-wrap;
    justify-self: start;
    width: 98%;
    /* padding-left: 0.5rem; */
  }

  .commentUploadTime {
    margin: 0;
    justify-self: end;
  }

  /* comment */
  .commentTitle {
    font-size: 1.2rem;
    margin-bottom: 0;
  }

  .inputArea {
    /* color: rgb(236, 236, 236); */
    background: rgb(37, 37, 37);
    
    resize: none;
    font-size: 0.8rem;
    box-sizing: border-box;

    padding: 0.4rem 0.5rem;
    border-radius: 7px;
    border-color: transparent;

    margin-bottom: 1rem;

    outline: none;
  }

  .commentInputContainer {
    display: grid;
    /* align-items: center; */
    grid-template-columns: auto 3rem;
  }

  .commentInput {
    margin-top: 0.5rem;
    display: inline-block;

    justify-self: start;
    align-self: start;
    width: 98%;
  }

  .btn {
    /* cursor: pointer; */

    margin-top: 0.5rem;
    justify-self: end;
    align-self: start;
    width: 3rem;
  }

  /* article */
  .articleHead {
    display: grid;
  }

  .articleTitle {
    justify-self: start;
    align-self: start;
    margin-bottom: 0;
  }

  .articleUploadTime {
    justify-self: start;
    align-self: start;
    margin: 0;
    font-size: 0.9rem;
  }

  .articleContent {
    white-space: pre-wrap;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }
</style>