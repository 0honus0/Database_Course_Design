<!--
 * @Author: your name
 * @Date: 2021-01-04 10:17:26
 * @LastEditTime: 2021-01-04 20:10:18
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\UpdateType.vue
-->
<template>
    <el-form style="width: 60%" :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">

        <el-form-item label="原户型" prop="type">
            <el-input v-model="ruleForm.type" readonly></el-input>
        </el-form-item>

        <el-form-item label="新户型" prop="newtype">
            <el-input v-model="ruleForm.newtype"></el-input>
        </el-form-item>


        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">修改</el-button>
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
                    newtype:'',
                },
                rules: {
                    newtype:[
                        { required: true, message: '新户型不能为空', trigger: 'blur' }
                    ]
                }
            };
        },
        methods: {
            back(){
                const _this=this
                _this.$router.push('/unit')
            },
            submitForm(formName) {
                const _this = this
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        var data={
                            'method':'change',
                            'type':this.ruleForm.type,
                            'change': this.ruleForm.newtype,
                        }
                        this.$axios.post('/api/type_change',data).then(function(resp){
                            if(resp.data['status'] == 'changesuccess'){
                                _this.$alert('修改成功！', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/unit')
                                    }
                                })
                            }
                            else{
                                _this.$alert(resp.data['status'],'消息'),{
                                    confirmButtonText:'确定',
                                    callback:action=>{
                                        _this.$router.push('/unit')
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
            console.log(this.$route.query.type)
            _this.ruleForm.type=this.$route.query.type
        }
    }
</script>
