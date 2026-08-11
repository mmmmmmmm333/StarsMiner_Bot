import json
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from fastapi import FastAPI, Request
from mangum import Mangum

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN) if TOKEN else None
dp = Dispatcher()

app = FastAPI()


@dp.message()
async def cmd_start(message: types.Message):
  if message.text and message.text.startswith("/start"):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="🎮 O'yinni ochish",
            web_app=types.WebAppInfo(url="https://starsminer.netlify.app/"),
        )
    ]])
    await message.answer(
        "Salom! Stars Miner o'yiniga xush kelibsiz. O'ynash uchun pastdagi"
        " tugmani bosing:",
        reply_markup=keyboard,
    )


# Barcha so'rovlarni qabul qilish uchun yo'lni "/" qildik
@app.post("/")
@app.post("/.netlify/functions/bot")
async def webhook(request: Request):
  if not bot:
    return {"error": "Token topilmadi"}
  try:
    body = await request.body()
    json_data = json.loads(body.decode("utf-8"))
    update = types.Update(**json_data)
    await dp.feed_update(bot, update)
  except Exception as e:
    print(f"Xatolik: {e}")
  return {"ok": True}


handler = Mangum(app)
