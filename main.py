import asyncio

import logging
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

import settings_bot

from tg_bot import start_router, calculation_data_router, calculation_link_router, callback_router

my_bot = Bot(token=settings_bot.TG_BOT, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(bot=my_bot)


dp.include_routers(
    start_router,
    callback_router,
    calculation_data_router,
    calculation_link_router
)


async def main():
    await my_bot.delete_webhook(drop_pending_updates=True)
    # await my_bot.set_my_commands(commands=user_command, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(my_bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())