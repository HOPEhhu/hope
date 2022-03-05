<template>
    <div id="dh1">
        <p id="ph1">4</p>
        <p id="ph2">个人爱好</p>
        <p>
            <router-link to="/booklist" class="rhobby1">书单</router-link>
        </p>
        <p>
            <router-link to="/excerptlist" class="rhobby1">摘录</router-link>
        </p>

        <p>
            <router-link class="rhobby1" :to="{
            path:'/skill',
            query:{
                sort:'writing'

            }

        }">
                随笔
            </router-link>
        </p>

        <p class="ph3">收藏</p>




    </div>
</template>

<script>
    export default {
        name: "Hobby",
        methods: {

        },

    };
</script>

<style scoped>
    #dh1 {
        width: 220px;
        height: 170px;



    }

    #ph1 {
        color: rgb(193, 33, 31);
        font-size: 36px;
        margin: 0%;
    }

    #ph2 {
        color: rgb(193, 33, 31);
        font-size: 24px;
        margin: 0%;
        line-height: 40px;
        font-weight: 600;
    }

    .ph3 {
        font-size: 20px;
        line-height: 12px;
    }

    .rhobby1 {
        font-size: 20px;
        line-height: 12px;
        text-decoration: none;
        color: black;
    }
</style>