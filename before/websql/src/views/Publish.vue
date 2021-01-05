<!--
 * @Author: your name
 * @Date: 2020-06-17 17:08:14
 * @LastEditTime: 2021-01-04 19:51:42
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
            <el-table-column prop="uuid" label="ID" width="90"></el-table-column>
            <el-table-column prop="username" label="用户名" width="80"></el-table-column>
            <el-table-column prop="name" label="备注" width="70"></el-table-column>
            <el-table-column prop="address" label="地址" width="140"></el-table-column>
            <el-table-column prop="room" label="房号" width="140"></el-table-column>
            <el-table-column prop="unit_type" label="单元类型" width="80"></el-table-column>
            <el-table-column prop="price" label="价格" width="50"></el-table-column>
            <el-table-column prop="link" label="联系方式" width="120"></el-table-column>
            <el-table-column prop="begintime" label="开始时间" width="190"></el-table-column>
            <el-table-column prop="endtime" label="结束时间" width="190"></el-table-column>
            <el-table-column fixed="right" label="操作" width="140">
                <template slot-scope="scope">
                    <el-button @click="lease(scope.row)" type="text" size="small">租赁</el-button>
                    <el-button @click="edit(scope.row)" type="text" size="small">修改</el-button>
                    <el-button @click="deleteWeb(scope.row)" type="text" size="small">删除</el-button>
                </template>
            </el-table-column>

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
        methods: {
            deleteWeb(row){
                const _this = this
                this.$axios.get('/api/del/'+row.uuid).then(function(resp){
                    _this.$alert('删除成功！', '消息', {
                        confirmButtonText: '确定',
                        callback: action => {
                            window.location.reload()
                        }
                    })
                })
            },
            edit(row) {
                this.$router.push({
                    path: '/updatepublish',
                    query:{
                        id:row.uuid,
                        type:row.unit_type
                    }
                })
            },
            lease(row) {
                this.$router.push({
                    path:'/addlease',
                    query:{
                        id:row.uuid
                    }
                })
            },
            page(currentPage){
                const _this=this
                this.$axios.get('/api/getpublishlist/'+currentPage+'/6').then(function(resp){
                    for(var i=0;i<resp.data.length;i++)
                    {
                        var data=new Date((resp.data[i]['begintime'])*1000)
                        resp.data[i]['begintime']=data.toLocaleString()
                        var data=new Date((resp.data[i]['endtime'])*1000)
                        resp.data[i]['endtime']=data.toLocaleString()
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
            this.$axios.get('/api/getpublishlist/1/6').then(function(resp){
                for(var i=0;i<resp.data.length;i++)
                {
                    var data=new Date((resp.data[i]['begintime'])*1000)
                    resp.data[i]['begintime']=data.toLocaleString()
                    var data=new Date((resp.data[i]['endtime'])*1000)
                    resp.data[i]['endtime']=data.toLocaleString()
                }
                _this.tableData=resp.data
                _this.pageSize=6
                _this.total=6
            })
            this.$axios.get('/api/getpublishcount').then(function(resp){
                _this.total=resp.data
                })
        },
        data() {
            return {
                total:null,
                tableData: null,
                pageSize:null
            }
        }
    }
</script>