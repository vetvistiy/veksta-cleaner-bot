import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8064418763:AAFdApyrYjA_bTguEtWz8aZuqqXI5pk00m8"

TARGET_BOT_ID = 7172499939

DELETE_DELAY = 300

YOUR_BOT_USERNAME = "autodeletekonoplyanka_bot"


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: Message):
    text = (
        "🧹 <b>Cleaner Bot</b>\n\n"
        "Автоматически удаляет сообщения выбранного бота "
        "каждые 5 минут.\n\n"
        "Добавь меня в чат и выдай право:\n"
        "• удаление сообщений"
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="➕ Добавить в чат",
                    url=f"https://t.me/{autodeletekonoplyanka_bot}?startgroup=true"
                )
            ]
        ]
    )

    await message.answer(text, reply_markup=kb, parse_mode="HTML")


@dp.message()
async def auto_delete(message: Message):
    if not message.from_user:
        return

    if message.from_user.id == TARGET_BOT_ID:
        await asyncio.sleep(DELETE_DELAY)

        try:
            await message.delete()
            print("Сообщение удалено")
        except Exception as e:
            print(f"Ошибка удаления: {e}")


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
