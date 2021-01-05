<!--
 * @Author: your name
 * @Date: 2021-01-03 16:08:12
 * @LastEditTime: 2021-01-04 20:07:34
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\Return.vue
-->
<template>
    <el-form style="width: 60%" :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">

        <el-form-item label="ID" prop="id">
            <el-input v-model="ruleForm.uuid" readonly></el-input>
        </el-form-item>

        <el-form-item label="退还金额" prop="price">
            <el-input v-model="ruleForm.price"></el-input>
        </el-form-item>


        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">确定</el-button>
            <el-button @click="resetForm('ruleForm')">清空</el-button>
            <el-button @click="back()">返回</el-button>
        </el-form-item>

    </el-form>
</template>

<script>
    export default {
        data() {
            return {
                ruleForm: {
                    uuid:'',
                    price:'',
                },
                rules: {
                    price:[
                        { required: true, message: '退还金额不能为空', trigger: 'blur' }
                    ]
                }
            };
        },
        methods: {
            back(){
                const _this=this
                _this.$router.push('/lease')
            },
            submitForm(formName) {
                const _this = this
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.$axios.post('/api/return',this.ruleForm).then(function(resp){
                            console.log(resp)
                            if(resp.data['status'] == 'success'){
                                _this.$alert('退租成功！', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/lease')
                                    }
                                })
                            }
                            else{
                                _this.$alert(resp.data['status'],'消息'),{
                                    confirmButtonText:'确定',
                                    callback:action=>{
                                        _this.$router.push('/lease')
                                    }
                                }
                            }
                        })
                    } else {
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        },
        created() {
            const _this = this
            // _this.$axios.get('/api/fbi/'+this.$route.query.id).then(function(resp){
            //     _this.ruleForm = resp.data
            // })
            _this.ruleForm.uuid=this.$route.query.id
        }
    }
</script>