<template>
    <tr>
        <td class="td1">{{ excerpt.content }}</td>
        <td><button @click="handleDelete(excerpt.id)">删除</button></td>
        
    </tr>
</template>

<script>
    export default {
        name: "Excerptitem",
        props: ["excerpt", "deleteExcerpt"],
        methods: {
            handleDelete(id) {
                if (confirm("确定要删除吗？")) {
                    this.deleteExcerpt(id)

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

    .td1 {
        width: 750px;
    }
td{
    padding:15px;
}
</style>