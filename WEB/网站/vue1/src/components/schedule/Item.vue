<template>
  <tr>
    <td><input type="checkbox" :checked="todo.finish" @click="handleChecked(todo.id)" /></td>
    <td :style="styleObj" class="td1" :title="todo.remark">{{ todo.content }}</td>
    <td><img src="../../assets/delete.png" class="tdimage1" @click.left="handleDelete(todo.id)"></td>
    <td><img src="../../assets/remark.png" class="tdimage1" @click.left="handleremark(todo.id)"></td>
    
  </tr>
</template>

<script>
  export default {
    name: "Item",
    props: ["todo", "checkTodo", "deleteTodo","remarkTodo"],
    methods: {
      handleChecked(id) {
        this.checkTodo(id)
      },
      handleDelete(id) {
        if (confirm("确定要删除吗？")) {
          this.deleteTodo(id)
        }
      },
      handleremark(id) {
        this.remarkTodo(id)
      }
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

  

  tr:hover .tdimage1 {
    display: block;
  }


  .td1 {
    width: 165px;
    font-size: 18px;
  }

  .tdimage1 {
    width: 20px;
    height: 20px;
    display: none;

  }
 
</style>