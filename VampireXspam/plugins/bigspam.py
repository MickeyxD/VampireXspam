async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Geo, Geo2, Geo3, Geo4, Geo5 , Geo6, Geo7, Geo8, Geo9, Geo10, SUDO_USERS


@Geo.on(events.NewMessage(pattern=r"\.bigspam"))
@Geo2.on(events.NewMessage(pattern=r"\.bigspam"))
@Geo3.on(events.NewMessage(pattern=r"\.bigspam"))
@Geo4.on(events.NewMessage(pattern=r"\.bigspam"))
@Geo5.on(events.NewMessage(pattern=r"\.bigspam"))
@Geo6.on(events.NewMessage(pattern=r"\.bigspam"))
@Geo7.on(events.NewMessage(pattern=r"\.bigspam"))
@Geo8.on(events.NewMessage(pattern=r"\.bigspam"))
@Geo9.on(events.NewMessage(pattern=r"\.bigspam"))
@Geo10.on(events.NewMessage(pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        vampire = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(vampire) == 2:
            message = str(vampire[1])
            counter = int(vampire[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
