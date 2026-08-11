import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from fastapi import FastAPI, Request

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

app = FastAPI()


@app.get("/api")
async def root():
  return {"status": "Bot and Game are running!"}


@dp.message()
async def cmd_start(message: types.Message):
  if message.text == "/start":
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="🎮 O'yinni ochish",
            web_app=types.WebAppInfo(url="https://stars-miner-bot.vercel.app/"),
        )
    ]])
    await message.answer(
        "Salom! Stars Miner o'yiniga xush kelibsiz. O'ynash uchun pastdagi"
        " tugmani bosing:",
        reply_markup=keyboard,
    )


@app.post("/api/index")
async def webhook(request: Request):
  try:
    json_data = await request.json()
    update = types.Update(**json_data)
    await dp.feed_update(bot, update)
  except Exception as e:
    print(f"Xatolik: {e}")
  return {"ok": True}
  
