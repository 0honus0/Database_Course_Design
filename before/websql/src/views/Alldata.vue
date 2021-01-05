<!--
 * @Author: your name
 * @Date: 2021-01-04 12:43:55
 * @LastEditTime: 2021-01-05 12:07:05
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\Alldata.vue
-->
<!--
 * @Author: your name
 * @Date: 2020-06-17 17:08:14
 * @LastEditTime: 2021-01-04 11:24:32
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\Mulu.vue
-->
<template>
    <div>
        <el-table
                :data="tableData"
                border
                style="width: 150%">
            <el-table-column prop="uuid" label="ID" width="100"></el-table-column>
            <el-table-column prop="username" label="房东" width="100"></el-table-column>
            <el-table-column prop="name" label="备注" width="100"></el-table-column>
            <el-table-column prop="address" label="地址" width="180"></el-table-column>
            <el-table-column prop="room" label="房号" width="140"></el-table-column>
            <el-table-column prop="flag" label="是否出租" width="100"></el-table-column>


        </el-table>

        <el-pagination
                background
                layout="prev, pager, next"
                :page-size="pageSize"
                :total="total"
                @current-change="page">
        </el-pagination>
    </div>
</template>

<script>
    export default {
        methods:{
                page(currentPage){
                const _this=this
                this.$axios.get('/api/getpublishlist/'+currentPage+'/6').then(function(resp){
                    for(var i=0;i<resp.data.length;i++)
                    {

                    }
                    _this.tableData=resp.data
                    _this.pageSize=6
                    _this.total=6
                })
                this.$axios.get('/api/getpublishcount').then(function(resp){
                    _this.total=resp.data
                })
            }
        },
        created() {
            const _this=this
            this.$axios.get('/api/getalldata/1/6').then(function(resp){
                console.log(resp)
                _this.tableData=resp.data
                _this.pageSize=6
                _this.total=6
            })
            this.$axios.get('/api/getalldata/1/6').then(function(resp){
                _this.total=resp.data
                })
        },
        data() {
            return {
                total:null,
                tableData: null,
                pageSize:null,
            }
        }
    }
</script>