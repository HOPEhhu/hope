<template>
  <tr @click="showBook(book.id)">
    <td>{{book.bookname}}</td>
    <td>{{book.author}}</td>
  </tr>
</template>

<script>
  export default {
    name: "Item",
    props: ["book", "show"],
    methods: {
      showBook(id) {
        this.show(id)
      },
      
     
    },
    computed: {
    }  
  };
</script>

<style scoped>
  

</style>