<template>
    <div id="ddocx1">
        <div v-html="message1" id="ddocx2"></div>  <!--显示文章详情-->
    </div>

</template>

<script>
    import axios from 'axios'
    export default {
        name: "docx",
        props: [],
        data() {
            return {
                message1: ""

            }
        },
        methods: {
        },
        mounted() {
            //获取文章内容详情，获得的格式为html格式，传递两个参数。文章类别和文章名
            var that = this;
            axios.get("http://124.71.219.191/api/docx", {
                params: {
                    "sort":that.$route.query.sort,
                    "name":that.$route.query.name,
                }
            })
                .then(function (value) {
                    that.message1 = value.data.retlist;
                })
                .catch(function (reason) {
                    console.log(reason)

                })




        },
        

    };
</script>

<style scoped>
    #ddocx1 {
        width: 1280px;

        margin: auto;
        
        position: absolute;

        background-color: rgb(240 241 245);
        background-image: linear-gradient(rgb(210 213 219) 1px, transparent 1px),
            linear-gradient(to right, rgb(210 213 219) 1px, rgb(240 241 245) 1px);
        background-size: 20px 20px;
    }
    #ddocx2{
        width: 1000px;
        font-size: 24px;
        margin: auto;
        
    }
</style>