# Broadcast
from pyrogram import Client, filters
import json, configparser, asyncio, os

from main import LimitatiBot_app

app = LimitatiBot_app
lang = app.lang
ADMIN = app.ADMIN
prefixes = app.prefixes

@app.on_message(filters.command(["bc", "broadcast"], prefixes=prefixes) & filters.user(ADMIN) & filters.private)
async def broadcast(client, msg):
    args = msg.text.split(' ')
    await msg.delete(revoke=True)
    if msg.reply_to_message:
        await msg.reply_to_message.delete(revoke=True)
        for x in os.listdir('User'):
            try:
                await msg.reply_to_message.copy(int(x))
                await asyncio.sleep(3)
            except:
                pass
        await msg.reply_text("✔️ **Broadcast inviato con successo.**")
    else:
        mess = await msg.reply_text("✖️ **Replica il messaggio da inoltrare**")
        await asyncio.sleep(3)
        await msg.delete(revoke=True)