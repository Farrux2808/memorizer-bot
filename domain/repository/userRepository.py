from domain import User
from database import UserModelClass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class UserRepository:

    def __init__(self, engine) -> None:
        self.engine = engine
    
    def creat(self, _user: User):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user = _user.convertToModelClass()
        session.add(user)
        session.commit()
        return _user
    
    def update(self, _user: User):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user = session.query(User).filter_by(id=_user.getId).first()
        for col in _user.convertToModelClass:
            print(col)
        # session.add(user)
        # session.commit()
        # return _user

    def sncById(self, _id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user = session.query(User).filter_by(id=_id).first()
        return user

