from pyrogram import Client
from bot.config import configs

confi = configs()

app = Client( 
    "jadoo",
    api_id = confi.api_id, 
    api_hash = confi.api_hash, 
    bot_token = confi.bot_token, 
    plugins = dict(root='bot/modules/')
)