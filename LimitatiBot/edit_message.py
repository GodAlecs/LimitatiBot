# Edited Message
from pyrogram import Client, filters
import json, configparser

from LimitatiBot.buttons import buttons
from LimitatiBot.filters import database
from main import LimitatiBot_app

app = LimitatiBot_app
lang = app.lang

@app.on_edited_message()
async def edited(app, message):

    await message.reply_text(lang['message_edited'], quote=True, reply_markup=buttons.avckey)
    
