from app import db
from database import UserModelClass
class User:
    _id: db.Integer
    _userId: db.Integer
    _fullName: db.String
    _phone: db.String
    _chatId: db.Integer
    _menuUrl: db.String
    _interval: db.Integer
    _tmp: db.String

    def buildId(self, id):
        self._id = id
        return self

    def buildUserId(self, userId):
        self._userId = userId
        return self
    
    def buildFullName(self, fullName):
        self._fullName = fullName
        return self

    def buildPhone(self, phone):
        self._phone = phone
        return self

    def buildChatId(self, chatId):
        self._chatId = chatId
        return self

    def buildMenuUrl(self, menuUrl):
        self._menuUrl = menuUrl
        return self

    def buildIntervel(self, interval):
        self._interval = interval
        return self
        
    def buildTmp(self, tmp):
        self._tmp = tmp
        return self


    def getId(self):
        return self._id
        
    def getUserId(self):
        return self._userId

    def getFullName(self):
        return self._fullName

    def getPhone(self):
        return self._phone
    
    def getChatId(self):
        return self._chatId
    
    def getMenuUrl(self):
        return self._menuUrl

    def getInterval(self):
        return self._interval

    def getTmp(self):
        return self._tmp


    def convertToEntity(self, user: UserModelClass):
        if user:
            self.buildId(user.id)
            self.buildChatId(user.chat_id)
            self.buildFullName(user.full_name)
            self.buildPhone(user.phone)
            self.buildUserId(user.user_id)
            self.buildMenuUrl(user.menu_url)
            self.buildIntervel(user.interval)
            self.buildTmp(user.tmp)
            return self
        else:
            return None

    def convertToModelClass(self):
        user = UserModelClass()
        user.user_id = self.getUserId()
        user.full_name = self.getFullName()
        user.phone = self.getPhone()
        user.menu_url = self.getMenuUrl()
        user.chat_id = self.getChatId()
        user.interval = self.getInterval()
        user.tmp = self.getTmp()
        return user