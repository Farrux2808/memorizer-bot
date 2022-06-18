import schedule
import time
import telegram
import commands
from telegram import (
    Poll,
)

def job():
    print("I'm working...")
    users = commands.getUsers()
    question = "How many eggs do you need for a cake?"
    options = ["1", "2", "4", "20"]
    for user in users:
        print(user)
        bot.send_message(chat_id=user[5], text = 'hello')
        bot.send_poll(chat_id=user[5], type = Poll.QUIZ, question=question, options=options, correct_option_id=2)


schedule.every(0.5).minutes.do(job)

bot = telegram.Bot(token="5210098659:AAEeJTWsjl_j9MyL598eR2iHXYLWieqwWag")
# mycursor = mydb.cursor()
while True:
    schedule.run_pending()
    time.sleep(1)