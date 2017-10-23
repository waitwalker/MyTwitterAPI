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
from sqlalchemy.orm import relationship
from models import session
from models import Base


class AboutTwitter(Base):
    print('开始创建关于表')
    __tablename__ = 'about_twitter'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32),nullable=False)
    urlString = Column(String(64),nullable=False)
    type = Column(String(24),nullable=False)
    subType = Column(String(4),nullable=False)

    @classmethod
    def all(self,cls):
        return session.query(cls).all()