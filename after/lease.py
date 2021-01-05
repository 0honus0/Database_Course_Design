'''
Author: your name
Date: 2020-12-30 08:45:33
LastEditTime: 2021-01-05 11:34:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \after\lease.py
'''
#插入租赁信息并进行价格管理和计数
from flask import Flask,Blueprint,request,jsonify
from sql import Lease,db,Publish,Unit_type,Login
import json
from flask_login import LoginManager,UserMixin,login_user,current_user,login_required,logout_user
lease_blueprint=Blueprint('lease',__name__)

@lease_blueprint.route('/lease',methods=['POST'])
@login_required
def lease():
    find=request.get_json()
    print(find)
    admin=current_user.username
    username=find['username1']
    name=find['name1']
    link=find['link1']
    try:
        use=find['use']
    except:
        use=''
    uuid=str(int(find['uuid']))
    result=Lease.query.filter_by(uuid=uuid).first()
    data={
        'status':''
    }
    if result!=None and str(result.uuid)==str(uuid):
        data['status']='已存在'
        return data
    xinxi=Lease(username=username,name=name,link=link,use=use,uuid=uuid)
    db.session.add(xinxi)
    db.session.commit()
    result=Lease.query.filter_by(uuid=uuid).first()
    if result!=None and str(result.uuid)==str(uuid):
        data['status']='success'
    result=Publish.query.filter_by(uuid=uuid).first()
    db.session.close()
    if result!=None:
        res=Unit_type.query.filter_by(type=result.unit_type).first()
        if res!=None:
            res.count=int(res.count)+1
        else:
            data['status']='unit_type查询失败'
        price=result.price
        db.session.commit()
        print(price)
    else:
        data['status']='uuid查询失败'
    result=Login.query.filter_by(username=admin).first()
    if result:
        result.count=float(result.count)+float(price)
        result.deliver=float(result.deliver)+float(price)*0.8
        result.balance=float(result.balance)+float(price)*0.2
        db.session.commit()
    else:
        data['status']='username查询失败'
    db.session.close()
    return jsonify(data)
