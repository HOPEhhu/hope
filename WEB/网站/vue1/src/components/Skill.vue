<!--文章目录页，根据传递过来类别的不同，显示不同的文章-->
<template>
    <div id="dskill1">
        <p>{{$route.query.sort}}</p>
        <ul>
            <li v-for="m in filelists" :key="m.id">
                <!--显示文章目录-->
                <!--点击文章可跳转至文章详情页，并向详情页传递两个参数，文章类别和文章标题-->
                <router-link class="routerskill1" :to="{
                    path:'/detail',
                    query:{
                        sort:$route.query.sort,
                        name:m.name
        
                    }
        
                }">

                    <!--将名字的后缀去掉-->
                    {{m.name.split(".")[0]}}
                </router-link>
            </li>
        </ul>
        <el-pagination class="filelist1" layout="prev, pager, next" :total="filelistss.length" :page-size="12"
            @current-change="handleCurrentChange">
        </el-pagination>
    </div>


</template>

<script>
    import axios from 'axios'
    export default {
        name: "Skill",
        props: [],
        data() {
            return {
                filelistss: [],
                filelists: [],
                currentval:1,


            }
        },
        methods: {
            handleCurrentChange(val) {
                this.filelists = this.filelistss.slice((val - 1) * 12, val * 12);
                this.currentval=val
            },
        },

        mounted() {
            //获取文章目录
            var that = this;
            axios.get(window.a + "/api/sort", {
                params: {
                    "sort": that.$route.query.sort  //传递想要获取的文章的类别
                }
            })
                .then(function (value) {
                    console.log(value)
                    that.filelistss = value.data.retlist;
                    that.filelists = that.filelistss.slice(0, 12)
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
        height: 720px;


        margin: auto;

        position: absolute;

        background-color: rgb(240 241 245);
        background-image: linear-gradient(rgb(210 213 219) 1px, transparent 1px),
            linear-gradient(to right, rgb(210 213 219) 1px, rgb(240 241 245) 1px);
        background-size: 20px 20px;
    }

    p {
        font-size: 64px;
        margin: auto;
        color: rgb(193, 33, 31);
        text-align: center;
    }

    ul {
        width: 800px;
        margin: auto;
    }

    .routerskill1 {
        font-size: 24px;
        line-height: 45px;
        text-decoration: none;
        color: black;
    }

    /*翻页*/
    .filelist1{
        position: absolute;
        top: 625px;
        left: 260px;
    }
</style>