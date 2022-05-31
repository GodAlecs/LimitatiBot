# Chat
from pyrogram import Client, filters
import json, configparser, time, re, asyncio

from LimitatiBot.buttons import buttons
from LimitatiBot.filters import database
from main import LimitatiBot_app

app = LimitatiBot_app
lang = app.lang
CMDB = app.CMDB
ADMIN = app.ADMIN

@app.on_message(filters.private & ~filters.user("self") & ~filters.command(CMDB), group=-30)
async def chat(app, message):

    j = json.load(open(f"LimitatiBot/User/{message.from_user.id}"))

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
            await asyncio.sleep(2)
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
                                chat_id=i, text=f"💬👮‍♀️ {message.from_user.mention} " + lang["he_answered"] + f" {r.mention} » {message.text}")
                        except Exception:
                            await app.send_message(
                                chat_id=i, text=f"💬👮‍♀️ {message.from_user.first_name} " + lang["he_answered"] + f" {mention_idsender} » {message.text}")
                    else:
                        r = message.reply_to_message.entities[0].user
                        await app.forward_messages(
                            chat_id=r.id, from_chat_id=chatid, message_ids=message.message_id, as_copy=True)
            if message.text:
                await app.send_message(
                    chat_id=idsender, text=lang[f"operator_message_prefix"] + f" {message.text}", reply_markup=buttons.avckey)
        except AttributeError:
            return await app.send_message(chatid, lang["error_message_reply"])
        except Exception:
            return await app.send_message(message.chat.id, lang["account_deleted"])
