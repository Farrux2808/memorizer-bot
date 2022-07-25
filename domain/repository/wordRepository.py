from domain import Word
from database import WordModelClass
from app import db
from sqlalchemy import desc, asc

class WordRepository:

    def creat(_word: Word):
        word = _word.convertToModelClass()
        db.session.add(word)
        db.session.commit()
        return _word
    
    def update(_word: Word):
        word = db.session.query(WordModelClass).filter_by(id=_word.getId()).first()
        if _word.getWord():
            word.word = _word.getWord()
        if _word.getDefinition():
            word.definition = _word.getDefinition()
        if _word.getCorrectCount():
            word.correct_count = _word.getCorrectCount()
        if _word.getCount():
            word.count = _word.getCount()
        db.session.commit()

    def delete(_word: Word):
        word = db.session.query(WordModelClass).filter_by(id=_word.getId()).first()
        db.session.delete(word)

    def sncById(_id):
        word = Word().convertToEntity(db.session.query(WordModelClass).filter_by(id=_id).first())
        return word

    def sncByUserId(_client_id):
        words = db.session.query(WordModelClass).filter_by(client_id=_client_id).all()
        return words

    def creatQuiz(_client_id):
        words = db.session.query(WordModelClass).filter_by(client_id=_client_id).order_by(asc(WordModelClass.count)).limit(10).all()
        wordss = []
        for word in words:
            wordss.append(Word().convertToEntity(word))
        return wordss

