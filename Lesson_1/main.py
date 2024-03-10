import asyncio
import config
from aiogram import Bot, Dispatcher
import logging
from Lesson_1.handler import career_choice, common


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.token)

    dp = Dispatcher()

    dp.include_router(career_choice.router)
    dp.include_router(common.router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

