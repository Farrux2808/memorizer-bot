from telegram.ext import (
    Updater,
    CommandHandler,
    PollHandler,
    PollAnswerHandler,
    MessageHandler,
    Filters,
)
import commands
import menuHandler
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
# import redis
import os

app = Flask(__name__)
telegram_bot_token = os.environ.get("BOT_TOKEN")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mariadb+pymysql://{os.environ.get("DB_USERNAME")}:{os.environ.get("DB_PASSWORD")}@127.0.0.1/memorizer'
db = SQLAlchemy(app)
# r = redis.Redis(
#     host='localhost',
#     port=6379)
updater = Updater(token=telegram_bot_token, use_context=True)

def main() -> None:
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", commands.start))
    dispatcher.add_handler(CommandHandler("quiz", commands.quiz))
    # dispatcher.add_handler(CommandHandler("a", Contact))
    # dispatcher.add_handler(PollHandler(commands.receive_quiz_answer, pass_chat_data=True, pass_user_data=True))
    # dispatcher.add_handler(PollAnswerHandler(commands.receive_quiz_answer,  pass_chat_data=True, pass_user_data=True))
    dispatcher.add_handler(MessageHandler(Filters.contact ,commands.contact_callback))
    dispatcher.add_handler(MessageHandler(Filters.text ,menuHandler.menuHandler))
    # dispatcher.add_handler(CommandHandler("Settings", commands.quiz))
    updater.start_polling()

@app.route('/start',methods=['POST','GET'])
def get_data():
    main()
    # bot = threading.Thread(target=main)
    # bot.start()
    return { 
        "error": 0
    }

if __name__ == "__main__":
    app.run(debug=True)
    
