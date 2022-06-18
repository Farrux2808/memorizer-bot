from lib2to3.pytree import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModelClass(Base): 
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    full_name = Column(String)
    phone = Column(String)
    chat_id = Column(Integer)
    menu_url = Column(String, nullable=True)
    def __repr__(self):
            return "<User(user_id='%s', full_name='%s', phone='%s', chat_id'%s', menu_url='%s')>" % (
                                    self.user_id, self.full_name, self.phone, self.chat_id, self.menu_url)