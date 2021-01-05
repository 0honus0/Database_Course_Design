<!--
 * @Author: your name
 * @Date: 2021-01-04 10:03:41
 * @LastEditTime: 2021-01-04 20:13:52
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\AddType.vue
-->
<template>
    <el-form style="width: 70%" :model="ruleForm" :rules="rules" ref="ruleForm" label-width="400px" class="demo-ruleForm">

        <el-form-item label="户型" prop="type">
            <el-input v-model="ruleForm.type"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">确认</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
            <el-button @click="back()">返回</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    export default {
        data() {
            return {
                ruleForm: {
                    type:'',
                },
                rules: {
                     type:[
                        { required: true, message: '户型类型不能为空', trigger: 'blur' }
                    ],
                }
            };
        },
        methods: {
            back(){
                const _this=this
                this.$router.push('/unit')
            },
            submitForm(formName) {
                const _this = this
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        var data={
                            'type':this.ruleForm.type,
                            'method':'add',
                        }
                        this.$axios.post('/api/type_change',data).then(function(resp){
                            if(resp.data['status'] == 'addsuccess'){
                                _this.$alert('户型添加成功！', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/unit')
                                    }
                                })
                            }else{
                                 _this.$alert(resp.data['status'], '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/addtype')
                                    }
                                })
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
        }
    }
</script>