from StringGen import Anony
from pyrogram import Client, filters, types 
from requests import get
import json
import asyncio 

# bot helpers 
BOT_MESSAGE = {
    'JOIN_CHANLL':
                u'عذرن عزيزي عليك الاشترك بي قناة البوت اولان لي استخدام البوت 🧩💬.'
                u'\n\n Channl : @{} 💭🔰.'
                u'\n\n  👇 قم بي الاشترك من ثم اضغط علا زر تحقق 🔱🔗 .'
                u'',
    'DONE_JOIN_CHANNL':
                    u'شكرأ لك على الاشتراك في قناة البوت.'
                    u'\n\n الان قم بإرسال ( /start )  لتشغيل البوت ♻️🔱.'
                 u''
}

def CHECK_JOIN_KEYBOARD(Channl: str):
    return types.InlineKeyboardMarkup([
        [
            types.InlineKeyboardButton(text='قناة البوت 〽️💭.', url=f't.me/{Channl}'),
            types.InlineKeyboardButton(text='تحقق ♻️.', callback_data='checkjoin')
        ]
    ])
def REDRESH_LANSHER(text: str):
    return types.InlineKeyboardMarkup([
        [
            types.InlineKeyboardButton(text=text, callback_data='NOT')
        ]
    ])
    
## api chack member join from channls
async def CHECK_USER_JOIN(api_key, channls_join: list, user_id : int):
    c ,r = None ,False
    statues = ['administrator','creator','member','restricted']
    for channl in channls_join:
        url =f"https://api.telegram.org/bot{api_key}/getChatMember?chat_id=@{channl}&user_id={str(user_id)}"
        respons = get(url)
        JSObj = json.loads(respons.text) 
        user_state = JSObj['result']['status']
        if user_state in statues:
            r = True 
        else : 
            r = False
            c = channl
            return r,c
    return r,c

BOT_CHANNL = ['YY5Y8']


@Anony.on_message(filters.regex('^/start$') & filters.private)
async def START_BOT(_, message: types.Message):
    chat_id, message_id, user_id = message.chat.id, message.id, message.from_user.id
    join_, channl = await CHECK_USER_JOIN(API_KEY,BOT_CHANNL, user_id)
    if not join_:
        await Anony.send_message(chat_id=chat_id, text=BOT_MESSAGE['JOIN_CHANLL'].format(channl), reply_markup=CHECK_JOIN_KEYBOARD(channl))
        return 
    await Anony.send_message(chat_id, 'مرحبا بك .')
