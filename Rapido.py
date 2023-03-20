import asyncio
import random

from PythonRapido import Pyro
)
menu_category = "fun"


RAID = [
"RANDI"
"TERI"
"MAA"
"KI"
"CHUT"
"ME"
"LODA"
"MARUGA"
"MADRCHOD"
"TERI"
"BHEN"
"KI"
"CHUT"
"ME"
"CHAPPL"
"MARUGA"
"BHEN"
"KE"
"BHOSDE"
"RANDI"
"KE"
"PILLE"
"TERI"
"MAA"
"ROYEGI"
"AB"
"TERI"
"MAA"
"NEE"
"FALTU"
"PAIDA"
"KR"
"DIYA"
"TUZE"
"RAND"
"KE"
"CHODE",
]


@Pyro.cmd(
    pattern="TERI",
    command=("TERI", menu_category),
    info={
        "header": "To Send Abuse rapidly with according to number",
        "usage": "{tr}TERI <number> <reply>",
    },
)
async def spam(e):
    lol = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    reply_to = await reply_id(e)
    if await age_verification(e, reply_to):
        return
    type = await useless.importent(e)
    if type:
        return
    await e.get_reply_message()
    if e.reply_to_msg_id:
        addgvar("spamwork", True)
        a = await e.get_reply_message()
        b = await e.client.get_entity(a.sender_id)
        g = b.id
        c = b.first_name
        counter = int(lol[0])
        username = f"[{c}](tg://user?id={g})"
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            reply = random.choice(RAID)
            caption = f"{username} {reply}"
            async with e.client.action(e.chat_id, "typing"):
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)

@Pyro.cmd(
    pattern="BHK",
    command=("BHK", menu_category),
    info={
        "header": "To stop raid on it.",
        "usage": "{tr}BHK <reply>",
    },
)
async def remove_chatbot(event):
    "To stop raid for that user"
    if event.reply_to_msg_id is None:
        return await eor(event, "Reply to a User's message to stop raid on him.")
    reply_msg = await event.get_reply_message()
    user_id = reply_msg.sender_id
    chat_id = event.chat_id
    if ris_added(chat_id, user_id):
        try:
            rremove_ai(chat_id, user_id)
        except Exception as e:
            await eod(event, f"**Error:**\n`{e}`")
        else:
            await eor(event, "Raid has been stopped for the user")
    else:
        await eor(event, "The user is not activated with raid")


@Pyro.cmd(
    pattern="delraid( -a)?",
    command=("delraid", menu_category),
    info={
        "header": "To delete raid in this chat.",
        "description": "To stop raid for all enabled users in this chat only..",
        "flags": {"a": "To stop in all chats"},
        "usage": [
            "{tr}delraid",
            "{tr}delraid -a",
        ],
    },
)
async def delete_chbot(event):
    "To delete ai in this chat."
    input_str = event.pattern_match.group(1)
    if input_str:
        lecho = rget_all_users()
        if len(lecho) == 0:
            return await eod(
                event, "You havent enabled ai atleast for one user in any chat."
            )
        try:
            rremove_all_users()
        except Exception as e:
            await eod(event, f"**Error:**\n`{str(e)}`", 10)
        else:
            await eor(event, "Deleted ai for all enabled users in all chats.")
    else:
        lecho = rget_users(event.chat_id)
        if len(lecho) == 0:
            return await eod(
                event, "You havent enabled raid atleast for one user in this chat."
            )
        try:
            rremove_users(event.chat_id)
        except Exception as e:
            await eod(event, f"**Error:**\n`{e}`", 10)
        else:
            await eor(event, "Deleted Raid for all enabled users in this chat")
