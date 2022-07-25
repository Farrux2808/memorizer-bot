import commands
import telegram

menu = {
    'Settings': {
        '5': 'btn1',
        '10': 'btn2',
        '30': 'btn3',
        '60': 'btn4',
        'back': 'btn'
    },
    'Add word': {
        'add': 'add_com',
        'addDef': 'add_def_com',
        'back': 'btn'
    },
    "Test": {
        'Last 10': 'last10',
        'Last 30': 'last20',
        'Last 50': 'last50',
        'back': 'btn'
    }
}

def menuHandler(update, context):
    user = commands.checkUser(update.message.chat.id)
    global menu
    if not user:
        return
    com = update.message.text
    chat_id = update.effective_chat.id
    if user.getMenuUrl() == '/':
        if com== 'Add word':
            keybordButtons = [telegram.KeyboardButton(text='back')]
            reply_markup = telegram.ReplyKeyboardMarkup([keybordButtons], resize_keyboard=True)
            user.buildMenuUrl("Add word")
            update.message.reply_text("Please, enter a word", reply_markup=reply_markup)
        elif com == "Settings":
            keybordButtons = []
            for btn in menu['Settings']:
                keybordButtons.append(telegram.KeyboardButton(text=btn))
            reply_markup = telegram.ReplyKeyboardMarkup([keybordButtons], resize_keyboard=True)
            user.buildMenuUrl("Settings")
            update.message.reply_text("Please, select the to sent poll interval", reply_markup=reply_markup)
        elif com == "Test":
            keybordButtons = []
            for btn in menu['Test']:
                keybordButtons.append(telegram.KeyboardButton(text=btn))
            reply_markup = telegram.ReplyKeyboardMarkup([keybordButtons], resize_keyboard=True)
            user.buildMenuUrl("Test")
            update.message.reply_text("Please, select test", reply_markup=reply_markup)
        else:
            keybordButtons = []
            for btn in menu:
                keybordButtons.append(telegram.KeyboardButton(text=btn))
            reply_markup = telegram.ReplyKeyboardMarkup([keybordButtons], resize_keyboard=True)
            user.buildMenuUrl("/")
            update.message.reply_text("Invalid command", reply_markup=reply_markup)
    elif len(user.getMenuUrl().split('/'))  == 1:
        if com == "back":
            keybordButtons = []
            for btn in menu:
                keybordButtons.append(telegram.KeyboardButton(text=btn))
            reply_markup = telegram.ReplyKeyboardMarkup([keybordButtons], resize_keyboard=True)
            user.buildMenuUrl("/")
            update.message.reply_text("Main menu", reply_markup=reply_markup)
        elif user.getMenuUrl() == "Add word":
            user.buildTmp(com)
            user.buildMenuUrl('Add word/def')
            context.bot.send_message(chat_id=chat_id, text="Please, enter a definition")
        elif user.getMenuUrl() == "Settings":
            if com.isnumeric():
                keybordButtons = []
                for btn in menu:
                    keybordButtons.append(telegram.KeyboardButton(text=btn))
                reply_markup = telegram.ReplyKeyboardMarkup([keybordButtons], resize_keyboard=True)
                user.buildMenuUrl("/")
                user.buildIntervel(int(com))
                update.message.reply_text("Main menu", reply_markup=reply_markup)
            elif com == 'back':
                keybordButtons = []
                for btn in menu:
                    keybordButtons.append(telegram.KeyboardButton(text=btn))
                reply_markup = telegram.ReplyKeyboardMarkup([keybordButtons], resize_keyboard=True)
                user.buildMenuUrl("/")
                update.message.reply_text("Main menu", reply_markup=reply_markup)
            else:
                context.bot.send_message(chat_id=chat_id, text="Something wrong")
    elif len(user.getMenuUrl().split('/'))  == 2:
        if user.getMenuUrl() == 'Add word/def' and com == "back":
            keybordButtons = []
            for btn in menu:
                keybordButtons.append(telegram.KeyboardButton(text=btn))
            reply_markup = telegram.ReplyKeyboardMarkup([keybordButtons], resize_keyboard=True)
            user.buildMenuUrl("/")
            update.message.reply_text("Main menu", reply_markup=reply_markup)
        elif user.getMenuUrl().split('/')[1] == 'def' and user.getTmp() != '-':
            word = commands.Word()
            word.buildWord(user.getTmp())
            word.buildDefinition(com)
            word.buildClientId(user.getId())
            word.buildCorrectCount(0)
            word.buildCount(0)
            commands.WordRepository.creat(word)
            user.buildTmp('-')
            user.buildMenuUrl('Add word')
            context.bot.send_message(chat_id=chat_id, text="Added successfuly")
        else:
            context.bot.send_message(chat_id=chat_id, text="Something wrong")
    commands.UserRepository.update(user)
    # print(update.message)
