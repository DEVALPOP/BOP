import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import app
from random import  choice, randint

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(
    command(["المطور احمد","الكاتب"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("HH3C4")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"– – – – – – – – – – – – – – – – – –\n↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘\n↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘\n↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘\n↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘\n– – – – – – – – – – – – – – – – – –",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["المطور اللواء"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("R_0_0_0")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"– – – – – – – – – – – – – – – – – –\n↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘\n↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘\n↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘\n↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘\n– – – – – – – – – – – – – – – – – –",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["مطورين","مطورين السورس","المطورين"])
  
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dcb95c105123fb71169ee.jpg",
        caption=f"""↯︙اهلا بك عزيزي {message.from_user.mention}\n↯︙مطورين سورس ماتركس ميوزك""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ : 𝖣𝖾𝗏 : ›", url=f"https://t.me/HH3C4"), 
                 ],[
                    InlineKeyboardButton(
                        "‹ : 𝖣𝖾𝗏² : ›", url=f"https://t.me/R_0_0_0"),
                ],[
                    InlineKeyboardButton(
                        "‹ : 𝖬𝖺𝖳𝗋𝗂x 𝖳𝖾𝖠𝗆 : ›", url=f"https://t.me/XMATTMX"),
                ],

            ]

        ),

    )

@app.on_message(command(["تخ"]) & filters.group)
async def huhh(client, message):
await message.reply_animation(
animation=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
caption=f"""↯︙قتل ↫ {message.from_user.mention}\nالضحيه دا 😢 ↫ {message.from_id.first_name}\nانا لله وانـا اليـه راجعـون 😢😢""",
)
reply_markup=InlineKeyboardMarkup(
[
[
InlineKeyboardButton("المقتول 🔪", url=f"{message.from_id.first_name}"),
],[
InlineKeyboardButton("‹ : 𝖬𝖺𝖳𝗋𝗂x 𝖳𝖾𝖠𝗆 : ›", url=f"https://t.me/XMATTMX"),
],
]
),
