from pyrogram import client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType

from bot import app

@app.on_message(filters.private & filters.command("start"))
async def start(c, m):
    await m.reply_text("Type /Submit and the form will be created for you to fill.")
@app.on_message(filters.group & filters.command("start"))
async def start(c, m):
    await m.reply_text("This bot is not meant for groups and will not respond to any command, please contact @bot_username in Private and type /submit which will create a form that you can submit")



@app.on_message(filters.command('help'))
async def help(c, m):
    await m.reply_text("Jadoo Bnake dega mujhe help ka message")
