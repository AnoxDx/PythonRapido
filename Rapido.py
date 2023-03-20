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
        "usage": "TERI <number> <reply>",
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
            reply = random.choice(RAID)
            caption = f"{reply}"
                       await asyncio.sleep(0.3)

@Pyro.cmd(
    pattern="BHK",
    command=("BHK", menu_category),
    info={
        "header": "To stop raid on it.",
        "usage": "BHK <reply>",
    },
)
async def remove_chatbot(event):
        try:
            rremove_ai()


@Pyro.cmd(
    pattern="LOL",
    command=("LOL", menu_category),
    info={
        "header": "To delete raid in this chat.",
        "description": "To stop raid for all enabled users in this chat only..",
        "flags": {"a": "To stop in all chats"},
        "usage": [
            "LOL",
            "LOL",
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
