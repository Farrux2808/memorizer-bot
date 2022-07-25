from domain import User
from database import UserModelClass
from app import db

class UserRepository:

    def creat(_user: User):
        user = _user.convertToModelClass()
        db.session.add(user)
        db.session.commit()
        return _user
    
    def update(_user: User):
        user = db.session.query(UserModelClass).filter_by(id=_user.getId()).first()
        if _user.getFullName():
            user.full_name = _user.getFullName()
        if _user.getInterval():
            user.interval = _user.getInterval()
        if _user.getMenuUrl():
            user.menu_url = _user.getMenuUrl()
        if _user.getTmp():
            user.tmp = _user.getTmp()
        db.session.commit()

    def sncById(_id):
        user = User().convertToEntity(db.session.query(UserModelClass).filter_by(id=_id).first())
        # db.session.commit()
        return user

    def sncByUserId(_userId):
        user = User().convertToEntity(db.session.query(UserModelClass).filter_by(user_id=_userId).first())
        # db.session.commit()
        return user


    def gettAll():
        users = db.session.query(UserModelClass).filter_by().all()
        return users


