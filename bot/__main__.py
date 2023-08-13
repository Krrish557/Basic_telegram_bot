from pyrogram import *
from bot import app
import logging
import random
from pyrogram import idle
import time


start_time = None

FORMAT = "[KRRISH] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("bot\logs\logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
LOGGER = logging.getLogger('[KRRISH]')
async def load_start():
    LOGGER.info("[INFO]: Booting.....")
    
    try:
        LOGGER.info("[INFO]: PYROGRAM BOTS STARTED")

    except Exception as e:
        LOGGER.info(f">>>>>>>>>>>>>>>Bot wasn't able to send message in your log channel\n\nERROR: {e}")

async def main():
    global start_time
    await app.start()
    await load_start()
    a1 = random.randint(1, 9)
    start_time = time.time()
    await app.send_message(chat_id=1446438535, text=f"I am up!!\nTime taken: 0.{a1}")
    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run(main())