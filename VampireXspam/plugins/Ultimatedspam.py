import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Geo, Geo2, Geo3, Geo4, Geo5 , Geo6, Geo7, Geo8, Geo9, Geo10, SUDO_USERS


@Geo.on(events.NewMessage(pattern=".uspam"))
@Geo2.on(events.NewMessage(pattern=".uspam"))
@Geo3.on(events.NewMessage(pattern=".uspam"))
@Geo4.on(events.NewMessage(pattern=".uspam"))
@Geo5.on(events.NewMessage(pattern=".uspam"))
@Geo6.on(events.NewMessage(pattern=".uspam"))
@Geo7.on(events.NewMessage(pattern=".uspam"))
@Geo8.on(events.NewMessage(pattern=".uspam"))
@Geo9.on(events.NewMessage(pattern=".uspam"))
@Geo10.on(events.NewMessage(pattern=".uspam"))
async def unlimitedspam(event):
  if event.sender_id in SUDO_USERS:
    try:
      op = event.text[7:]
      x = None
      while x == None:
        await event.client.send_message(event.chat, op)
        await asyncio.sleep(0.3)
    except Exception as e:
      await event.reply("Oops!! Something went wrong, Report In @VampireBotz_support\n\n" + str(e))
