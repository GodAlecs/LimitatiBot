# Main
import configparser, json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import (
    Client, 
    filters
)

# Private Class
from LimitatiBot.buttons import buttons
from LimitatiBot.filters import database

# Main Class
class LimitatiBot_app(Client):

    config = configparser.ConfigParser()
    config.read('config.ini')

    app = Client(
        "main",
        api_id = config['Credentials']['API_ID'],
        api_hash = config['Credentials']['API_HASH'],
        bot_token = config['Credentials']['TOKEN'],
        plugins=dict(root=f"LimitatiBot"),
        sleep_threshold=180
    )

    ADMIN = [1881915129] # You can add multiple ids: Example [1881915129, 1881915129, 1881915129]
    ALIAS = config['Variables']['ALIAS']
    CMDB = ["start", "bc", "broadcast", "help"]
    prefixes = config['Variables']['ALIAS']

    lang = json.load(open(f"LimitatiBot/lang/" + config['Language']['LANGUAGE'] + ".json", encoding = 'utf-8'))

    if __name__ == "__main__":
        app.run()