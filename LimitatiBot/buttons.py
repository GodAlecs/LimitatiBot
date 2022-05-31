# Buttons
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import json, configparser

config = configparser.ConfigParser()
config.read('config.ini')
lang = json.load(open(f"LimitatiBot/lang/" + config['Language']['LANGUAGE'] + ".json", encoding = 'utf-8'))


#   Class of Buttons

class buttons():
    
    #   Start Button
    start_btn = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=lang["start_chat_button"], callback_data='avc')]
    ])

    #   End Chat Button
    avckey = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=lang['end_chat_button'], callback_data='avcend')]
    ])

    #   Home Button
    homekey = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=lang["start_chat_button"], callback_data='avc')]
    ])

    #   Return Home Button
    avcendkey = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='🏡 Home', callback_data='home')]
    ])

