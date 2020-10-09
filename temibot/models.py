from temibot import db
from datetime import datetime
#import dropbox
import os



class User(db.Model):

    __tablename__ = 'users'
    
    #id = db.Column(db.Integer,primary_key=True)
    phone_num = db.Column(db.String(64), primary_key = True)
    email = db.Column(db.String(64),nullable = True,unique=True,index=True)
    full_name = db.Column(db.String(70), nullable = True)

    def __init__(self, phone_num, email, full_name):
        self.phone_num = phone_num
        self.email = email
        self.full_name = full_name

    def __repr__(self):
        return f" Phone Number: {self.phone_num}, Full Name: {self.full_name}"