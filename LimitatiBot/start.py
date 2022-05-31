# Start
from pyrogram import Client, filters
import json, configparser

from LimitatiBot.buttons import buttons
from LimitatiBot.filters import database
from main import LimitatiBot_app

app = LimitatiBot_app
lang = app.lang
prefixes = app.ALIAS

@app.on_message(filters.command("start", prefixes=prefixes) & filters.private & database())
async def start(app, message):

    await app.send_message(message.chat.id, text=lang[f"start"], reply_markup=buttons.start_btn, disable_web_page_preview=True)
