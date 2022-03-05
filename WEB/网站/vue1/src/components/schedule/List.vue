<template>

  <div>
    <div id="dlist1">
      {{time}}
      {{weekc}}
    </div>
    <table>
      <Item v-for="todo in todos" :key="todo.id" :todo="todo" :checkTodo="checkTodo" :deleteTodo="deleteTodo" />
    </table>
    <input type="text"  @keyup.enter="add" />
  </div>
</template>

<script>
  import axios from 'axios'
  import Item from "./Item.vue";
  export default {
    name: "List",
    components: { Item },
    props: ["year", "week", "day", "weekc"],
    data() {
      return {
        todos: []
      }
    },
    computed: {
      time: {
        //将获取到的周数转化为日期
        get() {
          var date1 = new Date(this.year, 0, 1);
          var dayMS = 24 * 60 * 60 * 1000;
          var firstDay = (7 - date1.getDay()) * dayMS;
          var weekMS = (this.week - 1) * 7 * dayMS;
          var result = date1.getTime() + firstDay + weekMS + this.day * dayMS;
          date1 = new Date(result);
          var year1 = date1.getFullYear();
          var month1 = date1.getMonth() + 1;
          var day1 = date1.getDate();
          date1 = year1 + "." + month1 + "." + day1;
          console.log(date1);
          return date1;
        }

      }
    },

    mounted() {
      var that = this;

      axios.get("http://124.71.219.191/api/schedule", {
        params: {
          "action": "list_schedule",
          "time": that.time,
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
    //监听watch变化，以更新数据
    watch: {
      time: {
        handler() {
          this.cha();
        }

      }
    },

    methods: {
      //查
      cha() {
        var that = this;

        axios.get("http://124.71.219.191/api/schedule", {
          params: {
            "action": "list_schedule",
            "time": that.time,
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


      //添加
      add(e) {
        var that = this;
        axios.post("http://124.71.219.191/api/schedule", {
          "action": "add_schedule",
          "data": {
            "time": that.time,
            "content": e.target.value,
          }
        })
          .then(function (response) {
            if (response.data.ret == 0) {
              const todoObj = { id: response.data.id, finish: false, content: e.target.value }
              that.todos.push(todoObj)
              e.target.value = ""

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

      //删除
      deleteTodo(id) {
        this.todos = this.todos.filter((todo) => {
          axios.post("http://124.71.219.191/api/schedule", {
            "action": "del_schedule",
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
          return todo.id != id

        })
      },

    },
  };
</script>

<style scoped>
  input {
    width: 190px;
    border: none;
    border-bottom: 2px solid black;
    background-color:inherit;
    position: absolute;
    top: 290px;

  }
  #dlist1{
    color: rgb(193, 33, 31);
    font-size: 18px;
    margin: 0%;
    line-height: 18px;
    text-align: center;
    }
</style>