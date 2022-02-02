# LimitedBot for telegram
# Developed by xMrPente / ipforward / zAlexExploit
# In case of problems contact me on TG -> t.me/AlexProjectsBot

# The sale of the SRC CODE is prohibited

# Libraries
from pyrogram import Client, filters
from pyrogram.types import Message
import json

app = Client(
    "main",
    api_id = 0,  # Insert your telegram API ID before the comma, remember NOT TO PUT the ""
    api_hash = "",  # Insert your HASH API into the ""
    bot_token = ""  # Enter the bot token
)

ALIAS = ["/"]  # Command prefixes
ADMIN = 1845164702  # ID ADMIN
CMDB = ["start"]  # Commands not to be seen by admins

lingua = json.load(
    open(f"lang/english.json")
)  # <- To change the bot language, replace the language name, example from "english.json" to "italiano.json"


# The available languages ​​can be found in the "lang" directory in the bot's source code

# Start

@app.on_message(filters.command("start", prefixes = ALIAS) & filters.private)
async def start(app: Client, message: Message):
    await app.send_message(message.chat.id, lingua["start"])


# Start Chat

@app.on_message(filters.private & ~filters.me & ~filters.command(CMDB), group = -30)
async def chat(app: Client, message: Message):
    chatid = message.chat.id
    if message.from_user.id != ADMIN:
        messageSent = await message.reply_text(lingua['message_send_message'])
        if message.text:
            await app.send_message(
                ADMIN,
                f'{lingua["user_prefix"]} {message.from_user.mention} ➣ {message.text}'
            )
        else:
            await app.forward_messages(
                chat_id = ADMIN, from_chat_id = message.chat.id,
                message_ids = message.message_id
            )
            await app.send_message(
                ADMIN,
                f'🗄 {message.from_user.mention} {lingua["photo_reply_message"]}'
            )

    # Admin Settings

    else:
        if message.reply_to_message:
            if message.text:
                r = message.reply_to_message.entities[0].user
                await app.send_message(
                    r.id,
                    f'{lingua[f"operator_message_prefix"]} {message.text}'
                )
            else:
                r = message.reply_to_message.entities[0].user
                await app.copy_message(
                    r.id,
                    chatid,
                    message.message_id
                )
        else:
            await app.send_message(
                chatid,
                lingua["error_message_reply"]
            )


app.run()
