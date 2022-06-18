from curses.ascii import US
from http.client import IM_USED
from lib2to3.pytree import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
import datetime
from .users import UserModelClass

Base = declarative_base()

class WordModelClass(Base): 
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("user.id"))
    word = Column(String)
    definition = Column(String)
    correct_count = Column(Integer)
    wrong_count = Column(Integer)
    created_ar = Column(DateTime, default=datetime.datetime.utcnow)
    def __repr__(self):
            return "<User(client_id='%s', word='%s', definition='%s', correct_count'%s', wrong_count='%s', created_ar='%s')>" % (
                                    self.client_id, self.word, self.definition, self.correct_count, self.wrong_count, self.created_ar)