# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 上午11:09
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : test.py
# @Software: PyCharm

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HostName = '127.0.0.1'
Port = '3306'
DataBase = 'twitter_database'
UserName = 'root'
Password = 'etiantian'

create_engine_base_string = 'mysql+pymysql://%s:%s@%s/%s?%s'%(UserName,Password,HostName,DataBase,"charset=utf8")

# 创建引擎
engine = create_engine(create_engine_base_string,encoding='utf-8',echo=True)

#创建基类
Base = declarative_base(engine)

#生成一个session类
Session_Class = sessionmaker(bind=engine)
session = Session_Class()

