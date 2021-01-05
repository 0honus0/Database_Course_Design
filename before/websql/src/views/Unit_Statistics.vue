<!--
 * @Author: your name
 * @Date: 2021-01-04 11:28:41
 * @LastEditTime: 2021-01-04 14:42:22
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\Unit_Statistics.vue
-->
<template>
    <div>
        <el-table
            :data="tableData"
            border
            style="width: 150%">
            <el-table-column prop="type"
                label="户型"
                width="300">
                <template slot-scope="scope">
                    <div slot="reference" class="name-wrapper">
                        <el-tag size="medium">{{ scope.row.type }}</el-tag>
                    </div>
                </template>
            </el-table-column>
            <el-table-column prop="type"
                label="数量"
                width="300">
                <template slot-scope="scope">
                    <div slot="reference" class="name-wrapper">
                        <el-tag size="medium">{{ scope.row.count }}</el-tag>
                    </div>
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
            page(currentPage){
                const _this=this
                this.$axios.get('/api/gettypeall/'+currentPage+'/6').then(function(resp){
                    _tableData=resp.data
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
            this.$axios.get('/api/gettypeall/1/6').then(function(resp){
                console.log(resp)
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