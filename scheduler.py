import schedule
import time
import telegram
import commands
import time
from telegram import (
    Poll,
)
from app import db, updater
from domain import UserRepository, User, Word, WordRepository
import random



def quizCreater(client_id):
    words =  WordRepository.creatQuiz(client_id)
    if len(words) >= 4:
        quiz = {
            "question": words[0].getWord(),
            "options": [words[0].getDefinition(), words[1].getDefinition(), words[2].getDefinition(), words[3].getDefinition()],
            "correct": 1
        }
        tmp = []
        for i in range(4):
            dif = random.choice(quiz["options"])
            tmp.append(dif)
            quiz["options"].remove(dif)
            if dif == words[0].getDefinition():
                quiz["correct"] = i
        quiz["options"] = tmp
        words[0].buildCount(words[0].getCount() + 1)
        WordRepository.update(words[0])
        return quiz
    else:
        return False

def job():
    users = UserRepository.gettAll()
    t = int(time.time()) // 60
    for user in users:
        if t % user.interval == 0:
            quiz = quizCreater(user.id)
            # bot.send_message(chat_id=user.chat_id, text = 'hello')
            if quiz:
                bot.send_poll(chat_id=user.chat_id, type = Poll.QUIZ, question=quiz["question"], options=quiz["options"], correct_option_id=quiz["correct"])

schedule.every(1).minutes.do(job)

# bot = telegram.Bot(token="5210098659:AAEeJTWsjl_j9MyL598eR2iHXYLWieqwWag")
bot = updater.bot
# mycursor = mydb.cursor()
while True:
    schedule.run_pending()
    time.sleep(1)


