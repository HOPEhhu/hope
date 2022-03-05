<template>
  <div id="dsign1">
    
    <img src="../assets/home.png" id="dimage3" @click.left="backimage">
    <img src="../assets/back.png" id="dimage4" @click.left="back">
    <div id="dsign2">
      <p id="psign1">Login</p>

      <p id="dsign3">用户名:<input id="isign1" type="text" v-model="name"></p>

      <p id="dsign4">密 码:<input id="isign2" type="password" v-model="password"></p>

      <p><input id="isign3" type="submit" class="btn" value="登  录" @click="sign"></p>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: "Sign",
    data() {
      return {
        name: "",
        password: "",

      }
    },

    methods: {
      backimage(){
        
        window.location.replace("http://124.71.219.191/");

      },

      back(){
        this.$router.back()
      },
      sign: function () {
        var that = this;
        const params = new URLSearchParams();
        params.append('name', that.name);
        params.append('password', that.password);
        axios.post("http://124.71.219.191/api/signin", params)
          .then(function (response) {
            if (response.data.ret == 0) {
              alert("登录成功")
              that.$router.back(); 

            } else {
              alert("登录失败")

            }

          })
          .catch(function (error) {
            console.log(error);
          });


      },



    }
  };
</script>


<style scoped>
  #dsign1 {
    width: 1280px;
    height: 720px;
    background-color: rgb(240 241 245);
    background-image: linear-gradient(rgb(210 213 219) 1px, transparent 1px),
      linear-gradient(to right, rgb(210 213 219) 1px, rgb(240 241 245) 1px);
    background-size: 20px 20px;
    margin: auto;
    box-shadow: 5px 5px 5px -2px rgba(0, 0, 0, 0.3);
    position: relative;
  }

  #dsign2 {
    position: absolute;
    top: 50%;
    margin-top: -200px;
    left: 50%;
    margin-left: -200px;
    /* absolute居中的一种方法 */
    width: 400px;
    height: 320px;
    border: 2px solid;
    border-radius: 25px;
    text-align: center;
    padding: 5px 40px;
    box-sizing: border-box;
    /* 这样padding就不会影响大小 */
  }

  #psign1 {
    font-size: 42px;
  }

  #isign1 {
    width: 130px;
    border: none;
    border-bottom: 2px solid black;
    background-color: inherit;
  }

  #dsign3 {
    font-size: 24px;

  }

  #dsign4 {
    font-size: 24px;
    word-spacing: 15px
  }

  input {
    font-family: "汇文明朝体", "SimSun";
    font-size: 24px;
  }

  #isign2 {
    width: 130px;
    border: none;
    border-bottom: 2px solid black;
    background-color: inherit;
  }

  #isign3 {
    background-color: inherit;
    border: 0px;
    font-family: "汇文明朝体", "SimSun";
    font-size: 36px;
    margin: 5px, 0px, 5px;
  }


  #dimage3 {
    position: absolute;

    width: 30px;
    height: 30px;
    top: 10px;
    left: 1240px;

  }


  #dimage4 {
    position: absolute;

    width: 30px;
    height: 30px;
    top: 50px;
    left: 1240px;

  }


</style>