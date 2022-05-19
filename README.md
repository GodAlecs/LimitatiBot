# 🤖 LimitatiBot [2.0]
LimitatiBot is a simple telegram bot to establish a conversation with a user without having to use private chats.

The bot was created on 02/02/2022, there will be many more updates in the future.

# ✅ Features
- 6 Languages available
- 100% Configurable
- Media support (photo / video / sticker / gif)

# ▶️ Examples
- Language File
```json
{
    "start": "**Limited Bot By @AlexProjects**\n\navailable on [GitHub](https://github.com/xMrPente/LimitatiBot)\n\nTo change the message text, go to the 'lang' folder in our source code",
    "message_send_message": "**✔️ Message Sent**",
    "operator_message_prefix": "**🔧 Operator** ➣",
    "user_prefix": "🆕💬 |",
    "error_message_reply": "⚠️ **Error:** __You have to reply a message__",
    "photo_reply_message": "**Reply this message to reply** 💬",
    "he_answered": "replied to",
    "start_chat_button": "✨ Start Chat",
    "end_chat_button": "❌ End Chat",
    "answer_admin": "👮‍♂️ You are admin, you cannot click this button",
    "end_chat_success": "🆗 Successfully finished",
    "start_chat_message": "🆗 Chat Started!\n\nNow, send me **a message** explaining your problem! One of our **Admin** will answer you as soon as possible"
}
```
- Config File
```txt
[Credentials]
# Enter your credentials
API_ID = 
API_HASH = 
TOKEN = 

[Variables]
ALIAS = /
CMDB = start

[Language]
# Choose a language from
# <-> chinese
# <-> german
# <-> english
# <-> french
# <-> italian
# <-> spanish
# Default is english
LANGUAGE = english
```
#❓ How To Install
- Install the libraries
```python
pip install pyrogram
pip install tgcrypto 
pip install configparser
```

- Once this is done, modify the "config.ini" with your credentials

- Then download the source code and start it with the following command
```python
python3 main.py
```

# 📝 Todo list
- Database Support (MySQL / sqlite3 / json)
- All languages of the world available
- Command /ban
- Command /unban

# ⚠️ Warning
the bot will be updated and improved, only if we notice some interest in it.
we also ask everyone not to sell this code, as it is now public.
If you want to support us, make a donation via PayPal

- https://paypal.me/HyperLegacyBot

# 🆘 Do you need help?
You can find us on telegram, here are some useful links
- https://t.me/GodAlecs
