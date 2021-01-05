<!--
 * @Author: your name
 * @Date: 2021-01-02 20:53:15
 * @LastEditTime: 2021-01-04 20:06:41
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \before\websql\src\views\UpdateLease.vue
-->
<template>
    <el-form style="width: 60%" :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">

        <el-form-item label="ID" prop="id">
            <el-input v-model="ruleForm.uuid" readonly></el-input>
        </el-form-item>

        <el-form-item label="用户名" prop="username">
            <el-input v-model="ruleForm.username"></el-input>
        </el-form-item>

        <el-form-item label="备注" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>

        <el-form-item label="联系方式" prop="link">
            <el-input v-model="ruleForm.link"></el-input>
        </el-form-item>

        <el-form-item label="用途" prop="use">
            <el-input v-model="ruleForm.use"></el-input>
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
                    uuid:'',
                    username:'',
                    name:'',
                    use:'',
                    link:'',
                },
                rules: {
                    uuid: [
                        { required: true, trigger: 'blur' },
                    ],
                    username: [
                        { required: true, message: '请输入用户名',trigger: 'blur' },
                    ],
                    name: [
                        { required: true, message:'请输入备注',trigger: 'blur' },
                    ],
                    link: [
                        { required: true, message: '请输入联系方式',trigger: 'blur' },
                        { min: 11, max: 11, message: '联系方式有误,请检查', trigger: 'blur' }
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
                        this.$axios.post('/api/updatelease',this.ruleForm).then(function(resp){
                            if(resp.data['status'] == 'success'){
                                _this.$alert('修改信息成功！', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/lease')
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
        },
        created() {
            const _this = this
            _this.$axios.get('/api/fbilease/'+this.$route.query.id).then(function(resp){
                _this.ruleForm = resp.data
            })
        }
    }
</script>