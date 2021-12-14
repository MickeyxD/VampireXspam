#VampireXspam By @MickeyxD

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from VampireXspam.utils import load_plugins
import logging
from telethon import events
from . import Geo, Geo2, Geo3, Geo4, Geo5, Geo6, Geo7, Geo8, Geo9, Geo10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "VampireXspam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("ᴠᴀᴍᴘɪʀᴇ ʙᴏᴛ sᴘᴀᴍ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴘʟᴏʏᴇᴅ -!")
print("ᴇɴᴊᴏʏ! ᴅᴏ ᴠɪsɪᴛ @TheVampireBotz")

if __name__ == "__main__":
    Geo.run_until_disconnected()
    
if __name__ == "__main__":
    Geo2.run_until_disconnected()

if __name__ == "__main__":
    Geo3.run_until_disconnected()
    
if __name__ == "__main__":
    Geo4.run_until_disconnected()

if __name__ == "__main__":
    Geo5.run_until_disconnected()
    
if __name__ == "__main__":
    Geo6.run_until_disconnected()
    
if __name__ == "__main__":
    Geo7.run_until_disconnected()

if __name__ == "__main__":
    Geo8.run_until_disconnected()
    
if __name__ == "__main__":
    Geo9.run_until_disconnected()

if __name__ == "__main__":
    Geo10.run_until_disconnected()    
