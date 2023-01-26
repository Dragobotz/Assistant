import requests
from bot import bot
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from info import START_IMG, START_TEXT, START_BUTTON, HELP_TEXT, HELP_BUTTON, SITHIJATD_BUTTONS, LOGO_TEXT, LOGO_BUTTON, HELP_TEXT, HELP_BUTTON, BOTSTATUS_TEXT, BOTSTATUS_BUTTON, QUOTE_TEXT, QUOTE_BUTTON, SONG_TEXT, SONG_BUTTON

@bot.on_callback_query(filters.regex("auto_rep"))
async def autorep(_, CallbackQuery):
    await bot.answer_callback_query(CallbackQuery.id, text="He he, Don't disturb me😁", show_alert=False)

AUTOREP_BUTTON = InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton('🔵Owner🔵' , url='https://t.me/GOD_DRAGOOP'),
                  InlineKeyboardButton('⭕Youtube⭕' , url='https://www.youtube.com/@DragoXServer'),
                ], 
                [
                 InlineKeyboardButton('〣────────────────〢' , callback_data='auto_rep'),
                ],
              ]
)

@bot.on_inline_query()
async def search(_, query):
    answers = []
    if query.query == "SITHIJA_TD":
        answers.append(
            InlineQueryResultArticle(
                title="DragoOp's Assistant",
                thumb_url="https://te.legra.ph/file/7c7492783613dc2bbb4bf.jpg",
                input_message_content=InputTextMessageContent(f"Hello there 👋\n\n🔰Please Use @GOD_DRAGOOP_BOT to contract me🔰\n🍀GOD DRAGOOP is away from Telegram\n\n💥Reason - O/L exam✍\n 📊Status - Offline⛔️"),
                reply_markup=AUTOREP_BUTTON,
                )
            )
        await query.answer(results=answers, cache_time=0)

@bot.on_inline_query()
async def alive(_, query):
    answers = []
    if query.query == "ALIVE":
        answers.append(
            InlineQueryResultPhoto(
          photo_url=START_IMG,
          title='Bot Inline Menu',
          caption=START_TEXT,
          parse_mode='html',
          reply_markup=START_BUTTON)
        )
        await query.answer(results=answers, cache_time=0)

@bot.on_inline_query()
async def Inline_Search(_, query: InlineQuery):
  t = query.query.lower()

  results = []
  offset = int(query.offset or 0)

  if t == '' or t == 'ahh':
    if t == '':
      results.append(InlineQueryResultPhoto(
          photo_url=START_IMG,
          title='DragoOp\'s Assistant Bot',
          caption=START_TEXT,
          parse_mode='html',
          reply_markup=START_BUTTON)
        )
    results.append(InlineQueryResultPhoto(
        photo_url=START_IMG,
        title='Inline Help Menu',
        caption=HELP_TEXT,
        parse_mode='html',
        reply_markup=HELP_BUTTON)
      )
  elif t != '' or t != ' ' or t != 'info' or t[0] != '!':
    results.append(InlineQueryResultPhoto(
        photo_url=START_IMG,
        title='info',
        caption='Hehe',
        reply_markup=SITHIJATD_BUTTONS)
      )
  try:
    await query.answer(results=results, cache_time=5)
  except QueryIdInvalid:
    pass
