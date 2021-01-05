'''
Author: your name
Date: 2020-12-30 08:45:14
LastEditTime: 2021-01-04 11:13:32
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \after\publish.py
'''
#插入发布信息
from flask import Flask,Blueprint,request,jsonify
from sql import Publish,db,Login,Unit_type
import time
publish_blueprint=Blueprint('publish',__name__)

@publish_blueprint.route('/publish',methods=['POST'])
def publish():
    data=request.get_json()
    print(data)
    username=data['username']
    name=data['name']
    address=data['address']
    room=data['room']
    unit_type=data['unit_type']
    link=data['link']
    price=str(float(data['price']))
    flag=0                                 #默认为0
    uuid=str(data['uuid'])
    begintime=int(data['begintime'])/1000
    endtime=int(data['endtime'])/1000
    data={
        'status':''
    }
    result=Publish.query.filter_by(uuid=uuid).first()
    if result!=None and str(result.uuid)==str(uuid):
        data['status']='exist'
        return data
    xinxi=Publish(username=username,name=name,address=address,room=room,unit_type=unit_type,link=link,price=price,flag=flag,uuid=int(uuid),begintime=int(begintime),endtime=int(endtime))
    db.session.add(xinxi)
    db.session.commit()
    db.session.close()
    print(str(uuid))
    result=Publish.query.filter_by(uuid=str(uuid)).first()
    print(result.username)
    if str(result.uuid)==str(uuid):
        data['status']='success'
    else:
        data['status']='failed'
    return data