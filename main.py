# LimitedBot for telegram
# Developed by xMrPente / ipforward / zAlexExploit
# In case of problems contact me on TG -> t.me/AlexProjectsBot

# The sale of the SRC CODE is prohibited

# Libraries
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.session import Session
import json

app = Client(
    "main",
    api_id = , # Insert your telegram API ID before the comma, remember NOT TO PUT the ""
    api_hash = "", # Insert your HASH API into the ""
    bot_token = "" # Enter the bot token
)

ALIAS = ["/"] # Command prefixes
ADMIN = 1845164702 # ID ADMIN
CMDB = ["start"] # Commands not to be seen by admins

lingua = json.load(open(f"lang/english.json")) # <- To change the bot language, replace the language name, example from "english.json" to "italiano.json"
# The available languages ​​can be found in the "lang" directory in the bot's source code

# Start

@app.on_message(filters.command("start", prefixes=ALIAS) & filters.private)
async def start(app, message):
    await app.send_message(message.chat.id, lingua["start"])


# Start Chat

@app.on_message(filters.private & ~filters.user("self") & ~filters.command(CMDB), group=-30)
async def chat(app, message):
    nome = message.from_user.first_name
    userid = message.from_user.id
    chatid = message.chat.id
    if userid != ADMIN:
        messageSent = await app.send_message(
            chatid, lingua['message_send_message'], reply_to_message_id=message.message_id)
        if message.text:
            await app.send_message(
                ADMIN, lingua["user_prefix"] + f" <a href='tg://user?id={userid}'>{nome}</a> ➣ {message.text}")
        else:
            await app.forward_messages(chat_id=ADMIN, from_chat_id=message.chat.id,
                                message_ids=message.message_id)
            await app.send_message(
                chat_id=ADMIN,
                text=f"🗄 <a href='tg://user?id={userid}'>{nome}</a> " + lingua["photo_reply_message"])
    
# Admin Settings

    if userid == ADMIN:
        if message.reply_to_message:
            if message.text:
                r = message.reply_to_message.entities[0].user
                await app.send_message(
                    chat_id=r.id, text=lingua[f"operator_message_prefix"] + f" {message.text}")
            else:
                r = message.reply_to_message.entities[0].user
                await app.forward_messages(
                    chat_id=r.id, from_chat_id=chatid, message_ids=message.message_id, as_copy=True)
        else:
            await app.send_message(
                chat_id=chatid, text=lingua["error_message_reply"])


app.run()