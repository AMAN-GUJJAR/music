
import logging
from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only

logging.basicConfig(level=logging.INFO)


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo("https://te.legra.ph/file/9ee01453fc404013fabf1.jpg")
    await message.reply_text(
        f"""<b>β¨ **ππ΄π»π²πΎπΌπ΄ {message.from_user.first_name}** \n
β‘ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) π°π»π»πΎπ ππΎπ ππΎ πΏπ»π°π πΌπππΈπ² πΎπ½ πΆππΎππΏπ ππ·ππΎππΆπ· ππ·π΄ π½π΄π ππ΄π»π΄πΆππ°πΌ'π ππΎπΈπ²π΄ π²π·π°ππ !**

π±οΈ **π΅πΎπ πΈπ½π΅πΎππΌπ°ππΈπΎπ½ π°π±πΎππ π°π»π» π΅π΄π°ππππ΄ πΎπ΅ ππ·πΈπ π±πΎπ, πΉπππ πππΏπ΄ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "π·πΎπ ππΎ πππ΄ πΌπ΄", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "π²πΎπΌπΌπ°π½π³π", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                         "π²ππ΄π°ππ΄π", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "πππΏπΏπΎππ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "π²π·π°π½π½π΄π»", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "π°π»π΄ππ° ππΎπ±πΎπ", url="https://t.me/ALEXA_MANAGER_ROBOT"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""β‘ **bot is running**\n<b>π±οΈ **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΆππΎππΏ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "π²π·π°π½π½π΄π»", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>ππ» **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands !**

β‘ __Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="π·πΎπ ππΎ πππ΄ πΌπ΄", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>π‘ Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°ππΈπ² π²πΌπ³", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "π°π³ππ°π½π²π΄π³ π²πΌπ³", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π°π³πΌπΈπ½ π²πΌπ³", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "πππ³πΎ π²πΌπ³", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "πΎππ½π΄π π²πΌπ³", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π΅ππ½ π²πΌπ³", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "π `PONG!!`\n"
        f"β‘οΈ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "π bot status:\n"
        f"β’ **uptime:** `{uptime}`\n"
        f"β’ **start time:** `{START_TIME_ISO}`"
    )
