<template>
    <el-form style="width: 70%" :model="ruleForm" :rules="rules" ref="ruleForm" label-width="400px" class="demo-ruleForm">

        <el-form-item label="ID" prop="uuid">
            <el-input v-model="ruleForm.uuid" readonly></el-input>
        </el-form-item>

        <el-form-item label="用户名" prop="username">
            <el-input v-model="ruleForm.username"></el-input>
        </el-form-item>

        <el-form-item label="备注" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>

        <el-form-item label="地址" prop="address">
            <el-input v-model="ruleForm.address"></el-input>
        </el-form-item>

        <el-form-item label="房号" prop="room">
            <el-input v-model="ruleForm.room"></el-input>
        </el-form-item>

        <el-form-item label="单元类型" prop='value'>
        <el-select v-model="value" placeholder="请选择单元类型">
            <el-option
            v-for="(item,index) in ruleForm.unit_type"
            :key="index"
            :label="item['type']"
            :value="item['type']">
            </el-option>
        </el-select>
        </el-form-item>

        <!-- <el-form-item label="单元类型" prop="unit_type">
            <el-input v-model="ruleForm.unit_type"></el-input>
        </el-form-item> -->

        <el-form-item label="价格" prop="price">
            <el-input v-model="ruleForm.price"></el-input>
        </el-form-item>

        <el-form-item label="联系方式" prop="link">
            <el-input v-model="ruleForm.link"></el-input>
        </el-form-item>

        <!-- <el-form-item label="开始时间" prop="begintime">
            <el-input v-model="ruleForm.begintime"></el-input>
        </el-form-item> -->

        <el-form-item label="开始时间" prop="begintime">
            <el-date-picker
            v-model="ruleForm.begintime"
            type="datetime"
            placeholder="选择日期时间">
            </el-date-picker>
        </el-form-item>

        <el-form-item label="结束时间" prop='endtime'>
            <el-date-picker
            v-model="ruleForm.endtime"
            type="datetime"
            placeholder="选择日期时间">
            </el-date-picker>
        </el-form-item>
        <!-- <el-form-item label="结束时间" prop="endtime">
            <el-input v-model="ruleForm.endtime"></el-input>
        </el-form-item> -->
        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">确认</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>

    </el-form>
</template>

<script>
    export default {
        data() {
            return {
                value:'',
                ruleForm: {
                    uuid:'',
                    username:'',
                    name:'',
                    address:'',
                    room:'',
                    unit_type:'',
                    price:'',
                    link:'',
                    begintime:'',
                    endtime:'',
                },
                rules: {
                    username:[
                        { required: true, message: '用户名不能为空', trigger: 'blur' }
                    ],
                    name:[
                        { required: true, message: '备注不能为空', trigger: 'blur' }
                    ],
                    address:[
                        { required: true, message: '地址不能为空', trigger: 'blur' }
                    ],
                    room:[
                        { required: true, message: '房号不能为空', trigger: 'blur' }
                    ],
                    unit_type:[
                        { required: true, message: '单元类型不能为空', trigger: 'blur' }
                    ],
                    price:[
                        { required: true, message: '价格不能为空', trigger: 'blur' }
                    ],
                    link:[
                        { required: true, message: '联系方式不能为空', trigger: 'blur' },
                        { min: 11, max: 11, message: '联系方式有误,请检查', trigger: 'blur' }
                    ],
                    begintime:[
                        { required: true, message: '开始时间不能为空', trigger: 'blur' }
                    ],
                    endtime:[
                        { required: true, message: '结束时间不能为空', trigger: 'blur' }
                    ],

                }
            };
        },
        methods: {
            submitForm(formName) {
                const _this = this
                var begin=(this.ruleForm.begintime.getTime())/10*10
                var end=(this.ruleForm.endtime.getTime())/10*10
                this.ruleForm.begintime=begin
                this.ruleForm.endtime=end
                this.ruleForm.unit_type=this.value
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.$axios.post('/api/publish',this.ruleForm).then(function(resp){
                            if(resp.data['status'] == 'success'){
                                _this.$alert('信息添加成功！', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/publish')
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
            var ts = Math.round(new Date().getTime()%100000000).toString();
            const _this = this;
            _this.ruleForm.uuid=ts
            this.$axios.get('/api/type_change').then(function(resp){
                _this.ruleForm.unit_type=resp.data
                })
        }
    }
</script>