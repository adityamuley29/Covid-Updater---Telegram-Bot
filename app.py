from flask import Flask, request
import telebot
from telegramBot.server import *
from telegramBot.credentials import *
import time


TOKEN = bot_token
bot = telebot.TeleBot(TOKEN)

# flask app starts below
app = Flask(__name__)

# start function below


@bot.message_handler(commands=['start', 'Start', 'Hello', 'hello'])
def start(message):
    bot_welcome = """
       Welcome to India Corona Cases Update bot, the bot is using the service from https://api.covid19india.org/data.json to fetch the Updated data of all States across INDIA.
       """
    bot.send_chat_action(message.chat.id, action="typing", timeout=1.5)
    bot.send_message(message.chat.id, bot_welcome)
    time.sleep(2.0)
    commands = "Plese Select the following to get update.\n/start - To start the Bot.\nEnter State Name - To get update about that state.\n/indiaupdate - To get the Total Cases of India.\n/help - Stuck! Get some help here."
    bot.send_message(message.chat.id, commands)


# State cases function below

def state(message):
    request = message.text.lower()

    if len(request) > 0:
        return True
    else:
        return False


@bot.message_handler(func=state)
def responses(message):

    response = searchedData(message.text)
    if response != None and response != "indiaupdate" and response != "/help":
        result = f"----------Data of {message.text.upper()}-----------\nActive cases:-{response[0]}\nConfirmed cases:-{response[1]}\nDeaths cases:-{response[2]}\nRecovered cases:-{response[3]}\n\nLast Updated:-{response[4]} "
        bot.send_message(message.chat.id, result)
    elif(message.text == "/indiaupdate"):
        ind_response = indiacases()
        result = f"----------Total Cases in INDIA-----------\nActive cases:-{ind_response[0]}\nConfirmed cases:-{ind_response[1]}\nDeaths cases:-{ind_response[2]}\nRecovered cases:-{ind_response[3]}\n\nLast Updated:-{ind_response[4]} "
        bot.send_message(message.chat.id, result)
    elif(message.text == "/help"):
        result = "Plese Make sure to Read above Commands."
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(
            message.chat.id, "No Data Found! Please check above commands.")


# print("Running")



@app.route('/')
def index():
    return '.'


bot.polling()

if __name__ == '__main__':
    app.run(threaded=True)
