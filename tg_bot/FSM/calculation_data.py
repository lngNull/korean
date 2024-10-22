from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter, state
from aiogram import F, Router, types
from aiogram.utils import markdown

from loguru import logger

from requests_parse import duble_parse
import settings_bot
from ..keyboard import main_menu_kb, age_kb
from .FSM import GetCarData

from pycbrf.toolbox import ExchangeRates

rates = ExchangeRates()
router = Router()


@router.callback_query(StateFilter(None), F.data == 'independent')
async def get_linck(callback_query : types.CallbackQuery, state : FSMContext):

    await state.set_state(GetCarData.price)

    await callback_query.message.answer_photo(
        photo=types.FSInputFile(
        path = r'.\tg_bot\FSM\image\photo_2024-10-18_08-18-45.jpg'),
        caption='Ниже в сообщении Вам необходимо указать стоимость автомобиля в корейских вонах. Например, Если сумма выглядит как на фото, то указать необходимо <b>35500000</b> ⬇️⬇️⬇️'
    )

@router.message(StateFilter(GetCarData.price), F.text)
async def go_parse(message : types.Message, state : FSMContext):

    await state.update_data(price = message.text)
    await state.set_state(GetCarData.engine_capacity)

    await message.answer(
        f'Укажите объем двигателя в кубических сантиметрах.\n <b>Например: 2000</b>'
    )


@router.message(StateFilter(GetCarData.engine_capacity), F.text)
async def go_parse(message : types.Message, state : FSMContext):

    await state.update_data(engine_capacity = message.text)
    await state.set_state(GetCarData.age)


    await message.answer(
        f'Возраст', reply_markup=age_kb()
    )



@router.callback_query(StateFilter(GetCarData.age), F.data.startswith('age'))
async def get_linck(callback_query : types.CallbackQuery, state : FSMContext):
    try:
        await callback_query.message.answer('Считаем. Пожалуйста, подождите.')
        await state.update_data(age = callback_query.data)
        data = await state.get_data()
        base = await duble_parse(data)


        # ftamojka_card_no_extra_charge = base['price_to_tamojka']
        # tamojka_card_no_extra_charge = f"{ftamojka_card_no_extra_charge:,}".replace(',', '.')

        # ftotal_price = base['card_price'] + base['tamojka_card']
        # total_price = f"{ftotal_price:,}".replace(',', '.')

        # fcustoms_fee = base['customs_fee']
        # customs_fee = f"{fcustoms_fee:,}".replace(',', '.')



        await callback_query.message.answer(
        text = await settings_bot.vrite_data(base),
        reply_markup=main_menu_kb())
    except Exception as ex:
        logger.error(f'{ex}')
        await callback_query.message.answer('Произошла непредвиденная ошибка. Попробуйте позже', reply_markup=main_menu_kb())

    await state.clear()

