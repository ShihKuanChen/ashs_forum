import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";

export const useLoginStore = defineStore('login', () => {
    const isLogin = ref(false);

    async function checkLogin() {
        try { 
            const response = await axios.get('/api/is_logged_in');
            isLogin.value = response.data['is_logged_in'];

            // .then(response => {
            //     isLogin.value = response.body;
            // })
            // .catch(error => {
            //     // isLogin.value = false;
            // })
        } catch (error) {
            console.log(error);
        };
    }
    
    return {isLogin, checkLogin}; 
});