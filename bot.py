import os
import telebot

TOKEN = os.getenv('TELEGRAM_TOKEN')
if not TOKEN:
    print("ERROR: TELEGRAM_TOKEN not set!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Trading Bot Aktif!")

@bot.message_handler(commands=['price'])
def price(message):
    bot.reply_to(message, "Bitcoin: $40,000")

@bot.message_handler(commands=['signal'])
def signal(message):
    bot.reply_to(message, "Signal: BUY BTC")

print("Bot starting...")
bot.polling(none_stop=True)
