from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,Boolean,DateTime,ForeignKey
from models import engine
from sqlalchemy.orm import relationship
from models import session

#创建基类
Base = declarative_base(engine)

class User(Base):
    __tablename__ = 'my_twitter_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_name = Column(String(60),nullable=False)
    password = Column(String(100),nullable=False)
    create_time = Column(DateTime,default=datetime.now())
    last_login = Column(DateTime)
    lonin_num = Column(Integer,default=0)

    @classmethod
    def all(self,cls):
        return session.query(cls).all()

    @classmethod
    def by_id(self,cls,id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def by_name(self,cls,name):
        return session.query(cls).filter_by(user_name=name).first()

