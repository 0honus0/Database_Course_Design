from flask import Flask,Blueprint,request,jsonify
from sql import Lease,db,Unit_type,Publish,Login
import json
from flask_login import LoginManager,UserMixin,login_user,current_user,login_required,logout_user
#from flask_restful import fields, marshal
from collections import OrderedDict

other_blueprint=Blueprint('other',__name__)

#归还登记
@other_blueprint.route('/return',methods=['POST'])
@login_required
def return_return():
    find=request.get_json()
    admin=current_user.username
    uuid=str(int(find['uuid']))
    price=str(float(find['price']))
    data={
        'status':''
    }
    result=Login.query.filter_by(username=admin).first()
    if result!=None:
        print(float(result.deliver))
        result.count=float(result.count)-float(price)
        result.deliver=float(result.deliver)-float(price)*float(0.8)
        result.balance=float(result.balance)-float(price)*float(0.2)
        db.session.commit()
    else:
        data['status']='修改资金失败'
    result=Publish.query.filter_by(uuid=uuid).first()
    lis=result.unit_type
    result=Lease.query.filter_by(uuid=uuid).first()
    if result:
        res=Unit_type.query.filter_by(type=lis).first()
        if res:
            res.count=int(res.count)-1
        else:
            data['status']='unit_type查询失败'
        db.session.delete(result)
        db.session.commit()
        db.session.close()
        data['status']='success'
    else:
        data['status']='uuid查询失败'
    return jsonify(data)

@other_blueprint.route('/gettype/<int:page>/<int:size>',methods=['GET'])
def getcount(page,size):
    result=Unit_type.query.paginate(page=page, per_page=size, error_out=True)
    if result:
        lis=[]
        n=0
        for i in result.items:
            data={}
            data['type']=i.type
            n=n+1
            lis.append(data)
        return jsonify(lis)
    else:
        return 'failed'

#获取发布内容
@other_blueprint.route('/getpublishlist/<int:page>/<int:size>',methods=['GET'])
def getpublishlist(page,size):
    result=Publish.query.filter_by(flag='0')
    count=result.count()
    lis=[]
    n=0
    for i in result:
        if n<(int(page-1)*int(size)):
            n=n+1
            continue
        elif n>=int(page)*int(size):
            break
        else:
            content={}
            content['uuid']=i.uuid
            content['username']=i.username
            content['name']=i.name
            content['address']=i.address
            content['room']=i.room
            content['unit_type']=i.unit_type
            content['price']=i.price
            content['link']=i.link
            content['begintime']=i.begintime
            print(i.begintime)
            content['endtime']=i.endtime
            lis.append(content)
            n=n+1
    return jsonify(lis)

#获取租赁信息
@other_blueprint.route('/getleaselist/<int:page>/<int:size>',methods=['GET'])
def getleaselist(page,size):
    result=Publish.query.filter_by(flag='1')
    result=result.paginate(page=page, per_page=size, error_out=True)
    lis=[]
    for i in result.items:
        content={}
        result1=Lease.query.filter_by(uuid=i.uuid).first()
        content['link']=result1.link
        content['username']=result1.username
        content['name']=result1.name

        content['uuid']=i.uuid
        content['address']=i.address
        content['room']=i.room
        content['unit_type']=i.unit_type
        content['price']=i.price
        content['begintime']=i.begintime
        content['endtime']=i.endtime
        content['use']=result1.use
        lis.append(content)
    return jsonify(lis)

#户型管理
@other_blueprint.route('/type_change',methods=['GET','POST','PUT'])
def type_change():
    if request.method=='GET':
        lis=[]
        res=Unit_type.query.all()
        for i in res:
            data={}
            data['type']=i.type
            lis.append(data)
        db.session.close()
        return jsonify(lis)
    if request.method=='POST':
        data={
            'status':''
        }
        find = request.get_json()
        print(find)
        type=find['type']
        method=find['method']
        data={}
        if method=='add':
            result=Unit_type.query.filter_by(type=type).first()
            if result!=None:
                data['status']='户型已存在'
                return data
            unit_type=Unit_type(type=type,count=0)
            db.session.add(unit_type)
            db.session.commit()
            result=Unit_type.query.filter_by(type=type).first()
            if result.type==type:
                data['status']='addsuccess'
                db.session.close()
            else:
                data['status']='添加失败'
            return data
        elif method=='del':
            result=Unit_type.query.filter_by(type=type).first()
            if result==None:
                data['status']='要删除的户型不存在'
                return data
            if str(int(result.count))=='0':
                db.session.delete(result)
                db.session.commit()
                db.session.close()
                data['status']='delsuccess'
            else:
                data['status']='删除失败，因为总数不为0'
            return data
        elif method=='change':
            change=find['change']
            result=Unit_type.query.filter_by(type=type).first()
            if result==None:
                data['status']='要修改的户型不存在'
                return data
            if str(int(result.count))=='0':
                result.type=change
                db.session.commit()
                result=Unit_type.query.filter_by(type=change).first()
                if result.type==change:
                    data['status']='changesuccess'
                    db.session.close()
                else:
                    data['status']='修改失败'
                db.session.close()
            else:
                data['status']='修改失败,因为要修改的户型总数不为0'
            return data

@other_blueprint.route('/del/<int:uuid>',methods=['GET'])
def delpublish(uuid):
    data={}
    result=Publish.query.filter_by(uuid=uuid).first()
    db.session.delete(result)
    db.session.commit()
    result=Publish.query.filter_by(uuid=uuid).first()
    if result==None:
        data['status']='success'
    else:
        data['status']='failed'
    return jsonify(data)

@other_blueprint.route('/getpublishcount',methods=['GET'])
def getpublishcount():
    result=Publish.query.all()
    n=0
    for i in result:
        if str(int(i.flag))=='0':
            n+=1
    return jsonify(n)

@other_blueprint.route('/getleasecount',methods=['GET'])
def getleasecount():
    result=Publish.query.all()
    n=0
    for i in result:
        if str(int(i.flag))=='1':
            n+=1
    return jsonify(n)

@other_blueprint.route('/fbi/<int:id>',methods=['GET'])
def findByID(id):
    i=Publish.query.filter_by(uuid=id).first()
    content={}
    content['uuid']=i.uuid
    content['username']=i.username
    content['name']=i.name
    content['address']=i.address
    content['room']=i.room
    content['unit_type']=i.unit_type
    content['price']=i.price
    content['link']=i.link
    content['begintime']=i.begintime
    content['endtime']=i.endtime
    return jsonify(content)

@other_blueprint.route('/fbilease/<int:id>',methods=['GET'])
def findByIDLease(id):
    find=Lease.query.filter_by(uuid=id).first()
    content={}
    content['uuid']=find.uuid
    content['username']=find.username
    content['name']=find.name
    content['use']=find.use
    content['link']=find.link
    return jsonify(content)

@other_blueprint.route('/updatepublish',methods=['POST','PUT'])
def updatepublish():
    #uuid=request.form['uuid']
    find=request.get_json()
    print(find)
    uuid=find['uuid']
    username=find['username']
    name=find['name']
    address=find['address']
    room=find['room']
    unit_type=find['unit_type']
    #price=find['price']
    link=find['link']
    begintime=int(find['begintime'])/1000
    endtime=int(find['endtime'])/1000
    data={}
    result=Publish.query.filter_by(uuid=uuid).first()
    if result==None:
        data['status']='failed'
        return data
    result.username=username
    result.name=name
    result.address=address
    result.room=room
    result.unit_type=unit_type
    #result.price=price
    result.link=link
    result.begintime=int(begintime)
    result.endtime=int(endtime)
    db.session.commit()
    db.session.close()
    data['status']='success'
    return jsonify(data)

@other_blueprint.route('/updatelease',methods=['POST'])
def updatelease():
    find=request.get_json()
    data={}
    uuid=find['uuid']
    username=find['username']
    name=find['name']
    link=find['link']
    use=find['use']
    result=Lease.query.filter_by(uuid=uuid).first()
    result.username=username
    result.name=name
    result.link=link
    result.use=use
    db.session.commit()
    db.session.close()
    data['status']='success'
    return jsonify(data)

@other_blueprint.route('/gettypecount',methods=['GET'])
def gettypecount():
    result=Unit_type.query.all()
    n=0
    for i in result:
        n+=1
    return jsonify(n)

@other_blueprint.route('/gettypeall/<int:page>/<int:size>',methods=['GET'])
def gettypeall(page,size):
    result=Unit_type.query.paginate(page=page, per_page=size, error_out=True)
    data=[]
    for i in result.items:
        lis={}
        lis['type']=i.type
        lis['count']=i.count
        data.append(lis)
    return jsonify(data)

@other_blueprint.route('/price',methods=['GET'])
def price():
    result=Login.query.filter_by(username=current_user.username).first()
    data=[]
    lis={}
    lis['count']=result.count
    lis['deliver']=result.deliver
    lis['balance']=result.balance
    data.append(lis)
    return jsonify(data)

@other_blueprint.route('/getalldata/<int:page>/<int:size>',methods=['GET'])
def getalldata(page,size):
    result=Publish.query.paginate(page=page, per_page=size, error_out=True)
    data=[]
    for i in result.items:
        lis={}
        lis['uuid']=i.uuid
        lis['username']=i.username
        lis['name']=i.name
        lis['address']=i.address
        lis['room']=i.room
        if str(i.flag)=='0':
            lis['flag']='否'
        else:
            lis['flag']='是'
        data.append(lis)
    return jsonify(data)

