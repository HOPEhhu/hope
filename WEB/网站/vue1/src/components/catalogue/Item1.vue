<template>
  <tr>
    <td><input type="checkbox" :checked="todo.finish" @click="handleChecked(todo.id)" /></td>
    <td :style="styleObj" class="td1">{{ todo.content }}</td>
  </tr>
</template>

<script>
  export default {
    name: "Item1",
    props: ["todo", "checkTodo", "deleteTodo"],
    methods: {
      handleChecked(id) {
        this.checkTodo(id)
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
    padding-top: 15px;
  }

  button {
    display: none;
    height: 20px
  }

  tr:hover button {
    display: block;
  }

  .td1 {
    width: 205px;
  }
</style>