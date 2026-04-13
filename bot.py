import telebot
import os

TOKEN = os.getenv("8761594910:AAG984I89hleez6DUQ4DK_dbOYrsMeL7FkI")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Halo sayang 😏 Bot kamu sudah aktif!")

print("Bot jalan...")
bot.infinity_polling()
