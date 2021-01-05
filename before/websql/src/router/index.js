/*
 * @Author: your name
 * @Date: 2020-06-16 17:35:09
 * @LastEditTime: 2021-01-04 21:30:36
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\router\index.js
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import Publish from '../views/Publish'
import AddPublish from '../views/AddPublish'
import AddLease from '../views/AddLease'
import Index from '../views/Index'
import UpdatePublish from '../views/UpdatePublish'
import UpdateLease from '../views/UpdateLease.vue'
import Lease from '../views/Lease'
import Return from '../views/Return'
import Unit from '../views/Unit.vue'
import AddType from '../views/AddType.vue'
import UpdateType from '../views/UpdateType.vue'
import Unit_Statistics from '../views/Unit_Statistics.vue'
import Price from '../views/Price.vue'
import AllData from '../views/Alldata.vue'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
Vue.use(VueRouter)

let routes;
routes = [
  {
    path: "/",
    name: "二手房中介管理",
    component: Index,
    show: true,
    redirect: "/login",
    children: [
      {
        path: "/publish",
        name: "查询发布信息",
        component: Publish,
        show:true
      },
      {
        path: "/lease",
        name: "查询租赁信息",
        component: Lease,
        show:true
      },
      {
        path: '/updatepublish',
        component: UpdatePublish,
        show: false
      },
      {
        path:'/addlease',
        name:'添加租赁信息',
        show:false,
        component:AddLease
      },
      {
        path: '/updatelease',
        component: UpdateLease,
        show: false
      },
      {
        path:'/return',
        name:'退租',
        show:false,
        component:Return
      },
    ],
  },
  {
    path:'/',
    name:"信息管理",
    component:Index,
    show:true,
    redirect:"/addPublish",
    children:[
      {
        path:"/addPublish",
        name:"添加发布信息",
        component: AddPublish,
        show:true
      },
      {
        path:"/unit",
        name:'户型管理',
        show:true,
        component:Unit,
      },
      {
        path:'/addtype',
        name:'添加户型',
        show:false,
        component:AddType,
      },
      {
        path:'/updatetype',
        name:'修改户型',
        show:false,
        component:UpdateType,
      },

    ]
  },
  {
    path:'/',
    name:"统计信息",
    component:Index,
    show:true,
    redirect:"/unit_statistics",
    children:[
      {
        path:"/unit_statistics",
        name:"户型统计",
        component: Unit_Statistics,
        show:true
      },
      {
        path:"/price",
        name:"余额统计",
        component:Price,
        show:true
      },
      {
        path:"/alldata",
        name:"房屋状态统计",
        component:AllData,
        show:true,
      },
    ]
  },
  {
    path:'/login',
    name:'登陆',
    component:Login,
    show:false,
  },
  {
    path:'/signup',
    name:'注册',
    component:SignUp,
    show:false,
  }
];

const router = new VueRouter({
  mode: 'history',
  base: '/',
  routes
})

export default router
