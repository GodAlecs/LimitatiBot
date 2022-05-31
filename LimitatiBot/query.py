# Query
from pyrogram import Client, filters
import json, configparser

from LimitatiBot.buttons import buttons
from LimitatiBot.filters import database
from main import LimitatiBot_app

app = LimitatiBot_app
lang = app.lang
ADMIN = app.ADMIN

@app.on_callback_query()
async def query(client, query):

#   Home

    if query.data == "home":

        await query.edit_message_text(lang[f"start"], reply_markup=buttons.homekey, disable_web_page_preview=True)


#   Avc

    if query.data == "avc":
        j = json.load(open(f"LimitatiBot/User/{query.from_user.id}"))
        if query.from_user.id in ADMIN:
            await query.answer(lang["answer_admin"], show_alert=True)
        else:    
            if j['input'] == "avc":
                await query.answer(lang['chat_alredy_open'], show_alert=True)
            else:
                j['input'] = f"avc"
                j = str(j).replace('{', '{\n    ')
                j = str(j).replace(',', ',\n   ')
                j = str(j).replace("'", '"')
                j = str(j).replace('}', '\n}')
                open(f"LimitatiBot/User/{query.from_user.id}", "w").write(j)

                await query.edit_message_text(lang["start_chat_message"], reply_markup=buttons.avckey, disable_web_page_preview=True)


#   AvcEnd

    if query.data == "avcend":

        if query.from_user.id in ADMIN:
            await query.answer(lang["answer_admin"], show_alert=True)
        else:
            j = json.load(open(f"LimitatiBot/User/{query.from_user.id}"))
            j['input'] = f"false"
            j = str(j).replace('{', '{\n    ')
            j = str(j).replace(',', ',\n   ')
            j = str(j).replace("'", '"')
            j = str(j).replace('}', '\n}')
            open(f"LimitatiBot/User/{query.from_user.id}", "w").write(j)

            await query.edit_message_text(lang["end_chat_success"], reply_markup=buttons.avcendkey, disable_web_page_preview=True)