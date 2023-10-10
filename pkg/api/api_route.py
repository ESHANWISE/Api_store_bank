import json
from flask import jsonify,request
from flask_httpauth import HTTPBasicAuth
from pkg.api import apiobj #pkg.admin is anoher way to specify the __init__.py within admin folder
from pkg.models import *


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    deets = db.session.query(Merchants.mer_pwd).filter(Merchants.mer_username==username).first()
    if deets:
        return deets.mer_pwd
    return None

@auth.error_handler
def unauthorized():
    return jsonify({"error":'unauthorized access'}),401


@apiobj.errorhandler(404)
def pagenotfound(error):
    feedback = {"status":0,"data":'The parameter supplied is not correct'}
    return jsonify(feedback),404


@apiobj.route("/listall/",methods=["GET"])

def list_allstores():
    
    allstoress = Store.query.all()
    records = []
    for i in allstoress:
        deets = dict()
        deets["storeName"] = i.store_name
        deets["storePhone"] = i.store_phone
        deets["storeAddress"] = i.store_address
        deets["storePix"] = i.store_pic
        records.append(deets)
    if records:
        feedback = {"status":1,"data":records}
    else:
        feedback = {"status":0,"data":records}
    return jsonify(feedback)

@apiobj.route("/listone/<int:id>/",methods=["GET"])
def list_store(id):
    store_details = db.session.query(Store).get_or_404(id)
    deets = dict()
    deets["storeId"] = store_details.store_id
    deets["storeName"] = store_details.store_name
    deets["storePhone"] = store_details.store_phone
    deets["storeAddress"] = store_details.store_address
    deets["storePix"] = store_details.store_pic
    return jsonify(deets)

@apiobj.route("/addnew/",methods=["POST"])
@auth.login_required
def addnew():
    # {"name":"New store name","phone":"New store phone","address":"new address"}
    if request.is_json:
        jsondata = request.get_json()
        storename = jsondata.get("name")
        storeaddress = jsondata.get("address")
        storephone = jsondata.get("phone")
        storepic = jsondata.get("pic")
        if storename == None or storephone == None or storepic == None:
            feedback = {"status":0,"data":'Please check the JSAON keys from our documentation'}
        else:
            s = Store(store_name=storename,store_address=storeaddress,store_phone=storephone,store_pic=storepic)
            db.session.add(s)
            db.session.commit()
            feedback = {"status":1,'data':"new stores added.."}
    else:
        {"status":0,'data':"You should be supply a json format"}
    return jsonify(feedback)

@apiobj.route("/delete/<int:id>/",methods=["DELETE"])
def delete_store(id):
    deleting = db.session.query(Store).get(id)
    if(Store):
        db.session.delete(deleting)
        db.session.commit()
        feedback = {"status":1,"data":"Store Deleted!"}
    else:
        feedback = {"status":0,"data":"The parameter supplied does not exist"}
    return jsonify(feedback)
    

@apiobj.route("/update/<id>/",methods=["PUT"])
def update_stores(id):
    # {"name":"New store name","phone":"New store phone","address":"new address"}
# request.jason_get() will extract the json in the body of the request
    jsondata = request.get_json()
    deets = Store.query.get(id)
    deets.store_phone = jsondata['phone']
    deets.store_address = jsondata['address']
    db.session.commit()
    return "Store updated"