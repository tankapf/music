from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Star Müzik tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/MTLXTSDCA4MLHScP7",
                caption=(f"""● **𝖬𝖾𝗋𝗁𝖺𝖻𝖺** {message.from_user.mention} \n\n● **𝖡𝖾𝗇** {bot} !\n\n● **𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝖽𝖾 müzik 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝖾𝗇 𝖡𝗈𝗍𝗎𝗆 . . !** \n\n● **𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲𝖾𝗌 𝖸𝗈𝗇𝖾𝗍𝗂𝗆 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂𝗉 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇 . . !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 Məni Qrupa Əlavə Et 🎉", url=f"https://t.me/StarMuzikBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💡 Əmirlər" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿 Vendetta 🐊", url="https://t.me/VendettaChatAz"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡ Kanal", url="https://t.me/cguesmasterresmi"
                    )
                ]
                
           ]
        ),
    )



@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>💡 Bütün Əmirlər : \n\n» /vbul => video yüklə . \n» /bul => mahnı yüklə . \n» /oynat => mahnı adı . \n» /durdur => mahnını diyandır  . \n» /devam => mahnıya dəvam et . \n» /atla =>  növbəti mahnı & Videoya keç . \n» /son => Mahnı & Videonu Diyandır . \n» /katil => assistant qrupa çağır . \n» /reload => admin siyahısı yeniləndi . \n\n» /auth => Userin Yetkisi Olmadığı Halda Əmirləri İşləməyə İcazə Verər  .  \n\n» /unauth =>  Userin Yetkisi Olmadığı Halda Əmirləri İşlədməsinə icazə verməni alar. </b>""",
    reply_markup=InlineKeyboardButton(
             [
                 [
                     InlineKeyboardButton(
                         "🇦🇿 Assistant", url="https://t.me/GroupMusicAzAssistant"
                     ),
                     InlineKeyboardButton(
                         "🧑🏻‍💻 Qurucu & Sahib", url="https://t.me/vusaliw"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbstart")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""● **Salam** {query.from_user.mention} \n\n● **Mən** {bot} !\n\n● **Group Az Music 🇦🇿 səsli söhbətdə mahnı dinləməyinizə kömək olan botam . . !** \n\n● **Ban Yetkisiz Səs Yetkisi Verib /reload edib /play yazın assistant özü qrupa daxil olacaq  . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 Məni Qrupa Əlavə Et 🎉", url=f"https://t.me/StarMuzikBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💡 Əmirlər" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "⚡ Kanal", url=f"https://t.me/cguesmasterresmi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑🏻‍💻 Qurucu & Sahib", url="https://t.me/vusaliw"
                    )
                ]
                
           ]
        ),
    )
