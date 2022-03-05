<template>
    <tr>
        <td class="td1"><a :href="web.weburl">{{ web.webname }}</a></td>

        <td><button @click="handleDelete(web.id)">删除</button></td>

    </tr>
</template>

<script>
    export default {
        name: "Webmarkitem",
        props: ["web", "deleteweb"],
        methods: {
            handleDelete(id) {
                if (confirm("确定要删除吗？")) {
                    this.deleteweb(id)

                }

            },
        },
        computed: {
        },
    };
</script>

<style scoped>
    button {
        display: none;
        height: 25px;
        background-color: rgb(221, 221, 221);
        width: 80px;
        border: 0px;
        font-family: "汇文明朝体", "SimSun";
        font-size: 20px;
        margin: 5px, 0px, 5px;

    }

    tr:hover button {
        display: block;
    }

    a {

        font-size: 24px;
        margin: 0%;
        text-decoration: none;
        color: black;

    }
    .td1{
        width: 300px;
    }
</style>