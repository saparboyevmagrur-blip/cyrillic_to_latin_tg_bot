import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "8673963131:AAFWrC3yDWlEPavQZ7-k5PU7sbcpzhu7LsY"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalom alaykum, botimizga xush kelibsiz")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	text = message.text
	if text.isascii():
		bot.reply_to(message, to_cyrillic(text))
	else: 
		bot.reply_to(message, to_latin(text))

bot.infinity_polling()