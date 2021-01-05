'''
Author: your name
Date: 2020-12-29 16:13:55
LastEditTime: 2021-01-05 11:42:36
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \after\app.py
'''
#主界面
from flask import Flask,request,Blueprint,make_response
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flask import url_for,jsonify
import json
from publish import publish_blueprint
from lease import lease_blueprint
from other import other_blueprint
from sql import Login,db
from flask_cors import CORS
from flask_login import LoginManager,UserMixin,login_user,current_user,login_required,logout_user

app=Flask(__name__)
CORS(app)

app.secret_key = 'honus'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.register_blueprint(publish_blueprint)
app.register_blueprint(lease_blueprint)
app.register_blueprint(other_blueprint)
CORS(publish_blueprint)
CORS(lease_blueprint)
CORS(other_blueprint)
class Config(object):
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://honus:honus@54.199.224.123:3306/sql_course'
    #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
    #禁用自动提交数据管理
    app.config["SQLALCHEMY_ECHO"]=True
    #设置这一项是每次请求结束后都会自动提交数据库中的变动
    app.config['SQLALCHEMY_RECORD_QUERIES']=True
    #启用查询记录
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
    app.config['JSON_AS_ASCII'] = False

app.config.from_object(Config)
db.app=app
db.init_app(app)


class User(UserMixin):
    def __init__(self,user):
        self.username=user.username
        self.password=user.password

    def get_id(self):
        return self.username

    @staticmethod
    def get(user_id):
        """根据用户ID获取用户实体，为 login_user 方法提供支持"""
        if not user_id:
            return None
        result=Login.query.all()
        for user in result:
            if user.username == user_id:
                return User(user)
        return None

@login_manager.user_loader
def user_loader(user_id):
    return User.get(user_id)

@app.route('/login',methods=['POST'])
def login():
    find=request.get_json()
    username=find['username']
    password=find['password']
    res={
        'status':'',
    }
    result=Login.query.filter_by(username=username).first()
    if result==None:
        res['status']='用户不存在'
        return res
    if result.username==username and result.password==password:
        user=User(result)
        user.name=username
        login_user(user)
        res['status']='success'
        return jsonify(res)
    else:
        res['status']='密码错误'
        return jsonify(res)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('/login'))

@app.route('/signup',methods=['POST'])
def signup():
    find=request.get_json()
    username=find['username']
    data={
        'status':''
    }
    result=Login.query.filter_by(username=username).first()
    if result!=None and str(username)==(result.username):
        data['status']='用户已存在'
        return data
    password=find['password']
    ensure=find['ensure']
    if str(password)!=str(ensure):
        data['status']='密码与确认密码不符'
        return data
    count='0'
    deliver='0'
    balance='0'
    user=Login(username=username,password=password,count=count,deliver=deliver,balance=balance)
    db.session.add(user)
    db.session.commit()
    result=Login.query.filter_by(username=username).first()
    if result.username==username:
        data['status']='success'
    else:
        data['status']='注册失败'
    db.session.close()
    return data
if __name__=='__main__':
    app.run(debug=True)