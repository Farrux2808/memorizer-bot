from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import telegram
import commands
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mrvirus:Pass_123@localhost/memorizer'
# db = SQLAlchemy(app)

global bot
bot = telegram.Bot('5210098659:AAEeJTWsjl_j9MyL598eR2iHXYLWieqwWag')

@app.route('/data',methods=['POST','GET'])
def get_data():
    if request.method=='POST':
        dp = Dispatcher(bot,None,workers=0)

        update = telegram.Update.de_json(request.json,bot)

        dp.add_handler(CommandHandler('start', commands.start))
        #   dp.add_handler(CommandHandler('translate', translate))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, commands.echo))
        #   dp.add_handler(MessageHandler(Filters.location, callback=location_user))

        dp.add_handler(MessageHandler(Filters.text, commands.echo))
        dp.process_update(update)
    bot.sendMessage(163899163, 'asfsdfsdfsd testeestsets')
    return {'error':0}

if __name__ == '__main__':
    s = bot.setWebhook("https://memorizer-bot.herokuapp.com/verify")
    app.run(debug=True)