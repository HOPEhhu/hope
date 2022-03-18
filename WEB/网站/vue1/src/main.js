/*
项目入口文件
*/
//引入vue
import Vue from 'vue'
//引入app组件，他是所有组件的父组件

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue'
import VueRouter from 'vue-router'

import './components/global.js'

//引入路由器
import router from './router'
//关闭vue 生产提示
Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(VueRouter)
//创建vue 实例对象
new Vue({
  router,
  render: h => h(App),
  
}).$mount('#app')
