/*
 * @Author: your name
 * @Date: 2021-01-04 13:38:47
 * @LastEditTime: 2021-01-04 19:40:40
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\app.config.js
 */

module.exports = {
    devServer:{
      proxy:{
          '/api':{
              "target":'http://127.0.0.1:5000',
              changeOrigin : true,
              "pathRewrite": { '^/api': '' }
          }
      }
    },
    css: {
      extract: false
    },
    chainWebpack: config => { config.performance.set('hints', false) }
  };