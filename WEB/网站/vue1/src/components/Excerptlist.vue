<template>
    
    <div id="dexcerpt1">
        <p>摘录</p>
        <table>
            <Excerptitem v-for="excerpt in excerpts" :key="excerpt.id" :excerpt="excerpt"
                :deleteExcerpt="deleteExcerpt" />
        </table>

        <el-pagination class="elexcerptlist1" layout="prev, pager, next" :total="excerptss.length" :page-size="5"
            @current-change="handleCurrentChange">
        </el-pagination>

        <p id="pexcerpt1">添加：</p>
        <p><textarea rows="10" cols="30" @keyup.enter="add"></textarea></p>
    </div>
</template>

<script>
    import axios from 'axios'
    import Excerptitem from "./excerpt/Excerptitem.vue";
    export default {
        name: "Excerptlist",
        components: { Excerptitem },
        props: [],
        data() {
            return {
                excerptss: [],
                excerpts: []
            }
        },
        computed: {

        },

        mounted() {
            var that = this;
            axios.get("http://124.71.219.191/api/excerpt", {
                params: {
                    "action": "list_excerpt",
                }
            })
                .then(function (value) {
                    console.log(value)
                    that.excerptss = value.data.retlist;
                    that.excerpts = that.excerptss.slice(0,5)
                })
                .catch(function (reason) {
                    console.log(reason)

                })




        },


        methods: {

            handleCurrentChange(val) {
                this.excerpts = this.excerptss.slice((val - 1) * 5, val * 5 );
            },

            //添加
            add(e) {
                var that = this;
                axios.post("http://124.71.219.191/api/excerpt", {
                    "action": "add_excerpt",
                    "data": {
                        "content": e.target.value,
                    }
                })
                    .then(function (response) {
                        if (response.data.ret == 0) {
                            const todoObj = { id: response.data.id, content: e.target.value };
                            that.excerptss.push(todoObj);
                            console.log(e.target.value);
                            e.target.value = "";

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
            deleteExcerpt(id) {
                this.excerpts = this.excerpts.filter((excerpt) => {
                    axios.post("http://124.71.219.191/api/excerpt", {
                        "action": "del_excerpt",
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
                    return excerpt.id != id

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
        height: 60px;
        border: none;
        border-bottom: 2px solid black;
        background-color: inherit;
        font-family: "汇文明朝体", "SimSun";
        font-size: 20px;
        position: absolute;
        top: 650px;
        left: 180px;
    }

    #pexcerpt1 {
        font-size: 24px;
        position: absolute;
        top: 620px;
        left: 110px;
    }

    table {
        font-size: 24px;
        position: absolute;
        left: 180px;
        top: 55px;

    }
    p{
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
</style>