from pyrogram import idle
from pyrogram import Client as Bot
from Nistha.Modules.cache.clientbot import run
from Nistha.config import API_ID, API_HASH, BOT_TOKEN

    
bot = Bot(
    ":Nistha:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Nistha/Plugins")
)

bot.start()
run()
idle()
