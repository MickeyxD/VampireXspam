import asyncio
from .. import Geo, Geo2, Geo3, Geo4, Geo5, Geo6, Geo7, Geo8, Geo9, Geo10, SUDO_USERS
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
import os
import random
import sys
    
@Geo.on(events.NewMessage(pattern=".leave"))
@Geo2.on(events.NewMessage(pattern=".leave"))
@Geo3.on(events.NewMessage(pattern=".leave"))
@Geo4.on(events.NewMessage(pattern=".leave"))
@Geo5.on(events.NewMessage(pattern=".leave"))
@Geo6.on(events.NewMessage(pattern=".leave"))
@Geo7.on(events.NewMessage(pattern=".leave"))
@Geo8.on(events.NewMessage(pattern=".leave"))
@Geo9.on(events.NewMessage(pattern=".leave"))
@Geo10.on(events.NewMessage(pattern=".leave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SUDO_USERS:
        vampire = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = vampire[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )   
