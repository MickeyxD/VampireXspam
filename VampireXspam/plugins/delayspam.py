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



@Geo.on(events.NewMessage(pattern=".delayspam"))
@Geo2.on(events.NewMessage(pattern=".delayspam"))
@Geo3.on(events.NewMessage(pattern=".delayspam"))
@Geo4.on(events.NewMessage(pattern=".delayspam"))
@Geo5.on(events.NewMessage(pattern=".delayspam"))
@Geo6.on(events.NewMessage(pattern=".delayspam"))
@Geo7.on(events.NewMessage(pattern=".delayspam"))
@Geo8.on(events.NewMessage(pattern=".delayspam"))
@Geo9.on(events.NewMessage(pattern=".delayspam"))
@Geo10.on(events.NewMessage(pattern=".delayspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Vampire = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Vampiresexy = Vampire[1:]
        if len(Vampiresexy) == 2:
            message = str(Vampiresexy[1])
            counter = int(Vampiresexy[0])
            sleeptime = float(Vampire[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Vampiresexy[0])
            sleeptime = float(Vampire[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Vampiresexy[0])
            sleeptime = float(Vampire[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
