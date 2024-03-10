from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from Lesson_1.kyeboard.keyboards import kb1, kb2
from Lesson_1.utils.randomfox import fox


router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Приветствую,{name}!', reply_markup=kb1)


@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пакеда,{name}!')

@router.message(Command('info'))
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Это учебный чат-бот,{name}! Он ничего особо не умеет, но уж какой есть :3', reply_markup=kb1)


@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
@router.message(F.text.lower() == 'show foxy')
@router.message(F.text.lower() == 'фыр')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису,{name}!')
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)

@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привяо,{name}!')
    elif 'пока' in msg_user:
        await message.answer(f'Пакеда,{name}!')
    elif 'ты кто' in msg_user:
        await message.answer_dice(dice = "🎲")
    elif 'лиса' in msg_user:
        await message.answer(f'Фыр-фыр-фыр, {name}, =^__^=', reply_markup=kb2)
    else:
        await message.answer(f'А ты как думаешь?')

