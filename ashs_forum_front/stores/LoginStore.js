import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";


export const useUserInfoStore = defineStore('userInfo', () => {
    const isLogin = ref(false);
    const isBanned = ref(false);
    const isManager = ref(false);

    async function updateUserInfo() {
        try {
            // 
            const response = await axios.get('/api/auth/get_user_info');
            const userInfo = response.data.data;
            isLogin.value = userInfo.is_login;

            // console.log(userInfo);

            if (isLogin.value === true) {
                isBanned.value = userInfo.is_banned;
                isManager.value = userInfo.is_manager;
            }
        } catch (error) {
            console.log(error);
        };
    }
    
    return {isLogin, isBanned, isManager, updateUserInfo}; 
}, {persist: true});