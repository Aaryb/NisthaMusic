import asyncio
import random
from time import time
from datetime import datetime
from Nistha.config import BOT_USERNAME
from Nistha.Modules.helpers.filters import command
from Nistha.Modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


NISTHA_IMG = (
"https://te.legra.ph/file/1b82afbf90d074849136e.jpg",
"https://te.legra.ph/file/0f64be1cf523f76aa0e2e.jpg",
"https://te.legra.ph/file/1bedd3d90170cc6da5282.jpg",
"https://te.legra.ph/file/c18b4ff72e93a1def1eef.jpg",
"https://te.legra.ph/file/43b1aff6ba286cd61b4cc.jpg",
"https://te.legra.ph/file/45f301147ffede1856f0d.jpg",
"https://te.legra.ph/file/40f551a935da47f59ff64.jpg",

)





START_TEXT = """
ʜɪ ɢᴜʏꜱ, ɪ ᴀᴍ ᴠᴇʀʏ ʜɪɢʜʟʏ ᴀ.ɪ ᴀᴅᴠᴀɴᴄᴇᴅ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ʙᴏᴛ.
ɪ' ᴍ ᴠᴇʀʏ ғᴀꜱᴛ ᴀɴᴅ ᴍᴏʀᴇ ᴇꜰꜰɪᴄɪᴇɴᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ᴀᴡᴇꜱᴏᴍᴇ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ !
"""






START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        random.choice(NISTHA_IMG),
        caption=(START_TEXT),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🍂 sᴜᴘᴘᴏʀᴛ", url="https://t.me/TeleBotService"),
            InlineKeyboardButton("🌾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TeleBotsUpdates")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎓 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/Mr_Disaster_Xd"),
        ]
   
     ]
  ),
)
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        random.choice(NISTHA_IMG),
        caption=(START_TEXT),
        reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🍂 sᴜᴘᴘᴏʀᴛ", url="https://t.me/TeleBotxSupport"),
            InlineKeyboardButton("🌾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TeleBotsUpdate")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎓 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/AnonDeveloper"),
        ]
   
     ]
  ),
)



