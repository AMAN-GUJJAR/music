from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, ASSISTANT_NAME
from modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **Welcome user, i'm {query.message.from_user.mention}** \n
⚡ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝙰𝙻𝙻𝙾𝚆 𝚈𝙾𝚄 𝚃𝙾 𝙿𝙻𝙰𝚈 𝙼𝚄𝚂𝙸𝙲 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂 𝚃𝙷𝚁𝙾𝚄𝙶𝙷𝚃 𝚃𝙷𝙴 𝙽𝙴𝚆 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼'𝚂 𝚅𝙾𝙸𝙲𝙴 𝙲𝙷𝙰𝚃𝚂 !**

🖱️ ** 𝙵𝙾𝚁 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙱𝙾𝚄𝚃 𝙰𝙻𝙻 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝙾𝙵 𝚃𝙷𝙴 𝙱𝙾𝚃, 𝙹𝚄𝚂𝚃 𝚃𝚈𝙿𝙴 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                         "𝙲𝚁𝙴𝙰𝚃𝙴𝚁", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                         "𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "𝙰𝙻𝙴𝚇𝙰 𝚁𝙾𝙱𝙾𝚃", url="https://t.me/ALEXA_MANAGER_ROBOT"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝚂𝙸𝙲 𝙲𝙼𝙳", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "𝙰𝙳𝚅𝙰𝙽𝙲𝙴𝙳 𝙲𝙼𝙳", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙰𝙳𝙼𝙸𝙽 𝙲𝙼𝙳", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "𝚂𝚄𝙳𝙾 𝙲𝙼𝙳", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙾𝚆𝙽𝙴𝚁 𝙲𝙼𝙳", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙵𝚄𝙽 𝙲𝙼𝙳", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺 ", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the basic commands</b>

🎧 [ GROUP VC CMD ]

- /play (song name) - play song from youtube
- /ytpplay (song name) - play song directly from youtube 
- /playlist - show the list song in queue
- /song (song name) - download song from youtube
- /search (video name) - search video from youtube detailed
- /video (video name) - download video from youtube detailed
- /lyrics - (song name) lyrics scrapper

🎧 [ CHANNEL VC CMD ]

- /cplay - stream music on channel voice chat
- /cplayer - show the song in streaming
- /cpause - pause the streaming music
- /cresume - resume the streaming was paused
- /cskip - skip streaming to the next song
- /cend - end the streaming music
- /admincache - refresh the admin cache
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/admincache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the admin commands</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the sudo commands</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
/rmd - remove all downloaded files
/clean - Remove all raw files

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the owner commands</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the fun commands</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙻𝙸𝚂𝚃", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 𝙲𝙻𝙾𝚂𝙴", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ end", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⛔ anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛄 group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

💡 **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.

and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.

❔ **usage:**

1️⃣ ban & temporarily ban user from your group:
   » type `/b username/reply to message` ban permanently
   » type `/tb username/reply to message/duration` temporarily ban user
   » type `/ub username/reply to message` to unban user

2️⃣ mute & temporarily mute user in your group:
   » type `/m username/reply to message` mute permanently
   » type `/tm username/reply to message/duration` temporarily mute user
   » type `/um username/reply to message` to unmute user

📝 note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝚂𝙸𝙲 𝙲𝙼𝙳", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "𝙰𝙳𝚅𝙰𝙽𝙲𝙴𝙳 𝙲𝙼𝙳", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙰𝙳𝙼𝙸𝙽 𝙲𝙼𝙳", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "𝚂𝚄𝙳𝙾 𝙲𝙼𝙳", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙾𝚆𝙼𝙴𝚁 𝙲𝙼𝙳", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙵𝚄𝙽 𝙲𝙼𝙳", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝙲𝙺", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
