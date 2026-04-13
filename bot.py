import telebot

TOKEN = "8761594910:AAHfZb3ugCjSr80CnWTYqx7RV-ftmb6xJyU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Halo sayang 😏 Nina selalu di sini buat kamu...")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Kamu bilang: " + message.text)

print("Bot jalan...")
bot.infinity_polling()
