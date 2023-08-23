import telebot

TOKEN = 'YOUR TOKEN'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def filter_messages(message):
    offensive_words = ['', '', '', '']  
    if any(word in message.text.lower() for word in offensive_words):
        bot.delete_message(message.chat.id, message.message_id)

bot.polling()