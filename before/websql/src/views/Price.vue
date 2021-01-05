<!--
 * @Author: your name
 * @Date: 2021-01-04 11:46:20
 * @LastEditTime: 2021-01-04 14:41:27
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\Price.vue
-->
<template>
    <div>
        <el-table
            :data="tableData"
            border
            style="width: 150%">
            <el-table-column prop="type"
                label="总收入"
                width="300">
                <template slot-scope="scope">
                    <div slot="reference" class="name-wrapper">
                        <el-tag size="medium">{{ scope.row.count }}</el-tag>
                    </div>
                </template>
            </el-table-column>
            <el-table-column prop="type"
                label="付给租户"
                width="300">
                <template slot-scope="scope">
                    <div slot="reference" class="name-wrapper">
                        <el-tag size="medium">{{ scope.row.deliver }}</el-tag>
                    </div>
                </template>
            </el-table-column>

            <el-table-column prop="type"
                label="剩余"
                width="300">
                <template slot-scope="scope">
                    <div slot="reference" class="name-wrapper">
                        <el-tag size="medium">{{ scope.row.balance }}</el-tag>
                    </div>
                </template>
            </el-table-column>
        </el-table>

    </div>
</template>

<script>
    export default {
        created() {
            const _this=this
            this.$axios.get('/api/price').then(function(resp){
                _this.tableData=resp.data
            })
        },
        data() {
            return {
                tableData: null
            }
        }
    }
</script>