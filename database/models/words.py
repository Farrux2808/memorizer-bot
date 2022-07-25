from email.policy import default
from app import db
from datetime import datetime

class WordModelClass(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    word = db.Column(db.String)
    definition = db.Column(db.String)
    correct_count = db.Column(db.Integer)
    count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # def __init__(self, client_id, word, definition, correct_count, wrong_count, created_at):
    #     self.client_id = client_id
    #     self.word = word
    #     self.definition = definition
    #     self.correct_count = correct_count,
    #     self.wrong_count = wrong_count,
    #     self.created_at = created_at
        