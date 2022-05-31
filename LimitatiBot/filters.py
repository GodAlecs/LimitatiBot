# Filter
from pyrogram import filters
import json

#   Database Filter
def database():
    async def func(_, client, msg):
        try:
            open(f"LimitatiBot/User/{msg.from_user.id}")
            j = json.load(open(f"LimitatiBot/User/{msg.from_user.id}"))
            if not j['username'] == f"{msg.from_user.username}":
                j['username'] = f"{msg.from_user.username}"
                j = str(j).replace('{', '{\n    ')
                j = str(j).replace(',', ',\n   ')
                j = str(j).replace("'", '"')
                j = str(j).replace('}', '\n}')
                open(f"LimitatiBot/User/{msg.from_user.id}", "w").write(j)
        except FileNotFoundError:
            open(f"LimitatiBot/User/{msg.from_user.id}", "w").write('{\n    ' +
        f'"username": "{msg.from_user.username}",\n    "id": {msg.from_user.id},\n    "input": "false"' + '\n}')
        return True
    return filters.create(func)