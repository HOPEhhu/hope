<template>

  <div id="dl2">
    <p id="pl1">3</p>
    <router-link to="/schedule" id="pl2">待办事项</router-link>
    <table>
      <Item1 v-for="todo in todos" :key="todo.id" :todo="todo" :checkTodo="checkTodo"  />
    </table>
  </div>
</template>

<script>
  import axios from 'axios'
  import Item1 from "./Item1.vue";
  export default {
    name: "List1",
    components: { Item1 },
    data() {
      return {
        todos: [],
        time:''
      }
    },
    mounted() {
      var that = this;

      var time1=new Date();
      var year1=time1.getFullYear();
      var month1=time1.getMonth()+1;
      var data1=time1.getDate();
      that.time=year1+'.'+month1+'.'+data1
      console.log(that.time)




      axios.get("http://124.71.219.191/api/schedule", {
        params: {
          "action": "list_schedule",
          "time": this.time,
        }
      })
        .then(function (value) {
          console.log(value)
          that.todos = value.data.retlist;
        })
        .catch(function (reason) {
          console.log(reason)

        })
    },
    methods: {


      //勾选
      checkTodo(id) {
        this.todos.forEach((todo) => {
          if (todo.id === id) {
            todo.finish = !todo.finish
            axios.post("http://124.71.219.191/api/schedule", {
              "action": "check_schedule",
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
          }
        })
      },
    }
  };

</script>

<style scoped>
  #dl2 {
    width: 280px;
    height: 380px;
    padding: 5px;
    font-size: 20px;
    
    
  }
  #pl1 {
    color: rgb(193, 33, 31);
    font-size: 36px;
    margin: 0%;
  }

  #pl2 {
    color: rgb(193, 33, 31);
    font-size: 24px;
    margin: 0%;
    line-height: 45px;
    text-decoration: none;
    font-weight: 600;
  }
</style>