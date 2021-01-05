<!--
 * @Author: your name
 * @Date: 2021-01-03 20:48:08
 * @LastEditTime: 2021-01-04 14:42:38
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\Unit.vue
-->
<template>
    <div>
        <el-table
                :data="tableData"
                border
                style="width: 100%">
            <el-table-column prop="type"
                label="户型"
                width="300">
                <template slot-scope="scope">
                    <div slot="reference" class="name-wrapper">
                        <el-tag size="medium">{{ scope.row.type }}</el-tag>
                    </div>
                </template>
            </el-table-column>
            <el-table-column label="操作">
            <template slot-scope="scope">
                <el-button
                size="mini"
                @click="edit(scope.row)">编辑</el-button>
                <el-button
                size="mini"
                type="danger"
                @click="del(scope.row)">删除</el-button>
            </template>
            </el-table-column>
        </el-table>
        <el-button type="primary" @click="add()">添加户型</el-button>
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
            add(){
                const _this=this
                this.$router.push('/addtype')
            },
            edit(row) {
                this.$router.push({
                    path: '/updatetype',
                    query:{
                        type:row.type
                    }
                })
            },
            del(row){
                var data={
                    'type':row.type,
                    'method':'del',
                }
                console.log(data)
                const _this=this
                this.$axios.post('/api/type_change',data).then(function(resp){
                                if(resp.data['status'] == 'delsuccess'){
                                _this.$alert('户型删除成功！', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        window.location.reload()
                                    }
                                })
                            }else{
                                _this.$alert(resp.data['status'], '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        window.location.reload()
                                    }
                                })
                            }
                        })
                    },
            page(currentPage){
                const _this=this
                this.$axios.get('/api/gettype/'+currentPage+'/6').then(function(resp){
                    _this.tableData=resp.data
                    _this.pageSize=6
                    _this.total=6
                })
                this.$axios.get('/api/gettypecount').then(function(resp){
                    _this.total=resp.data
                })
            }
        },
        created() {
            const _this=this
            this.$axios.get('/api/gettype/1/6').then(function(resp){
                _this.tableData=resp.data
                _this.pageSize=6
                _this.total=6
            })
            this.$axios.get('/api/gettypecount').then(function(resp){
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