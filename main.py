import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = "8064418763:AAFdApyrYjA_bTguEtWz8aZuqqXI5pk00m8"

TARGET_BOT = "konoplyankabot"

DELETE_DELAY = 1800

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message()
async def auto_delete(message: Message):
    if not message.from_user:
        return

    username = message.from_user.username

    if username and username.lower() == TARGET_BOT.lower():
        await asyncio.sleep(DELETE_DELAY)

        try:
            await message.delete()
            print(f"Удалено сообщение от @{username}")
        except Exception as e:
            print(f"Ошибка удаления: {e}")


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


if name == "__main__":
    asyncio.run(main())
