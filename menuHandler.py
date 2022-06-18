import commands

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
    }
}

def menuHandler(update, context):
    user = commands.checkUser(update.message.chat.id)
    if not user:
        return
    chat_id = update.effective_chat.id
    print(update.message)
    context.bot.send_message(chat_id=chat_id, text=update.message.text)