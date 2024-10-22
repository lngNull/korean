from aiogram.filters import StateFilter, state
from aiogram.fsm.context import FSMContext
from aiogram import F, Router, types
from aiogram.utils import markdown
from aiogram import Router

from ..keyboard import contact_user_kb, contacts_kb
from .FSM import FeedbackData

router = Router()


@router.callback_query(StateFilter(None), F.data == 'feedback')
async def start_feedback(callback_query : types.CallbackQuery, state : FSMContext):

    await state.set_state(FeedbackData.model_car)

    await callback_query.message.answer(
        'Укажите марку и модель автомобиля для подбора. Можно указать несколько моделей.'
    )


@router.message(StateFilter(FeedbackData.model_car), F.text)
async def get_modelcar_go_budget(message : types.Message, state : FSMContext):

    await state.update_data(model_car = message.text)

    await state.set_state(FeedbackData.budget)

    await message.answer(
        'Укажите Ваш планируемый бюджет в рублях.'
    )


@router.message(StateFilter(FeedbackData.budget), F.text)
async def get_budget_go_additional_parameters(message : types.Message, state : FSMContext):

    await state.update_data(budget = message.text)
    await state.set_state(FeedbackData.additional_parameters)

    await message.answer(
        'Укажите дополнительные параметры (объем двигателя, привод, год выпуска, цвет).'
    )


@router.message(StateFilter(FeedbackData.additional_parameters), F.text)
async def get_additional_parameters_go_contanct(message : types.Message, state : FSMContext):

    await state.update_data(additional_parameters = message.text)
    await state.set_state(FeedbackData.contact)

    await message.answer(
        'Оставьте телефон для связи', reply_markup= contact_user_kb()
    )

@router.message(StateFilter(FeedbackData.contact), F.text=='Без номера')
async def get_contanct_parameters_go_finelly( message: types.Message, state : FSMContext):
    try:
        await state.update_data(username = message.from_user.username)
        await state.update_data(full_name = message.from_user.full_name)

        data = await state.get_data()

        await state.set_state(FeedbackData.finally_state)
        await state.clear()

        await message.bot.send_message(
            chat_id = '-4566967974',
            text= markdown.text(
                    '<b>===== Есть Клиент! =====</b>',
                    '',
                    f'▪️Имя: <b>{data['full_name']}</b>',
                    f'▪️Ссылка: <b>@{data['username']}</b>',
                    f'▪️Номер: <b>Без Номера</b>',
                    '',
                    f'Марка: <b>{data['model_car']}</b>',
                    f'Допы: <b>{data['additional_parameters']}</b>',
                    f'Прайс: <b>{data['budget']}</b>', sep='\n'
                )
            )
        
        await message.answer(
            markdown.text(
                    'Мы получили вашу заявку!',
                    'Сейчас наши менеджеры обрабатывают ее, но вы можете написать напрямую:',
                    '',
                    'Менеджер LIPAN AUTO RUS:',
                    'Телефон: <code> +7 922 021 6868 </code>',
                    '',
                    'Контакт: Менеджер LIPAN AUTO Korea',
                    'Телефон: <code> +82 10 4336 3344 </code>', sep='\n'
                ),reply_markup=contacts_kb()
        )
    except:
        await message.answer(
            markdown.text(
                    'Попробуйте позже или напишите нашим менеджерам', sep='\n'
                ),reply_markup=contacts_kb())

@router.message(StateFilter(FeedbackData.contact))
async def get_contanct_parameters_go_finelly(message : types.Message, state : FSMContext):
    try:
        await state.update_data(contact = message.contact.phone_number)
        await state.update_data(username = message.from_user.username)
        await state.update_data(full_name = message.from_user.full_name)

        data = await state.get_data()

        await state.set_state(FeedbackData.finally_state)
        await state.clear()

        await message.bot.send_message(
            chat_id = '-4566967974',
            text= markdown.text(
                    '<b>===== Есть Клиент! =====</b>',
                    '',
                    f'▪️Имя: <b>{data['full_name']}</b>',
                    f'▪️Ссылка: <b>@{data['username']}</b>',
                    f'▪️Номер: <b><code>{data['contact']}</code></b>',
                    '',
                    f'Марка: <b>{data['model_car']}</b>',
                    f'Допы: <b>{data['additional_parameters']}</b>',
                    f'Прайс: <b>{data['budget']}</b>', sep='\n'
                )
        )
        await message.answer(
            markdown.text(
                    'Мы получили вашу заявку!',
                    'Сейчас наши менеджеры обрабатывают ее, но вы можете написать напрямую:',
                    '',
                    'Менеджер LIPAN AUTO RUS:',
                    'Телефон: <code> +7 922 021 6868 </code>',
                    '',
                    'Контакт: Менеджер LIPAN AUTO Korea',
                    'Телефон: <code> +82 10 4336 3344 </code>', sep='\n'
                ),reply_markup=contacts_kb()
        )
    except:
        await message.answer(
            markdown.text(
                    'Попробуйте позже или напишите нашим менеджерам', sep='\n'
                ),reply_markup=contacts_kb())

