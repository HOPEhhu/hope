<!--目录页的专业技能目录-->
<template>
    <div id="ds1">
        <p id="ps1">2</p>
        <p id="ps2">专业技能</p>
        <!--跳转到文章目录，sort为传递参数，代表文章的类别-->
        <router-link class="ps3" :to="{
            path:'/skill',   
            query:{
                sort:'cv'
            }
        }" >
            机器学习
        </router-link><br>
        <router-link class="ps3" :to="{
            path:'/skill',
            query:{
                sort:'Python'

            }

        }" >
        Python
        </router-link><br>

        <router-link class="ps3" :to="{
            path:'/skill',
            query:{
                sort:'hardware'

            }

        }" >
        硬件
        </router-link><br>

        <router-link class="ps3" :to="{
            path:'/skill',
            query:{
                sort:'web'

            }

        }" >
        Web
        </router-link><br>
        





    </div>
</template>skill

<script>
    export default {
        name: "Skill1",
        methods: {

        },

    };
</script>

<style scoped>
    #ds1 {
        width: 220px;
        height: 170px;



    }

    #ps1 {
        color: rgb(193, 33, 31);
        font-size: 36px;
        margin: 0%;
    }

    #ps2 {
        color: rgb(193, 33, 31);
        font-size: 24px;
        margin: 0%;
        line-height: 40px;
        font-weight: 600;
    }

    .ps3 {
        font-size: 20px;
        line-height: 30px;
        text-decoration: none;
        color: black;
    }
</style>