<!--
 * @Author: your name
 * @Date: 2020-06-17 19:29:11
 * @LastEditTime: 2021-01-04 11:48:33
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\Index.vue
-->
<template>
  <el-container style="height: 100%; border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-menu router :default-openeds="['0','1','2']">
        <el-submenu v-for="(item,index) in $router.options.routes" :index="index+''" v-if="item.show">
          <template slot="title">{{item.name}}</template>
          <el-menu-item v-for="(item2,index2) in item.children" :index="item2.path" 
                        :class="$route.path==item2.path?'is-active':''" v-if="item2.show">{{item2.name}}</el-menu-item>
        </el-submenu>
      </el-menu>
    </el-aside>
    <el-main>
        <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
    export default {
        name: "Index"
    }
</script>

<style scoped>

</style>