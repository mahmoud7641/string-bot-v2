from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT,OWNER_ID


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="بدا استخراج الجلسة 🖥️", callback_data="gensession")],
        [
            InlineKeyboardButton(text="الـمـطـور👷", user_id=OWNER_ID),
            InlineKeyboardButton(
                text="سـورس مـحـمـود - Mahmoud", url=SUPPORT_CHAT
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="بايروجورام v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="بايروجورام v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="تليثون", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="حاول مجدداً", callback_data="gensession")]]
)
