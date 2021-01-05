'''
Author: your name
Date: 2020-12-30 10:38:27
LastEditTime: 2021-01-04 23:07:49
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \after\sql.py
'''
#数据库
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(use_native_unicode='utf8')

class Login(db.Model):
    #__tablename__='login'
    username=db.Column(db.String(20),primary_key=True)
    password=db.Column(db.String(20),nullable=False)
    count=db.Column(db.Float(20),nullable=False)
    deliver=db.Column(db.Float(20),nullable=False)
    balance=db.Column(db.Float(20),nullable=False)
    def repr(self):
        return self

class Publish(db.Model):
    __tablename__='publish'
    username=db.Column(db.String(20),nullable=False)
    name=db.Column(db.String(20),nullable=False)
    address=db.Column(db.String(255),nullable=False)
    room=db.Column(db.String(255),nullable=False)
    unit_type=db.Column(db.String(255),nullable=False)
    link=db.Column(db.String(255),nullable=False)
    price=db.Column(db.Float(20),nullable=False)
    flag=db.Column(db.Integer,nullable=False)
    uuid=db.Column(db.Integer,primary_key=True)
    begintime=db.Column(db.Integer,nullable=False)
    endtime=db.Column(db.Integer,nullable=False)
    def repr(self):
        return self

class Lease(db.Model):
    __tablename__='lease'
    username=db.Column(db.String(20),nullable=False)
    name=db.Column(db.String(20),nullable=False)
    link=db.Column(db.String(255),nullable=False)
    use=db.Column(db.String(255),nullable=False)
    uuid=db.Column(db.Integer,primary_key=True)
    def repr(self):
        return self

class Unit_type(db.Model):
    __tablename__='unit_type'
    type=db.Column(db.String(255),primary_key=True)
    count=db.Column(db.Integer,nullable=False)


#result=Login.query.all()
# print(type(result))
# for i in result:
#     print(i.username)
#     print(i.password)
#数据返回为Login对象