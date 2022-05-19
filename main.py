# Libraries
import configparser, json, time, re
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
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

ADMIN = [1881915129] # You can add multiple ids: Example [1881915129, 1881915129, 1881915129]
ALIAS = config['Variables']['ALIAS']
CMDB = config['Variables']['CMDB']

lang = json.load(open(f"lang/" + config['Language']['LANGUAGE'] + ".json", encoding = 'utf-8'))

# EDIT THE CONFIG.INI
#######################################################################################

# Users

def database():
    async def func(_, client, msg):
        try:
            open(f"User/{msg.from_user.id}")
            j = json.load(open(f"User/{msg.from_user.id}"))
            if not j['username'] == f"{msg.from_user.username}":
                j['username'] = f"{msg.from_user.username}"
                j = str(j).replace('{', '{\n    ')
                j = str(j).replace(',', ',\n   ')
                j = str(j).replace("'", '"')
                j = str(j).replace('}', '\n}')
                open(f"User/{msg.from_user.id}", "w").write(j)
        except FileNotFoundError:
            open(f"User/{msg.from_user.id}", "w").write('{\n    ' +
        f'"username": "{msg.from_user.username}",\n    "id": {msg.from_user.id},\n    "input": "false"' + '\n}')
        return True
    return filters.create(func)


# Start

@app.on_message(filters.command("start", prefixes=ALIAS) & filters.private & database())
async def start(app, message):

    startb = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=lang["start_chat_button"], callback_data='avc')]
    ])

    await app.send_message(message.chat.id, text=lang[f"start"], reply_markup=startb, disable_web_page_preview=True)

# Start Chat

homekey = InlineKeyboardMarkup([
    [InlineKeyboardButton(text='🏡 Home', callback_data='home')]
])

@app.on_message(filters.private & ~filters.user("self") & ~filters.command(CMDB), group=-30)
async def chat(app, message):

    avckey = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=lang['end_chat_button'], callback_data='avcend')]
    ])

    j = json.load(open(f"User/{message.from_user.id}"))

    if j['input'] == "avc":
        nome = message.from_user.first_name
        userid = message.from_user.id
        chatid = message.chat.id
        if message.from_user.id not in ADMIN:
            for i in ADMIN:
                if message.text:
                    await app.send_message(
                        i, f"{userid}\n\n<a href='tg://user?id={userid}'>{nome}</a> ➣ {message.text}")
                else:
                    await app.forward_messages(chat_id=i, from_chat_id=message.chat.id, message_ids=message.id)
                    await app.send_message(
                        chat_id=i,
                        text=f"{userid}\n\n🗄 <a href='tg://user?id={userid}'>{nome}</a> " + lang["photo_reply_message"])
            messageSent = await message.reply_text(lang['message_send_message'])
            time.sleep(2)
            await messageSent.delete()

# Admin Settings

    nome = message.from_user.first_name
    userid = message.from_user.id
    chatid = message.chat.id

    if message.from_user.id in ADMIN:
        try:
            # these variables are used to define a user with active forwarding privacy
            rmsg = message.reply_to_message.text                     
            idsender = re.split("\s", rmsg)[0]
            mention_idsender = (await app.get_users(idsender)).mention
            for i in ADMIN:
                if message.reply_to_message:
                    if message.text:
                        try:
                            r = message.reply_to_message.entities[0].user
                            await app.send_message(
                                chat_id=i, text=f"💬👮‍♀️ {message.from_user.mention}" + lang["he_answered"] + f" {r.mention} » {message.text}")
                        except Exception:
                            await app.send_message(
                                chat_id=i, text=f"💬👮‍♀️ {message.from_user.first_name}" + lang["he_answered"] + f" {mention_idsender} » {message.text}")
                    else:
                        r = message.reply_to_message.entities[0].user
                        await app.forward_messages(
                            chat_id=r.id, from_chat_id=chatid, message_ids=message.message_id, as_copy=True)
            if message.text:
                await app.send_message(
                    chat_id=idsender, text=lang[f"operator_message_prefix"] + f" {message.text}", reply_markup=avckey)
        except AttributeError:
            await app.send_message(chatid, lang["error_message_reply"])

@app.on_callback_query()
async def query(client, query):

#   Home

    if query.data == "home":

        homekey = InlineKeyboardMarkup([
            [InlineKeyboardButton(text=lang["start_chat_button"], callback_data='avc')]
        ])

        await query.edit_message_text(lang[f"start"], reply_markup=homekey, disable_web_page_preview=True)


#   Avc

    if query.data == "avc":

        if query.from_user.id in ADMIN:
            await query.answer(lang["answer_admin"], show_alert=True)
        else:    
            avckey = InlineKeyboardMarkup([
                [InlineKeyboardButton(text=lang["end_chat_button"], callback_data='avcend')]
            ])

            j = json.load(open(f"User/{query.from_user.id}"))
            j['input'] = f"avc"
            j = str(j).replace('{', '{\n    ')
            j = str(j).replace(',', ',\n   ')
            j = str(j).replace("'", '"')
            j = str(j).replace('}', '\n}')
            open(f"User/{query.from_user.id}", "w").write(j)

            await query.edit_message_text(lang["start_chat_message"], reply_markup=avckey, disable_web_page_preview=True)


#   AvcEnd

    if query.data == "avcend":

        if query.from_user.id in ADMIN:
            await query.answer(lang["answer_admin"], show_alert=True)
        else:
            avcendkey = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='🏡 Home', callback_data='home')]
            ])

            j = json.load(open(f"User/{query.from_user.id}"))
            j['input'] = f"false"
            j = str(j).replace('{', '{\n    ')
            j = str(j).replace(',', ',\n   ')
            j = str(j).replace("'", '"')
            j = str(j).replace('}', '\n}')
            open(f"User/{query.from_user.id}", "w").write(j)

            await query.edit_message_text(lang["end_chat_success"], reply_markup=avcendkey, disable_web_page_preview=True)

app.run()
