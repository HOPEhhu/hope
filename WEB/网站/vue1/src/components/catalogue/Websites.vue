<template>
  <div id="dw1">
    <p id="pw1">1</p>
    <p id="pw2">常用网站</p>
    <select id="shortselect" v-model="selected">
      <option value="baidu">百度</option>
      <option value="bing">必应</option>
    </select>
    <input type="text" id="iw2" @keyup.enter="search">
    <table>
      <tr>
        <td>
          <a href="https://www.zhihu.com" target="_blank"> 知乎 </a>
        </td>
        <td>
          <a href="https://www.csdn.net/" target="_blank">CSDN </a>
        </td>
        <td>
          <a href="https://translate.google.cn/" target="_blank">谷歌翻译 </a>
        </td>
      </tr>
      <tr>
        <td>
          <a href="https://tieba.baidu.com/index.html" target="_blank">贴吧 </a>
        </td>
        <td>
          <a href="https://www.bilibili.com/" target="_blank">Bilibili </a>
        </td>
        <td>
          <a href="https://yjss.hhu.edu.cn/home/stulogin" target="_blank">教学管理 </a>
        </td>
      </tr>
      <tr>
        <td>
          <a href="https://huaban.com/home/" target="_blank">花瓣 </a>
        </td>
        <td>
          <a href="hhttps://mail.qq.com/" target="_blank">QQmail </a>
        </td>
        <td>
          <a href="https://mail.hhu.edu.cn/" target="_blank">河海邮箱 </a>
        </td>
      </tr>
    </table>











  </div>

</template>

<script>

  export default {
    name: "Websites",
    data() {
      return {
        selected: "baidu",
        s1: "https://www.baidu.com/s?wd=",
        s2: "https://www.bing.com/search?q="
      }
    },
   

    methods: {
      search(e) {
        if (this.selected == "baidu") {
          window.open(this.s1 + e.target.value)
          e.target.value = ""
        } else {
          window.open(this.s2 + e.target.value)
          e.target.value = ""
        }
      }
    }


  };
</script>

<style scoped>
  #dw1 {
    width: 220px;
    height: 170px;
    

  }

  #pw1 {
    color: rgb(193, 33, 31);
    font-size: 36px;
    margin: 0%;
  }

  #pw2 {
    color: rgb(193, 33, 31);
    font-size: 24px;
    margin: 0%;
    line-height: 45px;
    font-weight: 600;
  }

  #shortselect {
    background-color:inherit;
    height: 28px;
    width: 58px;
    border: 0px;
    font-family: "汇文明朝体", "SimSun";
    font-size: 20px;
    margin: 5px, 0px, 5px;
    
  }

  #iw2 {
    /*输入框 */
    width: 130px;
    border: none;
    border-bottom: 2px solid black;
    background-color:inherit;
  }

  a {
    font-size: 20px;
    color: black;
    text-decoration: none;
    line-height: 35px;
    word-spacing: 22px;
    

  }
  table{
    width: 210px;
    text-align: center;
  }
</style>