

from .. import Geo, Geo2, Geo3, Geo4, Geo5 , Geo6, Geo7, Geo8, Geo9, Geo10, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Geo.on(events.NewMessage(pattern=".ping"))
@Geo2.on(events.NewMessage(pattern=".ping"))
@Geo3.on(events.NewMessage(pattern=".ping"))
@Geo4.on(events.NewMessage(pattern=".ping"))
@Geo5.on(events.NewMessage(pattern=".ping"))
@Geo6.on(events.NewMessage(pattern=".ping"))
@Geo7.on(events.NewMessage(pattern=".ping"))
@Geo8.on(events.NewMessage(pattern=".ping"))
@Geo9.on(events.NewMessage(pattern=".ping"))
@Geo10.on(events.NewMessage(pattern=".ping"))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\nϟ ʀɪᴢᴏᴇʟ X sᴘᴀᴍ ϟ︎ `{ms}` ᴍs")                       


# ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀
# ▒█▀▀▄ ▒█░░▒█ ░▒█░░
# ▒█▄▄█ ▒█▄▄▄█ ░▒█░░
