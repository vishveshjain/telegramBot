import telebot
import requests
import config

Token = config.QuotesToken
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to random Quotes. Please hit /help to find out more and my full potential")

@bot.message_handler(commands=['help'])
def help(message):
    help_text = """Commands:
/start - Greeting
/help - Show command list
/quotes - Show one random quote at a time"""
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['quotes'])
def quotes(message):
    response = requests.get("https://zenquotes.io/api/image")
    if response.status_code == 200:
        image_content = response.content
        bot.send_photo(message.chat.id, photo=image_content)
    else:
        bot.reply_to(message, "Failed to fetch quote.")

bot.polling()
