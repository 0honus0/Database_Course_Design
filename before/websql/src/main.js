/*
 * @Author: your name
 * @Date: 2020-06-16 17:35:09
 * @LastEditTime: 2021-01-04 21:09:07
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\main.js
 */
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'C:/Program Files/nodejs/node_global/node_modules/vue.js/node_modules/axios';
import './plugins/element.js'
import '../icon/iconfont.css'
Vue.prototype.$axios=axios;
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
