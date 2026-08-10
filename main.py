import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from fastapi import FastAPI, Request

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

app = FastAPI()


@dp.message()
async def cmd_start(message: types.Message):
  if message.text == "/start":
    # Bu yerda o'yin havolasini yuborish kodi bo'ladi
    await message.answer(
        "Salom! Stars Miner o'yinini boshlash uchun quyidagini bosing:"
    )


@app.post("/")
async def webhook(request: Request):
  json_data = await request.json()
  update = Update.model_validate(json_data, context={"bot": bot})
  await dp.feed_update(bot, update)
  return {"ok": True}
  
