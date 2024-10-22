from aiogram.filters import StateFilter, state
from aiogram.fsm.context import FSMContext
from aiogram import F, Router, types
from aiogram.utils import markdown
from aiogram import Router
from loguru import logger

import settings_bot

from ..keyboard import main_menu_kb, back_kb
from .FSM import GetLinck

from requests_parse import parse_encar

from pycbrf.toolbox import ExchangeRates


rates = ExchangeRates()

router = Router()


@router.callback_query(StateFilter(None), F.data == 'go_parse')
async def get_linck(callback_query : types.CallbackQuery, state : FSMContext):

    await state.set_state(GetLinck.link)

    await callback_query.message.edit_text(
        f'Для расчета стоимости автомобиля пришлите ссылку с сайта Encar.com', reply_markup=back_kb()
    )

# {'model_name': 'Kia Stonic', 'model_trim': '1.4 Trendy', 'fuel': 'Бензин',
# 'miles': '19541', 'year': '2019', 'mont': '05', 'engine_displacement': '1,368',
# 'link': 'http://ci.encar.com/carpicture/carpicture10/pic3820/38207472_001.jpg?impolicy=heightRate&rh=653&cw=1160&ch=653&cg=Center&wtmk=http://ci.encar.com/wt_mark/w_mark_04.png&t=20240923132032',
# 'price': 9999, 'card_price': 7336085, 'price_no_extra_charge': 7153481, 'price_to_tamojka': 279054, 'tamojka_card': 394054,
# 'tamojka_card_no_extra_charge': 96466}


@router.message(StateFilter(GetLinck.link), parse_encar)
async def get_linck( message : types.Message, state : FSMContext, en_car : parse_encar):
    try:
        

        await message.answer_photo(
            photo=en_car['link'],
            caption= await settings_bot.link_data(en_car),
            reply_markup=main_menu_kb()
    )   
    except Exception as ex:
        logger.error(f'{ex}')
        await message.answer('Произошла непредвиденная ошибка. Попробуйте позже', reply_markup=main_menu_kb())

    await state.clear()
