# LimitedBot for telegram
# Developed by xMrPente / ipforward / zAlexExploit
# In case of problems contact me on TG -> t.me/AlexProjectsBot

# The sale of the SRC CODE is prohibited

# Libraries
import asyncio
import json
from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(
    'main',
    api_id = 0,  # Insert your telegram API ID before the comma, remember NOT TO PUT the ''
    api_hash = '',  # Insert your HASH API into the ''
    bot_token = ''  # Enter the bot token
)

ALIAS = ['/']  # Command prefixes
ADMINS = [1845164702]  # ID ADMIN
CMDB = ['start']  # Commands not to be seen by admins

# To change the bot language, replace the language name, example from 'english.json' to 'italiano.json'
lingua = json.load(open(f'lang/english.json'))


# The available languages ​​can be found in the 'lang' directory in the bot's source code

# Start

@app.on_message(filters.command('start', prefixes = ALIAS) & filters.private)
async def start(app: Client, message: Message):
    await app.send_message(message.chat.id, lingua['start'])


# Start Chat

@app.on_message(filters.private & filters.user(ADMINS) & ~filters.command(CMDB) & filters.reply)
async def from_admins(app: Client, message: Message):
    await app.copy_message(
        message.reply_to_message.entities[0].user.id,
        message.chat.id,
        message.message_id
    )


@app.on_message(filters.private & filters.user(ADMINS) & ~filters.command(CMDB))
async def from_admins_not_reply(app: Client, message: Message):
    await app.send_message(message.chat.id, lingua['error_message_reply'])


@app.on_message(filters.private & ~filters.me & ~filters.user(ADMINS) & ~filters.command(CMDB))
async def from_users(app: Client, message: Message):
    await message.reply_text(lingua['message_send_message'])
    for admin in ADMINS:
        await asyncio.gather(
            message.copy(admin),
            app.send_message(admin, f'🗄 {message.from_user.mention} {lingua["photo_reply_message"]}'),
            return_exceptions = True
        )
        await asyncio.sleep(0.5)


app.run()
