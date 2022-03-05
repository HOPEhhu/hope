<template>
  <div id="dbook1">
    
    <img src="../assets/home.png" id="dimage3" @click.left="backimage">
    <img src="../assets/back.png" id="dimage4" @click.left="back">
    <h1 id="hbook1">书单</h1>
    <!--显示书籍详细信息-->
    <div class="dbook2" v-if="showbook">
      <p>书名：{{ showbookname }}</p>
      <p>作者：{{ showauthor }}</p>
      <p>字数：{{ showwordcount }}</p>
      <p>时间：{{ showreadtime }}</p>
      <p>读后感：{{ showremark }}</p>
      <button @click="add1" >添加</button>
      <button @click="change1" >修改</button>
      <button @click="delete1" >删除</button>
    </div>

    <!--修改书籍信息-->
    <div class="dbook2" v-if="changebook">
      
        <p>书名：<input type="text" v-model="showbookname" /></p>
        <p>作者：<input type="text" v-model="showauthor" /></p>
        <p>字数：<input type="text" v-model="showwordcount" /></p>
        <p>时间：<input type="text" v-model="showreadtime" /></p>
        <p>读后感：</p>
        <p><textarea rows="10" cols="30" v-model="showremark"></textarea></p>
        <button @click="change2" >提交</button>
        <button @click="back1" >返回</button>
      
    </div>

    <!--添加书籍信息-->
    <div class="dbook2" v-if="addbook">
      
        <p>书名：<input type="text" v-model="showbookname" /></p>
        <p>作者：<input type="text" v-model="showauthor" /></p>
        <p>字数：<input type="text" v-model="showwordcount" /></p>
        <p>时间：<input type="text" v-model="showreadtime" /></p>
        <p>读后感：</p>
        <p><textarea rows="10" cols="30" v-model="showremark"></textarea></p>
        <button @click="add2" >提交</button>
        <button @click="back1" >返回</button>
      
    </div>

    <table>
      <tr>
        <td>书名</td>
        <td>作者</td>
      </tr>
      <Bookitem
        v-for="book in books"
        :key="book.id"
        :book="book"
        :show="show"
      />
    </table>
    <el-pagination
      class="elbooklist1"
      layout="prev, pager, next"
      :total="bookss.length"
      :page-size="10"
      @current-change="handleCurrentChange"
    >
    </el-pagination>
  </div>
</template>

<script>
import axios from "axios";
import Bookitem from "../components/book/Bookitem.vue";
export default {
  name: "Booklist",
  components: { Bookitem },

  data() {
    return {
      showid: "",
      showbookname: "",
      showauthor: "",
      showreadtime: "",
      showwordcount: "",
      showremark: "",
      bookss: [],
      books: [],
      showbook: true,
      changebook: false,
      addbook: false,
    };
  },
  methods: {
    backimage(){
        
        window.location.replace("http://124.71.219.191/");

      },

      back(){
        this.$router.back()
      },
    show(id) {
      this.books.forEach((book) => {
        if (book.id === id) {
          this.showid = book.id;
          this.showbookname = book.bookname;
          this.showauthor = book.author;
          this.showreadtime = book.readdata;
          this.showwordcount = book.wordCount;
          this.showremark = book.remark;
        }
      });
    },

    change2() {
      var that = this;
      axios
        .post("http://124.71.219.191/api/book", {
          action: "modify_book",
          id: that.showid,
          newdata: {
            bookname: that.showbookname,
            author: that.showauthor,
            readdata: that.showreadtime,
            wordcount: that.showwordcount,
            remark: that.showremark,
          },
        })
        .then(function (response) {
          if (response.data.ret == 0) {
            alert("修改成功");
            that.showbook = true;
            that.changebook = false;
            that.addbook = false;
          } else if (response.data.ret == 302) {
            alert("未登录");
            that.$router.push("signin");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    add2() {
      var that = this;
      axios
        .post("http://124.71.219.191/api/book", {
          action: "add_book",
          data: {
            bookname: that.showbookname,
            author: that.showauthor,
            readdata: that.showreadtime,
            wordcount: that.showwordcount,
            remark: that.showremark,
          },
        })
        .then(function (response) {
          if (response.data.ret == 0) {
            alert("添加成功");
            location.reload();
          } else if (response.data.ret == 302) {
            alert("未登录");
            that.$router.push("signin");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    change1() {
      if (this.showid != "") {
        (this.showbook = false),
          (this.changebook = true),
          (this.addbook = false);
      } else {
        alert("当前内容为空，不能修改。");
      }
    },
    delete1() {
        alert("确定要删除吗？")
      var that = this;
      axios
        .post("http://124.71.219.191/api/book", {
          action: "del_book",
          id: that.showid,
        })
        .then(function (response) {
          if (response.data.ret == 0) {
            location.reload();
          } else if (response.data.ret == 1) {
            alert("书名不存在");
          } else if (response.data.ret == 302) {
            alert("未登录");
            that.$router.push("signin");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    add1() {
      (this.showid = ""),
        (this.showbookname = ""),
        (this.showauthor = ""),
        (this.showreadtime = ""),
        (this.showwordcount = ""),
        (this.showremark = ""),
        (this.showbook = false),
        (this.changebook = false),
        (this.addbook = true);
    },
    back1(){
        this.showbook=true,
      this.changebook= false,
      this.addbook= false
    },

    handleCurrentChange(val) {
    this.books = this.bookss.slice((val-1)*10, val*10);
  },
  },

  mounted() {
    var that = this;
    axios
      .get("http://124.71.219.191/api/book?action=list_book")
      .then(function (value) {
        that.bookss = value.data.retlist;
        that.books = that.bookss.slice(0,10)
      })
      .catch(function (reason) {
        console.log(reason);
      });
  },
  
};
</script>

<style scoped>
#hbook1 {
  color: rgb(193, 33, 31);
  font-size: 64px;
  margin: 0%;
  line-height: 70px;
  text-align: center;
}

#dbook1 {
  width: 1280px;
  height: 720px;

  margin: auto;
  box-shadow: 5px 5px 5px -2px rgba(0, 0, 0, 0.3);

  background-color: rgb(240 241 245);
  background-image: linear-gradient(rgb(210 213 219) 1px, transparent 1px),
    linear-gradient(to right, rgb(210 213 219) 1px, rgb(240 241 245) 1px);
  background-size: 20px 20px;
  position: relative;
}
table {
  position: absolute;
  top: 50px;
  left: 660px;
  font-size: 24px;
  width: 550px;
  line-height: 42px;
}
.dbook2 {
  position: absolute;
  top: 60px;
  left: 140px;
  font-size: 24px;
  height: 560px;
  width: 476px;
  
  
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

.elbooklist1 {
  position: absolute;
  top: 560px;
  left: 660px;
  width: 400px;
}
button{
   
    background-color:inherit;
    height: 28px;
    width: 60px;
    border: 0px;
    font-family: "汇文明朝体", "SimSun";
    font-size: 20px;
    margin: 5px, 0px, 5px;
   
}
input{
    width: 300px;
    border: none;
    border-bottom: 2px solid black;
    background-color:inherit;
    font-family: "汇文明朝体", "SimSun";
    font-size: 20px;
}

textarea{
    width: 375px;
    height: 180px;
    border: none;
    border-bottom: 2px solid black;
    background-color:inherit;
    font-family: "汇文明朝体", "SimSun";
    font-size: 20px;
}

</style>