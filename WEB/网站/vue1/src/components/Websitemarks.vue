<template>

    <div id="dexcerpt1">
        <p id="wp1">常用网站</p>
        <p id="wp2">收藏夹</p>


        <table id="wtable1">
            <tr>
                <td><a href="http://www.baidu.com/" target="_blank">百度</a></td>
                <td><a href="https://www.csdn.net/" target="_blank">CSDN</a></td>
                <td><a href="http://i.chaoxing.com/" target="_blank">学习通</a></td>
                <td><a href="https://translate.google.cn/" target="_blank">谷歌翻译</a></td>
            </tr>
            <tr>
                <td><a href="http://www.bing.com/" target="_blank">必应</a></td>
                <td><a href="https://www.bilibili.com/" target="_blank">bilibili</a></td>
                <td><a href="https://www.amazon.cn/" target="_blank">亚马逊</a></td>
                <td><a href="https://yjss.hhu.edu.cn/home/stulogin" target="_blank">教学管理</a></td>
            </tr>
            <tr>
                <td><a href="https://www.zhihu.com" target="_blank">知乎</a></td>
                <td><a href="https://github.com/" target="_blank">GitHub</a></td>
                <td><a href="https://account.aliyun.com/" target="_blank">阿里云</a></td>
                <td><a href="https://mail.hhu.edu.cn/" target="_blank">河海邮箱</a></td>
            </tr>
            <tr>
                <td><a href="https://tieba.baidu.com/index.html" target="_blank">贴吧</a></td>
                <td><a href=" https://codepen.io/trending" target="_blank">Codepen</a></td>
                <td><a href="https://auth.huaweicloud.com/" target="_blank">华为云</a></td>
                <td><a href="https://weread.qq.com/" target="_blank">微信读书</a></td>
            </tr>
            <tr>
                <td><a href="https://huaban.com/home/" target="_blank">花瓣</a></td>
                <td><a href="https://www.xiwang.online/" target="_blank">HOPE</a></td>
                <td><a href="https://cloud.tencent.com/" target="_blank">腾讯云</a></td>
                <td><a href="http://kgbook.com/" target="_blank">苦瓜书盘</a></td>
            </tr>
            <tr>
                <td><a href="https://www.zcool.com.cn/" target="_blank">站酷</a></td>
                <td><a href="https://www.google.com/" target="_blank">Google</a></td>
                <td><a href="https://www.bfg-notice.top/" target="_blank">避风港</a></td>
                <td><a href="https://www.jiumodiary.com/" target="_blank">鸠摩搜索</a></td>
            </tr>
            <tr>
                <td><a href="https://mail.qq.com/" target="_blank">邮箱</a></td>
                <td><a href="https://minecraft.fandom.com/zh/wiki/Minecraft_Wiki" target="_blank">Minecraft</a></td>
                <td><a href="https://www.allhistory.com/" target="_blank">全历史</a></td>
                <td><a href="https://book.douban.com/" target="_blank">豆瓣读书</a></td>
            </tr>


        </table>
        <!--竖线-->
        <div class="sx"></div>

        <table id="wtable2">
            <Webmarkitem v-for="web in webs" :key="web.id" :web="web" :deleteweb="deleteweb" />
        </table>

        <!--翻页-->
        <el-pagination class="weblist1" layout="prev, pager, next" :total="webss.length" :page-size="10"
            @current-change="handleCurrentChange">
        </el-pagination>



        <p id="pexcerpt1">添加：</p>
        <div id="dweb1">
            网站：<input type="text" v-model="webname" />
            网址：<input type="text" v-model="weburl" @keyup.enter="add" />
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import Webmarkitem from "./excerpt/Webmarkitem.vue";
    export default {
        name: "Websitemarks",
        components: { Webmarkitem },
        props: [],
        data() {
            return {
                webss: [],
                webs:[],
                webname: '',
                weburl: '',
                currentval:1,

            }
        },
        computed: {

        },

        mounted() {
            var that = this;
            axios.get(window.a + "/api/web", {
                params: {
                    "action": "list_web",
                }
            })
                .then(function (value) {
                    console.log(value)
                    that.webss = value.data.retlist;
                    that.webs = that.webss.slice(0, 10)


                })
                .catch(function (reason) {
                    console.log(reason)

                })




        },


        methods: {
            handleCurrentChange(val) {
                this.webs = this.webss.slice((val - 1) * 10, val * 10);
                this.currentval=val
            },


            //添加
            add() {
                var that = this;
                axios.post(window.a + "/api/web", {
                    "action": "add_web",
                    "data": {
                        "webname": that.webname,
                        "weburl": that.weburl,
                    }
                })
                    .then(function (response) {
                        if (response.data.ret == 0) {
                            const todoObj = { id: response.data.id, webname: that.webname, weburl: that.weburl };
                            that.webss.push(todoObj);
                            that.webs = that.webss.slice((that.currentval - 1) * 10, that.currentval * 10);
                            that.webname = "";
                            that.weburl = "";
                            console.log(response.data.id)
                        } else if (response.data.ret == 302) {
                            alert("未登录")
                            that.$router.push("signin");
                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },

//此处有bug:删除只是将webs和数据库中的内容删除了，webss中的内容没有删除，所以如果删除之后立即添加内容，那么之前删除的内容也会在屏幕上显示

            //删除
            deleteweb(id) {
                this.webs = this.webs.filter((web) => {
                    axios.post(window.a + "/api/web", {
                        "action": "del_web",
                        "data": {
                            "id": id,
                        }
                    })
                        .then(function (response) {
                            if (response.data.ret == 0) {
                                console.log(response.data.ret)
                            } else if (response.data.ret == 302) {
                                alert("未登录")
                                this.$router.push("signin");
                            }
                        })
                        .catch(function (error) {
                            console.log(error);
                        });
                    return web.id != id

                })
            },

        },
    };
</script>

<style scoped>
    #dexcerpt1 {
        width: 1280px;
        height: 720px;
        background-color: rgb(240 241 245);
        background-image: linear-gradient(rgb(210 213 219) 1px, transparent 1px), linear-gradient(to right, rgb(210 213 219) 1px, rgb(240 241 245) 1px);
        background-size: 20px 20px;
        margin: auto;
        box-shadow: 5px 5px 5px -2px rgba(0, 0, 0, 0.3);
        position: relative;
    }

    textarea {
        width: 800px;
        height: 80px;
        border: none;
        border-bottom: 2px solid black;
        background-color: inherit;
        font-family: "汇文明朝体", "SimSun";
        font-size: 20px;
        position: absolute;
        top: 620px;
        left: 220px;
    }

    /*添加*/
    #pexcerpt1 {    
        font-size: 24px;
        position: absolute;
        top: 600px;
        left: 666px;
    }

    /*左面表*/
    #wtable1 {
        position: absolute;
        width: 500px;
        text-align: center;
        left: 120px;
        top: 80px;
    }

    a {
        font-size: 32px;
        color: black;
        text-decoration: none;
        line-height: 60px;
        word-spacing: 22px;
    }

    /*右面表*/
    #wtable2 {
        font-size: 24px;
        position: absolute;
        left: 720px;
        top: 85px;

    }

    #wp1 {
        font-size: 36px;
        color: rgb(193, 33, 31);
        position: absolute;
        top: 0px;
        left: 300px;

    }

    #wp2 {
        font-size: 36px;
        color: rgb(193, 33, 31);
        position: absolute;
        top: 0px;
        left: 820px;
    }


    .elexcerptlist1 {
        position: absolute;
        top: 560px;
        left: 180px;
    }

    input {
        width: 200px;
        border: none;
        border-bottom: 2px solid black;
        background-color: inherit;
        font-family: "汇文明朝体", "SimSun";
        font-size: 20px;
    }

    /*添加框*/
    #dweb1 {
        position: absolute;
        top: 650px;
        left: 700px;
    }


    /*竖线*/
    .sx {
        width: 2px;
        height: 600px;
        background-color: black;
        position:absolute;
        top: 60px;
        left: 660px;
    }

    /*翻页*/
    .weblist1{
        position: absolute;
        top: 580px;
        left: 700px;
    }
</style>