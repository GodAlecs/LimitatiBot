# LimitedBot for telegram
# Developed by xMrPente / ipforward / zAlexExploit
# In case of problems contact me on TG -> t.me/AlexProjectsBot

# The sale of the SRC CODE is prohibited

# Libraries
import configparser, json
from pyrogram import (
    Client, 
    filters
)

config = configparser.ConfigParser()
config.read('config.ini')

#######################################################################################
# EDIT THE CONFIG.INI

app = Client(
    "main",
    api_id = config['Credentials']['API_ID'],
    api_hash = config['Credentials']['API_HASH'],
    bot_token = config['Credentials']['TOKEN']
)

ALIAS = config['Variables']['ALIAS']
ADMIN = int(config['Variables']['ADMIN_ID'])
CMDB = config['Variables']['CMDB']

lingua = json.load(open(f"lang/" + config['Language']['LANGUAGE'] + ".json"))

# EDIT THE CONFIG.INI
#######################################################################################

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
