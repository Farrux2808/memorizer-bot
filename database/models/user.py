from app import db


class UserModelClass(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    full_name = db.Column(db.String)
    phone = db.Column(db.String)
    chat_id = db.Column(db.Integer)
    menu_url = db.Column(db.String, nullable=True)
    interval = db.Column(db.Integer)
    tmp = db.Column(db.String, nullable=True)

    # def __init__(self, user_id, full_name, phone, chat_id, menu_url):
    #     self.user_id = user_id
    #     self.full_name = full_name
    #     self.phone = phone
    #     self.chat_id = chat_id,
    #     self.menu_url = menu_url