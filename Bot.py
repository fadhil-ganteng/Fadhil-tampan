import os
import telebot
from flask import Flask, request

TOKEN = '998838354:AAHcvArqzmA6KxgCwue5T4TmEAr6H_hpNRY'
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)
url='https://i.imgur.com/WggW5Lk.jpg'

def sendmsg(message,text):
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['start'])
def startmsg(message):
    bot.send_message(message.chat.id,'<b>Sugeng Rawuh dateng tukiman bot</b>\ncoba ketik <b>Kulanuwun</b> trus mangke bakal dibales',parse_mode='HTML')

@bot.message_handler(func=lambda msg: msg.text is not None)
def reply_to_message(message):
    if 'Kulanuwun' in message.text.lower():
        sendmsg(message,'Hai, {} sempak'.format(message.from_user.first_name))
    elif 'kulanuwun' in message.text.lower():
        sendmsg(message, 'Hai, {} sempak'.format(message.from_user.first_name))

def reply_to_message(message):
    if 'piye' in message.text.lower():
        sendmsg(message,'apik su'.format(message.from_user.first_name))
    elif 'Piye' in message.text.lower():
        sendmsg(message, 'apik su'.format(message.from_user.first_name))

#bagian server
@server.route('/' + TOKEN,methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return 'ok webhook sudah terpasang !', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://tukiman-bot.herokuapp.com/'+TOKEN)
    return 'hai sayang', 200

if __name__ == '__main__':
    server.run(host="0.0.0.0",port=int(os.environ.get('PORT',5000)))
