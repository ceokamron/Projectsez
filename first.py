import telebot

bot = telebot.TeleBot('6966071597:AAEVl1ujZ6wqjxW1Lm--VMV0vwepN1-pyJQ')

@bot.message_handler(commands = ['command1', 'start'])
def first(message):
    bot.send_message(message.chat.id, f'Assalomu Aleykum, {message.from_user.first_name}') #{message.from_user.last_name}

@bot.message_handler(commands= ['command2', 'aloqa'])
def first(message):
    bot.send_message(message.chat.id, 'Dostavka xizmati  +998933282828')

@bot.message_handler(commands = ['command3', 'Manzil'])
def first(message):
    bot.send_message(message.chat.id, 'Manzilimiz Guliston Shahar, 2 mikrarayon, Uzbekistan ko`chasi, Saxovat Savdo Markazi')
    
bot.infinity_polling()
