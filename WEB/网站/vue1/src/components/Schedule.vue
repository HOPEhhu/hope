<template>
  <div id="dsc1" @mousewheel="mouseWheel">
    <list :year="year" :week="week" :day="1" weekc="星期一" id="Mon" />
    <list :year="year" :week="week" :day="2" weekc="星期二" id="Tue" />
    <list :year="year" :week="week" :day="3" weekc="星期三" id="Wed" />
    <list :year="year" :week="week" :day="4" weekc="星期四" id="Thurs" />
    <list :year="year" :week="week" :day="5" weekc="星期五" id="Fri" />
    <list :year="year" :week="week" :day="6" weekc="星期六" id="Sat" />
    <list
      :year="year"
      :week="Number(week) + 1"
      weekc="星期日"
      day="0"
      id="Sun"
    />
    <el-date-picker
      v-model="value1"
      type="week"
      format="yyyy 第 WW 周"
      placeholder="选择周"
      class="el1"
    />

    <!--//还有问题：初始化时间；每个框内显示星期几；空白处显示时间；时间选择框放到合适位置-->
  </div>
</template>

<script>
import List from "./schedule/List.vue";
export default {
  name: "Schedule",
  data() {
    return {
      value1: new Date(),
    };
  },
  props: [],
  components: {
    List,
  },
  methods: {
    mouseWheel(e) {
      if (e.wheelDelta || e.detail) {
        if (e.wheelDelta > 0 || e.detail < 0) {
          //当鼠标滚轮向上滚动时
         
        }
        if (e.wheelDelta < 0 || e.detail > 0) {
          //当鼠标滚轮向下滚动时
        }
      }
    },
  },

  computed: {
    //因为要显示一周的内容，如果只是在日期上加的话可能会有问题，所以要将日期转化为周。再到list中将周转化为日期，
    year: {
      get() {
        var value2 = new Date(this.value1);
        value2 = value2.getFullYear();
        return value2;
      },
    },
    week: {
      get() {
        //将日期转化为周
        var date = new Date(this.value1);
        var date2 = new Date(date.getFullYear(), 0, 1);
        var day1 = date.getDay();
        if (day1 == 0) day1 = 7;
        var day2 = date2.getDay();
        if (day2 == 0) day2 = 7;
        var d = Math.round(
          (date.getTime() -
            date2.getTime() +
            (day2 - day1) * (24 * 60 * 60 * 1000)) /
            86400000
        );
        var date3 = Math.ceil(d / 7);
        if (date.getHours() >= 12) date3 = date3 - 1;
        return date3;
      },
    },
  },
};
</script>

<style scoped>
#dsc1 {
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

#Mon {
  position: absolute;
  top: 25px;
  left: 60px;
  border: 2px solid black;
  width: 200px;
  height: 320px;
}

#Tue {
  position: absolute;
  top: 25px;
  left: 300px;
  border: 2px solid black;
  width: 200px;
  height: 320px;
}

#Wed {
  position: absolute;
  top: 25px;
  left: 540px;
  border: 2px solid black;
  width: 200px;
  height: 320px;
}

#Thurs {
  position: absolute;
  top: 25px;
  left: 780px;
  border: 2px solid black;
  width: 200px;
  height: 320px;
}

#Fri {
  position: absolute;
  top: 25px;
  left: 1020px;
  border: 2px solid black;
  width: 200px;
  height: 320px;
}

#Sat {
  position: absolute;
  top: 375px;
  left: 780px;
  border: 2px solid black;
  width: 200px;
  height: 320px;
}

#Sun {
  position: absolute;
  top: 375px;
  left: 1020px;
  border: 2px solid black;
  width: 200px;
  height: 320px;
}
.el1 {
  position: absolute;
  top: 375px;
  left: 60px;
}
</style>