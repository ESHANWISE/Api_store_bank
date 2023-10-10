from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Store(db.Model):
    store_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    store_name=db.Column(db.String(120),nullable=False)
    store_phone=db.Column(db.String(50),nullable=False)
    store_address=db.Column(db.String(200),nullable=False)
    store_pic=db.Column(db.String(200),nullable=False)


class Merchants(db.Model):
    mer_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    mer_username=db.Column(db.String(100),nullable=True)
    mer_pwd=db.Column(db.String(255),nullable=True)
    mer_dateadded = db.Column(db.DateTime(),default=datetime.utcnow)