import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "26348115"))
API_HASH = getenv("API_HASH", "8da1c482cbcd3b30bd76dbf6e57daa18")
BOT_USERNAME = getenv("http://t.me/HoligrasMuzikBot")
BOT_TOKEN = getenv("6306196396:AAGCpiaWMuQDCONjDvrcFsywEsW3vG6ku48")
UPDATE_CHANNEL = getenv("https://t.me/Holigras")
SUPPORT_GROUP = getenv("https://t.me/Holigras")
OWNER_USERNAME = getenv("Levoz0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5709622852").split()))
aiohttpsession = aiohttp.ClientSession()
