<template>
  <tr>
    <td><input type="checkbox" :checked="todo.finish" @click="handleChecked(todo.id)" /></td>
    <td :style="styleObj" class="td1">{{ todo.content }}</td>
    <td><button @click="handleDelete(todo.id)">删除</button></td>
  </tr>
</template>

<script>
  export default {
    name: "Item",
    props: ["todo", "checkTodo", "deleteTodo"],
    methods: {
      handleChecked(id) {
        this.checkTodo(id)
      },
      handleDelete(id) {
        if (confirm("确定要删除吗？")) {
          this.deleteTodo(id)

        }

      },
    },
    computed: {
      styleObj: {
        get() {
          if (this.todo.finish) {
            return { textDecoration: "line-through" };
          } else {
            return { textDecoration: "none" };
          }
        },
      },
    },
  };
</script>

<style scoped>
  td {
    padding-top: 5px;
  }

  button {
    display: none;
    height: 18px;
    background-color: rgb(221, 221, 221);
    width: 40px;
    border: 0px;
    font-family: "汇文明朝体", "SimSun";
    font-size: 14px;
    margin: 5px, 0px, 5px;
    
  }

  tr:hover button {
    display: block;
  }

  .td1 {
    width: 115px;
  }
</style>