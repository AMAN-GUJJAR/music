from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@ALEXAMUSIC_ROBOT"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo("https://te.legra.ph/file/9ee01453fc404013fabf1.jpg")
    await message.reply_text(
        text="**𝙷𝙴𝙻𝙻𝙾 👋🏻 {}!**\n\n𝙸 **𝙲𝙰𝙽 𝙿𝙻𝙰𝚈 𝙼𝚄𝚂𝙸𝙲 𝙸𝙽 𝚅𝙾𝙸𝙲𝙴 𝙲𝙷𝙰𝚃 𝙾𝙵 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙶𝚁𝙾𝚄𝙿𝚂.**𝙸 𝙷𝙰𝚅𝙴 𝙰 **𝙻𝙾𝚃 𝙾𝙵 𝙲𝙾𝙾𝙻 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚃𝙷𝙰𝚃 𝚆𝙸𝙻𝙻 𝙰𝙼𝙰𝚉𝙴 𝚈𝙾𝚄!**\n\n**𝙲𝙻𝙸𝙲𝙺 /cmdlist 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙷𝙴𝙻𝙿 𝙾𝙽 𝙼𝚈 𝚄𝚂𝙰𝙶𝙴 ⚡**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("🖱️ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 🖱️", url="https://t.me/ALEXAMUSIC_ROBOT?startgroup=true")
            ],[
            InlineKeyboardButton("🥳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 🥳", url="https://t.me/DARKAMANSUPPORT"),
            InlineKeyboardButton("♨️ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ♨️", url="https://t.me/DARKAMANCHANNEL")
            ],[
            InlineKeyboardButton("⚡ 𝙰𝙻𝙴𝚇𝙰 𝚁𝙾𝙱𝙾𝚃 ⚡", url="https://t.me/ALEXA_MANAGER_ROBOT")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@ALEXAMUSIC_ROBOT"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**𝙰𝙻𝙴𝚇𝙰 𝙼𝚄𝚂𝙸𝙲 𝙱𝙾𝚃 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴 **",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="⚡𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿⚡", url="https://t.me/DARKAMANSUPPORT")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@ALEXAMUSIC_ROBOT"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**𝙰𝙻𝙴𝚇𝙰 𝙼𝚄𝚂𝙸𝙲: Help Menu**

__× First Add Me To Your Group..
× Promote Me As Admin In Your Group With All Permission..__

**🏷 Common Commands.**

• `/play` - Song Name : __Plays Via Youtube__
• `/dplay` - Song Name : __Play Via Deezer__
• `/splay` - Song Name : __Play Via Jio Saavn__
• `/playlist` - __Show now playing list__
• `/current` - __Show now playing__

• `/song` - Song Name : __Get The Song From YouTube__
• `/vid` - Video Name : __Get The Video From YouTube__
• `/deezer` - song name : __download songs you want quickly via deezer__
• `/saavn` - song name : __download songs you want quickly via saavn__
• `/search` - YouTube Title : __(Get YouTube Search Query)__

**🏷 Group Admin Commands.**

• `/skip` : __Skips Music__
• `/pause` : __Pause Playing Music__
• `/resume` : __Resume Playing Music__
• `/end` : __Stops playing Music__
• `/reload` : __Reloads Admin List__
• `/userbotjoin` : __Assistant Joins The Group__
• `/userbotleave` : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="⚡ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ⚡", url="https://t.me/DARKAMANSUPPORT")
              ]]
          )
      )
