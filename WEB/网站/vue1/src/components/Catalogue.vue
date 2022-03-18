<template>
  <div id="dc1">
    <img id="image1" src="https://img.xjh.me/random_img.php?type=bg&ctype=nature&return=302">
    <p>{{excerpt}}</p>
    <Websites class="w1" />
    <Skill1 class="s1" />
    <list1 class="l1" />
    <Hobby class="hh1" />

  </div>
</template>

<script>
  import Websites from "./catalogue/Websites.vue";
  import Skill1 from "./catalogue/Skill1.vue";
  import List1 from "./catalogue/List1.vue";
  import Hobby from "./catalogue/Hobby.vue";
  import axios from 'axios'
  export default {
    name: "Catalogue",
    props: [],
    components: {
      Websites,
      Skill1,
      List1,
      Hobby,
    },
    data() {
      return {
        excerpt: "",


      }
    },

    mounted() {
      var that = this;
      axios.get(window.a + "/api/excerpt", {
        params: {
          "action": "list_excerpt",
        }
      })
        .then(function (value) {
          const a = Math.random() * value.data.retlist.length;
          that.excerpt = value.data.retlist[Math.floor(a)]["content"];
        })
        .catch(function (reason) {
          console.log(reason)

        })




    },




    methods: {
    },

    computed: {},
  };
</script>

<style scoped>
  #dc1 {
    width: 1280px;
    height: 720px;
    background-color: rgb(240 241 245);
    background-image: linear-gradient(rgb(210 213 219) 1px, transparent 1px), linear-gradient(to right, rgb(210 213 219) 1px, rgb(240 241 245) 1px);
    background-size: 20px 20px;
    margin: auto;
    box-shadow: 5px 5px 5px -2px rgba(0, 0, 0, 0.3);
    position: relative;
  }

  #image1 {
    width: 480px;
    height: 270px;
    position: absolute;
    left: 80px;
    top: 50px;

    --b: 10px;
    /* control the size */
    padding: var(--b);
    border: calc(2*var(--b)) solid #0000;
    outline: 1px solid #000;
    outline-offset: calc(-1*var(--b));
    background: conic-gradient(from 90deg at 1px 1px, #0000 90deg, #000 0);
  }




  p {
    position: absolute;
    left: 120px;
    top: 400px;
    width: 450px;
    height: 200px;
    font-size: 24px;
    text-indent: 48px;
  }


  .w1 {
    position: absolute;
    left: 700px;
    top: 65px;
  }

  .s1 {
    position: absolute;
    left: 1000px;
    top: 65px;
  }

  .l1 {
    position: absolute;
    left: 700px;
    top: 300px;
  }

  .hh1 {
    position: absolute;
    left: 1000px;
    top: 305px;
  }
</style>