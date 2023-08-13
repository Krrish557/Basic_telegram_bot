from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
from bot import app

buttons = [[InlineKeyboardButton(text = "male", callback_data="male")], [InlineKeyboardButton(text= "female", callback_data="female")]]
buttons2 = [[InlineKeyboardButton(text = "Yes", callback_data="yes")], [InlineKeyboardButton(text= "No", callback_data="no")]]

messagelist = []
user = {}

@app.on_message(filters.private & filters.command(["sub", "submit"]))
async def start_command(client, message):
    await client.send_message(
        message.chat.id,
        f"Hello ${message.from_user.username}\nThis is Draw Characters (Non AI).\n\n"
        "This bot collects information about your character, "
        "and then sends the data acquired to the creator of this bot, "
        "who will manually draw the character and send it to you personally.\n\n"
        "Please Note: The drawing will be black and white made by ink."
    )
    await client.send_message(chat_id = 
        message.chat.id, text =
        "What is the gender of the character you want to draw?\n"
        "You can respond with 'male' or 'female'.", reply_markup = InlineKeyboardMarkup(buttons)
    )

@app.on_callback_query()
async def q(c, q):
    data = q.data 

    if data == "male":
        await app.send_message(q.message.chat.id, '''1) What should be the overall physique??  lean, bulky, normal, etc....( you can also refer to someone else's physique)

2) If muscular, how much muscular?? totally ripped and shredded, very less muscular.....(specify, if you want muscles in specific places only)

3) What type of facial structure do you want? Round, rectangle,...etc. (If you can't decide, you can also refer to someone else's face)

4) Describe the beard (if any) and hairstyle (specify if bald).

5) Do you want the character wearing clothes?? If yes, decribe his outfit.  (If he is shirtless or nude....specify about body hairs)

6) Do you want your character, wearing any accesories?? tattoos, chains, pirecings......etc. (anything which is not a part of the outfit, and normal body is counted)

7) What is the most appealing body part to you in a male's body?? ("This Question Is Compulsary To Answer")\n\n Use /Answer [Your answers''')
    elif data == 'female':
        await app.send_message(q.message.chat.id, '''1) What should be the overall physique?? slim, chubby, skinny, muscular...etc. (you can also refer to someone else's physique)

2) Describe the hair length, and hairstyle. Specify colour if you want to. 

3) Describe the lips. (swollen, normal, plump...etc)

4) What should be size of the breasts?? (you can also refer to someone else's breast size)

5) How thick/thin should the ass and thighs be?? (you can also refer to someone else's ass and thighs' thickness)

6) Do you want you character wearing any clothes?? If yes, describe her outfit. (specify if you want no clothes)

7) Do you want your character wearing any accesories?? tattoos, chains, pirecings......etc. (anything which is not a part of the outfit, and normal body is counted)

8) What is the most appealing body part to you in a female's body?? ("This Question Is Compulsary To Answer")\n\n Use /Answer [Your answers]''')

    elif data == "yes":
        await c.send_message(1446438535, f"Submitted by @{user[q.message.chat.id][0]} on {datetime.now()} Submittion:\n\n {messagelist[0]}")
        await user[q.message.chat.id][1].edit('''
Thank you for using this service, I hope you will be satisfied by the outcome.

Please Note : The artist drawing your character is a human with a life of his own to attend, so please do not expect the results to come by very quickly, as the artist will try to put the best efforts, and therefore it might take some time.

Please Note : The artist is a human, who is not a professional artist, and therefore there is room for small mistakes, so please don't expect a 100% smooth result.



                                              
The data has been sent to the artist (@sorrynoideas). They will pm you as soon as the results are completed.

If you have any other query, please, contact : @sorrynoideas .!''')
        user.clear()
        messagelist.clear()
        return
    elif data == 'no':
        await q.reply_text("Please use /Sub command again to restart the forum :)")
        return
        
@app.on_message(filters.private & filters.command(["ans", "answer"]))
async def t(c, m):
    text = m.text.split()
    message = ' '.join(text[1:])
    messagelist.append(message)
    msg = await m.reply_text(text = f"Are you sure you want to send the following message to the Artist?:\n\n{message}", reply_markup = InlineKeyboardMarkup(buttons2))
    user[m.chat.id] = [m.from_user.username, msg]