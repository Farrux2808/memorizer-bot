import logging
import mysql.connector
from telegram.ext import (
    Updater,
    CommandHandler,
    PollHandler,
    MessageHandler,
    Filters,
)
import commands
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

url = 'mysql://mrvirus:Pass_123@localhost/memorizer'
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="mrvirus",
#   password="Pass_123",
#   database="memorizer"
# )

telegram_bot_token = "5210098659:AAEeJTWsjl_j9MyL598eR2iHXYLWieqwWag"


def main() -> None:
    updater = Updater(token=telegram_bot_token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", commands.start))
    # dispatcher.add_handler(CommandHandler("quiz", commands.quiz))
    # dispatcher.add_handler(CommandHandler("a", Contact))
    # dispatcher.add_handler(PollHandler(commands.receive_quiz_answer))
    # dispatcher.add_handler(MessageHandler(Filters.contact ,commands.contact_callback))
    dispatcher.add_handler(MessageHandler(Filters.text ,commands.echo))
    # dispatcher.add_handler(CommandHandler("Settings", commands.quiz))
    updater.start_polling()

if __name__ == "__main__":
    main()
