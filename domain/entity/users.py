from distutils.command.build import build
from hashlib import new
from tokenize import String
from sqlalchemy import Integer, String, null
from database import UserModelClass
class User:
    _id: Integer
    _userId: Integer
    _fullName: String
    _phone: String
    _chatId: Integer
    _menuUrl: String

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


    def convertToentity(self, user: UserModelClass):
        self.buildChatId(user.chat_id)
        self.buildFullName(user.full_name)
        self.buildPhone(user.phone)
        self.buildUserId(user.user_id)
        self.buildMenuUrl(user.menu_url)
        return self

    def convertToModelClass(self):
        user = UserModelClass()
        user.user_id = self.getUserId()
        user.full_name = self.getFullName()
        user.phone = self.getPhone()
        user.menu_url = self.getMenuUrl()
        user.chat_id = self.getChatId()
        return user