# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 上午11:09
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : test.py
# @Software: PyCharm


from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,Boolean,DateTime,ForeignKey
from models import engine
from sqlalchemy.orm import relationship,backref
from models import session
from models import Base

class User(Base):

    print("开始创建user表")
    __tablename__ = 'my_twitter_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    phone_num = Column(String(64),nullable=False)
    user_name = Column(String(60),nullable=False)
    email = Column(String(64),nullable=True)
    password = Column(String(100),nullable=False)
    create_time = Column(DateTime,default=datetime.now())
    last_login = Column(DateTime)
    lonin_num = Column(Integer,default=0)
    # home_twitter = relationship('HomeTwitterList',backref('user',))

    @classmethod
    def all(self,cls):
        return session.query(cls).all()

    @classmethod
    def by_id(self,cls,id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def by_name(self,cls,name):
        return session.query(cls).filter_by(user_name=name).first()

    @classmethod
    def by_phone_num(self,cls,phoneNum):
        return session.query(cls).filter_by(phone_num=phoneNum).first()

    @classmethod
    def by_email(self,cls,Email):
        return session.query(cls).filter_by(email=Email).first()


class HomeTwitterList(Base):

    print("开始创建homeList表")
    __tablename__ = 'home_twitter_list'
    id = Column(Integer,primary_key=True,autoincrement=True)
    retwitterType = Column(String(32),nullable=False)
    retwitterAccount = Column(String(32),nullable=False)
    avatarImage = Column(String(8),nullable=False)
    account = Column(String(32),nullable=False)
    nickName = Column(String(32),nullable=False)
    time = Column(String(32),nullable=False)
    content = Column(String(160),nullable=False)
    contentImages = Column(String(64),nullable=False)
    contentVideo = Column(String(16),nullable=False)
    commentCount = Column(String(16),nullable=False)
    retwitterCount = Column(String(16),nullable=False)
    likeCount = Column(String(16),nullable=False)
    privateMessageCount = Column(String(16),nullable=False)
    # user_id = (Integer,ForeignKey('user.id'))

    @classmethod
    def all(self, cls):
        return session.query(cls).all()