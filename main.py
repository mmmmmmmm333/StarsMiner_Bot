import os
from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI, Request

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

app = FastAPI()


@app.get("/")
async def root():
  return {"status": "Bot is running!"}


@dp.message()
async def cmd_start(message: types.Message):
  if message.text == "/start":
    await message.answer(
        "Salom! Stars Miner o'yinini boshlash uchun quyidagini bosing:"
    )


@app.post("/")
async def webhook(request: Request):
  json_data = await request.json()
  update = types.Update(**json_data)
  await dp.feed_update(bot, update)
  return {"ok": True}
  
