<template>

    <div id="dexcerpt1">
        
    <img src="../assets/home.png" id="dimage3" @click.left="backimage">
    <img src="../assets/back.png" id="dimage4" @click.left="back">
        <p>常用网站</p>
        <table>
            <Webmarkitem v-for="web in webs" :key="web.id" :web="web"
                :deleteweb="deleteweb" />
        </table>

        <p id="pexcerpt1">添加：</p>
        <div id="dweb1">
            网站名：<input type="text" v-model="webname" />
            网址：<input type="text" v-model="weburl" />
            <button @click="add" >提交</button>
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
                webs: [],
                webname:'',
                weburl:'',

            }
        },
        computed: {

        },

        mounted() {
            var that = this;
            axios.get("http://124.71.219.191/api/web", {
                params: {
                    "action": "list_web",
                }
            })
                .then(function (value) {
                    console.log(value)
                    that.webs = value.data.retlist;
                })
                .catch(function (reason) {
                    console.log(reason)

                })




        },


        methods: {
            backimage(){
        
        window.location.replace("http://124.71.219.191/");

      },

      back(){
        this.$router.back()
      },


            //添加
            add() {
                var that = this;
                axios.post("http://124.71.219.191/api/web", {
                    "action": "add_web",
                    "data": {
                        "webname": that.webname,
                        "weburl": that.weburl,
                    }
                })
                    .then(function (response) {
                        if (response.data.ret == 0) {
                            const todoObj = { id: response.data.id, webname: that.webname,weburl:that.weburl };
                            that.webs.push(todoObj);
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



            //删除
            deleteweb(id) {
                this.webs = this.webs.filter((web) => {
                    axios.post("http://124.71.219.191/api/web", {
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

    #pexcerpt1 {
        font-size: 24px;
        position: absolute;
        top: 620px;
        left: 200px;
    }

    table {
        font-size: 24px;
        position: absolute;
        left: 350px;
        top: 65px;

    }

    p {
        font-size: 64px;
        margin: auto;
        color: rgb(193, 33, 31);
        text-align: center;
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
    #dweb1{
        position: absolute;
        top: 650px;
        left: 250px;
    }

    button{
   
   background-color:inherit;
   height: 28px;
   width: 60px;
   border: 0px;
   font-family: "汇文明朝体", "SimSun";
   font-size: 20px;
   margin: 5px, 0px, 5px;
  
}

#dimage3 {
    position: absolute;

    width: 30px;
    height: 30px;
    top: 10px;
    left: 1240px;

  }


  #dimage4 {
    position: absolute;

    width: 30px;
    height: 30px;
    top: 50px;
    left: 1240px;

  }

</style>