<template>
  <div id="d1">
    <div v-if="showtime" id="d2" @click.left="ch">
      <p id="p1">{{ hours }}:{{ minutes }}</p>
      <p id="p2">{{ year }}.{{ month }}.{{ date }} {{ week }}</p>
    </div>
    <div id="d3" v-if="showbutton">
      <img src="./assets/home.png" class="dimage3" @click.left="backhome">
      <img src="./assets/refresh.png" class="dimage3" @click.left="refresh">
      <img src="./assets/back.png" class="dimage3" @click.left="back">
    </div>


    <!--.once:只执行一次-->
    <router-view></router-view>

  </div>
</template>

<script>
  //引入组件

  //import Catalogue from "./components/Catalogue.vue"
  //import Sign from "./components/Sign.vue"
  //import docx from "./components/docx.vue"
  export default {
    name: "App",
    components: {},
    data() {
      return {
        //时间
        year: "2022",
        month: "1",
        date: "1",
        hours: "00",
        minutes: "00",
        seconds: "00",
        week: "星期一",
        //时间显示
        showtime: true,
        showbutton: false,
      };
    },

    mounted() {
      //判断当前页面位置，如果不是在封面，则不显示时间
      if (window.location.href != window.a +"/#/") {
          this.showtime = false
          this.showbutton = true
        } else {
          this.showtime = true
          this.showbutton = false
        }

      //时间
      setInterval(getTime, 500);
      var that = this;
      function getTime() {
        var dateObj = new Date();
        var year = dateObj.getFullYear(); //年
        var month = dateObj.getMonth() + 1; //月  (注意：月份+1)
        var date = dateObj.getDate(); //日
        var day = dateObj.getDay();
        var weeks = [
          "星期日",
          "星期一",
          "星期二",
          "星期三",
          "星期四",
          "星期五",
          "星期六",
        ];
        var week = weeks[day]; //根据day值，获取星期数组中的星期数。
        var hours = dateObj.getHours(); //小时
        var minutes = dateObj.getMinutes(); //分钟
        var seconds = dateObj.getSeconds(); //秒

        if (month < 10) {
          month = "0" + month;
        }
        if (date < 10) {
          date = "0" + date;
        }
        if (hours < 10) {
          hours = "0" + hours;
        }
        if (minutes < 10) {
          minutes = "0" + minutes;
        }
        if (seconds < 10) {
          seconds = "0" + seconds;
        }

        that.year = year;
        that.month = month;
        that.date = date;
        that.hours = hours;
        that.minutes = minutes;
        that.seconds = seconds;
        that.week = week;
      }
    },

    methods: {

      ch() {
        this.$router.push("catalogue");
        //判断当前页面位置，如果不是在封面，则不显示时间
        if (window.location.href != window.a +"/#/") {
          this.showtime = false
          this.showbutton = true
        } else {
          this.showtime = true
          this.showbutton = false
        }

      },
      backhome() {
        window.location.replace(window.a + "/");
      },
      back() {
        this.$router.back()
        //判断当前页面位置，如果是目录，则返回后即为封面
        if (window.location.href != window.a +"/#/catalogue") {
          this.showtime = false
          this.showbutton = true
        } else {
          this.showtime = true
          this.showbutton = false
        }
      },

      refresh(){
        this.$router.go(0);
      }

      //所有页面，滚轮上滑都是返回上一页，初目录下滑重新加载封面外，所有页面下滑都是跳转到目录

      /* mouseWheel(e) {
         if (e.wheelDelta || e.detail) {
           if (e.wheelDelta > 0 || e.detail < 0) {
            
             //当鼠标滚轮向上滚动时
           }
           if (e.wheelDelta < 0 || e.detail > 0) {
             //当鼠标滚轮向下滚动时
             this.$router.push("catalogue");
             this.showtime = false;
           }
         }
       },*/
    },
  };
</script>

<style>
  body,
  html {
    height: 100%;
    margin: 0;
    padding: 0;
  }


  body {

    font-family: "汇文明朝体", "SimSun";
    display: flex;
    justify-content: center;
    align-items: center;
    background-image: url(https://api.ixiaowai.cn/gqapi/gqapi.php);
    background-size: cover;
    background-position: center;
  }

  #d1 {
    width: 1280px;
    height: 720px;

    margin: auto;

    position: absolute;
    /*将显示区域固定在屏幕正中间 */
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

  }

  #d2 {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

  }

  #d3 {
    position: absolute;
    width: 35px;
    top: 8px;
    left: 1235px;
    z-index: 10
  }



  #p1 {
    font-size: 152px;
    text-align: center;
    margin: -50px;
  }

  #p2 {
    font-size: 38px;
    text-align: center;
  }

  .dimage3 {
    width: 30px;
    height: 30px;
    margin-bottom: 10px;

  }

  @font-face {
    font-family: 汇文明朝体;

    src: url("shouxieti.ttf");
  }
</style>