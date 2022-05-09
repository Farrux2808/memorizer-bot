import telegram
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from PyDictionary import PyDictionary

dictionary=PyDictionary()

telegram_bot_token = "5210098659:AAEeJTWsjl_j9MyL598eR2iHXYLWieqwWag"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello there. Provide any English word and I will give you a bunch "
                                                   "of information about it.")


# obtain the information of the word provided and format before presenting.
def get_word_info(update, context):
    # get the word info
    word_info = dictionary.meaning(update.message.text)
    print(word_info)

    # If the user provides an invalid English word, return the custom response from get_info() and exit the function
    if word_info.__class__ is str:
        update.message.reply_text(word_info)

    message = f"text: {1+1}"

    update.message.reply_text(message)

# run the start function when the user invokes the /start command 
dispatcher.add_handler(CommandHandler("start", start))

# invoke the get_word_info function when the user sends a message 
# that is not a command.
dispatcher.add_handler(MessageHandler(Filters.text, get_word_info))
updater.start_polling()