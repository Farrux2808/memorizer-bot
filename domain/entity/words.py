from app import db
from database import WordModelClass
class Word:
    _id: db.Integer
    _word: db.String
    _definition: db.String
    _correct_count: db.Integer
    _count: db.Integer
    _created_at: db.DateTime
    _client_id: db.Integer

    def buildId(self, id):
        self._id = id
        return self

    def buildWord(self, word):
        self._word = word
        return self
    
    def buildDefinition(self, definition):
        self._definition = definition
        return self

    def buildCorrectCount(self, correct_count):
        self._correct_count = correct_count
        return self

    def buildCount(self, count):
        self._count = count
        return self

    def buildClientId(self, client_id):
        self._client_id = client_id
        return self


    def getId(self):
        return self._id
        
    def getWord(self):
        return self._word

    def getDefinition(self):
        return self._definition

    def getCorrectCount(self):
        return self._correct_count
    
    def getCount(self):
        return self._count
    
    def getClientID(self):
        return self._client_id

    def convertToEntity(self, word: WordModelClass):
        if word:
            self.buildId(word.id)
            self.buildWord(word.word)
            self.buildClientId(word.client_id)
            self.buildCorrectCount(word.correct_count)
            self.buildCount(word.count)
            self.buildDefinition(word.definition)
            return self
        else:
            return None

    def convertToModelClass(self):
        word = WordModelClass()
        word.word = self.getWord()
        word.definition = self.getDefinition()
        word.correct_count = self.getCorrectCount()
        word.count = self.getCount()
        word.client_id = self.getClientID()
        return word