import telegram
from telegram import (
    Poll,
    Update,
)
from telegram.ext import (
    CallbackContext,
)
from domain import UserRepository, User, Word, WordRepository
from app import db

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="HI, I'm Mmorizer bot. I will help you for learn new words")
    contact(update, context)


def echo(update,context):
   bot = context.bot
   city_name = update.message.text
   chat_id = update.message.from_user.id
#    user = UserModelClass.query.all()
   bot.sendMessage(chat_id, city_name)
#    print(user[0].full_name)



def quiz(update: Update, context: CallbackContext) -> None:
    if not checkUser(update.message.chat.id):
        return
    questions = ["1", "2", "4", "20"]
    message = update.effective_message.reply_poll(
        "How many eggs do you need for a cake?", questions, type=Poll.QUIZ, correct_option_id=2
    )
    payload = {
        message.poll.id: {"chat_id": update.effective_chat.id, "message_id": message.message_id}
    }
    context.bot_data.update(payload)


def receive_quiz_answer(update: Update, context: CallbackContext) -> None:
    print(update)
    print("********")
    print(context.chat_data)
    # if not checkUser(update.message.chat.id):
    #     return
    # if update.poll.is_closed:
    #     return
    # if update.poll.total_voter_count == 3:
    #     try:
    #         quiz_data = context.bot_data[update.poll.id]
    #         print(quiz_data)
    #     except KeyError:
    #         return
    #     context.bot.stop_poll(quiz_data["chat_id"], quiz_data["message_id"])


def contact(update: Update, context: CallbackContext):
    contact_keyboard = telegram.KeyboardButton(text="SIGN UP",request_contact=True)
    reply_markup = telegram.ReplyKeyboardMarkup([[ contact_keyboard ]], resize_keyboard=True)
    update.message.reply_text("Please register to use the bot.", reply_markup=reply_markup)

def contact_callback(update: Update, context: CallbackContext):
    contact = update.effective_message.contact
    settens_btn = telegram.KeyboardButton(text="Settengs")
    add_btn = telegram.KeyboardButton(text="Add word")
    reply_markup = telegram.ReplyKeyboardMarkup([[ settens_btn, add_btn ]], resize_keyboard=True)
    if not checkUser(update.message.chat.id):
        user = User()
        user.buildChatId(update.message.chat_id)
        user.buildFullName(contact.first_name + ' ' + contact.last_name)
        user.buildIntervel(10)
        user.buildUserId(contact.user_id)
        user.buildMenuUrl('/')
        user.buildPhone(contact.phone_number)
        user.buildTmp('-')
        UserRepository.creat(user)
    update.message.reply_text("You successfully registered!", reply_markup=reply_markup)

def checkUser(user_id):
    user = UserRepository.sncByUserId(user_id)
    if user:
        return user
    else:
        return False
