import json
from aiogram.filters import StateFilter, state
from aiogram.filters.command import Command
from aiogram.filters import StateFilter
from aiogram import F, Router, types

from .keyboard import buisnes_kb, main_menu_kb, contacts_kb, social_media_kb

router = Router()


@router.message(StateFilter(None), Command('start'))
async def start(message : types.Message):
    await message.answer_photo(
        photo = types.FSInputFile(path=r'.\tg_bot\FSM\image\photo_2024-10-19_04-21-51.jpg'),
        caption= f'''Привет,  <b>{message.from_user.full_name}</b>! Вас приветствует компания LIPAN AUTO.\n
    Мы более 2 лет помогаем клиентам из России и других стран привозить автомобили из Южной Кореи. Наша цель — сделать процесс покупки машины максимально простым и выгодным для вас.\n
    📦 Мы выполняем всё "под ключ": от подбора автомобиля до доставки и оформления всех необходимых документов.\n
    ⚙️ Почему выбирают нас: — Гарантированная доставка автомобиля по договору; — Прозрачный и честный расчет всех затрат, включая таможенные пошлины и доставку; — Официальная оплата услуг компании из любого региона; — Поддержка на всех этапах сделки — от выбора авто до его получения. \n
    📈 Экономия от рынка РФ может составлять 20-40%, а наша команда позаботится о том, чтобы вы получили лучший автомобиль по доступной цене!\n
    🚀 Нажмите на кнопку, чтобы записаться на бесплатную консультацию. Мы подготовим для вас индивидуальный расчет стоимости авто и ответим на все вопросы.''',
        reply_markup=main_menu_kb()
        )


@router.callback_query(F.data =='contact')
async def contact(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
                '''🇰🇷Автомобили прямо из Южной Кореи \n\n Экспорт Авто \n Весь спектр услуг по покупке авто \n ✅ Гарантированная доставка ✅ Комплексная проверка автомобилей \n ✅ Привлекательные цены ✅ Легальные способы оплаты \n\n Менеджер LIPAN AUTO RUS \n Телефон: <code> +7 922 021 6868 </code> \n\n Контакт: Менеджер LIPAN AUTO Korea \n Телефон: <code> +82 10 4336 3344 </code> ''',
                reply_markup=contacts_kb()
    )


@router.callback_query(StateFilter('*'),F.data == 'menu')
async def menu(callback_query : types.CallbackQuery, state : StateFilter):
    
    await state.clear()
    await callback_query.message.answer(
        f'🇰🇷 Авто напрямую <b>из Южной Кореи ✈️</b> \n ✈️ Экспорт авто <b>в Россию</b> 🇷🇺 \n\n ✅ Надежная доставка | Полная проверка авто ✅  \n ✅ Выгодная цена | Официальная оплата ✅',
        reply_markup=main_menu_kb()
    )


@router.callback_query(F.data == 'new_buisnes')
async def contacts(callback_query : types.CallbackQuery):
    await callback_query.message.answer(
        f'Выберите способ расчета:', reply_markup= buisnes_kb()
    )


@router.callback_query(F.data == 'social_media')
async def menu(callback_query : types.CallbackQuery):

    await callback_query.message.answer(
        f'Будь вкурсе наших новостей!',
        reply_markup=social_media_kb()
        )
    




