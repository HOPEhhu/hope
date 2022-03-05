<!--文章目录页，根据传递过来类别的不同，显示不同的文章-->
<template>
    <div id="dskill1">
        <p>{{$route.query.sort}}</p>
        <ul>
            <li v-for="m in filelist" :key="m.id"><!--显示文章目录-->
                <!--点击文章可跳转至文章详情页，并向详情页传递两个参数，文章类别和文章标题-->
                <router-link class="routerskill1" :to="{
                    path:'/detail',
                    query:{
                        sort:$route.query.sort,
                        name:m.name
        
                    }
        
                }" >
                {{m.name}}
                <!--将名字的后缀去掉
                {{m.name.split(".")[0]}}-->
            </router-link>
            </li>
        </ul>
    </div>


</template>

<script>
    import axios from 'axios'
    export default {
        name: "Skill",
        props: [],
        data() {
            return {
                filelist: []


            }
        },
        methods: {

        },

        mounted() {
            //获取文章目录
            var that = this;
            axios.get("http://124.71.219.191/api/sort", {
                params: {
                    "sort":that.$route.query.sort  //传递想要获取的文章的类别
                }
            })
                .then(function (value) {
                    console.log(value)
                    that.filelist = value.data.retlist;
                })
                .catch(function (reason) {
                    console.log(reason)

                })




        },

    };
</script>

<style scoped>
    #dskill1 {
        width: 1280px;
        

        margin: auto;
        
        position: absolute;

        background-color: rgb(240 241 245);
        background-image: linear-gradient(rgb(210 213 219) 1px, transparent 1px),
            linear-gradient(to right, rgb(210 213 219) 1px, rgb(240 241 245) 1px);
        background-size: 20px 20px;
    }

    p{
        font-size: 64px;
        margin: auto;
        color: rgb(193, 33, 31);
        text-align: center;
    }
    ul{
        width: 800px;
        margin: auto;
    }

    .routerskill1{
        font-size: 24px;
        line-height: 50px;
        text-decoration: none;
        color: black;
    }
</style>