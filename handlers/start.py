from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME
from config import START_IMG


@Client.on_message(filters.command(["start"]) & ~filters.channel)
async def start(_, message: Message):
    if update.chat.type == "private":
        text="**Hello 👋🏻 {}!**\n\nI **Can Play Music In Voice Chats of Telegram Groups.**I Have A **lot of cool feature that will amaze You!**\n\n**Click /cmdlist For More Help On My Usage ❤**".format(message.from_user.mention)
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Add To Your Group ➕", url="https://t.me/{BOT_USERNAME}?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Group", url="https://t.me/MusicBotSupports"),
            InlineKeyboardButton("Channel 🔊", url="https://t.me/GroupMusicXNews")
            ],[
            InlineKeyboardButton("Commands 🛠", url="https://telegra.ph/Music-Bot-05-07")
            ]]
        )
        await message.reply_text(
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )

@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
          text="**Music Bot Is Online ✅**",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/MusicBotSupports")
              ]]
          )
      )


@Client.on_message(filters.command(["cmdlist", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**Group Music Bot : Help Menu**

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
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/MusicBotSupports")
              ]]
          )
      )
