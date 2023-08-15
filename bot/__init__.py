from pyrogram import Client
from bot.config import configClass

confi = configClass()

app = Client( 
    "jadoo",
    api_id = confi.api, 
    api_hash = confi.hash, 
    bot_token = confi.token, 
    plugins = dict(root='bot/modules/')
)
