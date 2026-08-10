import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = os.getenv("BOT_TOKEN")
# GitHub havolangiz (username.github.io/StarsMiner_Bot/index.html ko'rinishida bo'ladi)
WEB_APP_URL = "https://mmmmmmmmm333.github.io/StarsMiner_Bot/index.html"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="🚀 O‘yinni boshlash", web_app=types.WebAppInfo(url=WEB_APP_URL))
    
    first_name = message.from_user.first_name or "Do'st"
    
    await message.answer(
        f"🌟 **Salom, {first_name}!**\n\n"
        f"\"Telegram Stars Miner\" botiga xush kelibsiz!\n"
        f"Tanga yig'ing, energiyani to'ldiring va har oylik reytingda qatnashib Telegram Stars yutib oling! 🏆",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
  
