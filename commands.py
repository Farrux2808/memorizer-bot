from turtle import up
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import (
    Poll,
    ParseMode,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)


def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="HI, I'm Mmorizer bot. I will help you for learn new words")
    contact(update, context)


def echo(update,context):
   bot = context.bot
   city_name = update.message.text
   chat_id = update.message.from_user.id
   bot.sendMessage(chat_id, city_name)
   print(chat_id)



# def quiz(update: Update, context: CallbackContext) -> None:
#     if not checkUser(update.message.chat.id):
#         return
#     questions = ["1", "2", "4", "20"]
#     message = update.effective_message.reply_poll(
#         "How many eggs do you need for a cake?", questions, type=Poll.QUIZ, correct_option_id=2
#     )
#     payload = {
#         message.poll.id: {"chat_id": update.effective_chat.id, "message_id": message.message_id}
#     }
#     context.bot_data.update(payload)


# def receive_quiz_answer(update: Update, context: CallbackContext) -> None:
#     if not checkUser(update.message.chat.id):
#         return
#     if update.poll.is_closed:
#         return
#     if update.poll.total_voter_count == 3:
#         try:
#             quiz_data = context.bot_data[update.poll.id]
#             print(quiz_data)
#         except KeyError:
#             return
#         context.bot.stop_poll(quiz_data["chat_id"], quiz_data["message_id"])


def contact(update: Update, context: CallbackContext):
    contact_keyboard = telegram.KeyboardButton(text="SIGN UP",request_contact=True)
    reply_markup = telegram.ReplyKeyboardMarkup([[ contact_keyboard ]], resize_keyboard=True)
    update.message.reply_text("Please register to use the bot.", reply_markup=reply_markup)

# def contact_callback(update: Update, context: CallbackContext):
#     contact = update.effective_message.contact
#     settens_btn = telegram.KeyboardButton(text="Settengs")
#     add_btn = telegram.KeyboardButton(text="Add word")
#     reply_markup = telegram.ReplyKeyboardMarkup([[ settens_btn, add_btn ]], resize_keyboard=True)
#     update.message.reply_text("You successfully registered!", reply_markup=reply_markup)
#     if not checkUser(update.message.chat.id):
#         mycursor = mydb.cursor()
#         sql = "INSERT INTO `client` (`user_id`, `full_name`, `phone`, `interval`, `chat_id`) VALUES (%s, %s, %s, %s, %s)"
#         val = (contact.user_id, contact.first_name + ' ' + contact.last_name, contact.phone_number, 10, update.message.chat_id)
#         mycursor.execute(sql, val)
#         mydb.commit()

# def checkUser(user_id):
#     mycursor = mydb.cursor()
#     mycursor.execute(f"SELECT * FROM client WHERE user_id = '{user_id}'")
#     user = mycursor.fetchone()
#     if user:
#         return user
#     else:
#         return False

# def getUsers():
#     mycursor = mydb.cursor()
#     mycursor.execute(f"SELECT * FROM client")
#     users = mycursor.fetchall()
#     return users


