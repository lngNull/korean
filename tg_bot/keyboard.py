from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types
import settings_bot

def main_menu_kb():
    main_menu_keyboard = InlineKeyboardBuilder()

    main_menu_keyboard.button(text=settings_bot.contacts, callback_data='contact'),
    main_menu_keyboard.button(text=settings_bot.start_calculation, callback_data='new_buisnes'),
    main_menu_keyboard.button(text=settings_bot.leave_request, callback_data='feedback'),

    main_menu_keyboard.button(text=settings_bot.social_media, callback_data='social_media'),
    main_menu_keyboard.button(text=settings_bot.auto_delivery_text, url=settings_bot.auto_delivery_link),

    main_menu_keyboard.button(text=settings_bot.pay_auto_text, url=settings_bot.pay_auto_link),
    main_menu_keyboard.button(text=settings_bot.sey_chat_text, url=settings_bot.sey_chat_text_link),
    
    main_menu_keyboard.button(text=settings_bot.purchase_steps_text, url=settings_bot.purchase_steps_link),

    main_menu_keyboard.adjust(1,1,1,1,1,1)
    return main_menu_keyboard.as_markup()



def contacts_kb():
    contacts_keyboard = InlineKeyboardBuilder()

    contacts_keyboard.button(text=settings_bot.first_button_text, url=settings_bot.first_button_link),
    contacts_keyboard.button(text=settings_bot.second_button_text, url=settings_bot.second_button_link),
    # contacts_keyboard.button(text='YouTube', url='https://www.youtube.com/@LIPANAUTO'),

    contacts_keyboard.button(text='🔙 Вернуться', callback_data='menu')
    contacts_keyboard.adjust(1,1)
    return contacts_keyboard.as_markup()



def social_media_kb():
    social_media_keyboard = InlineKeyboardBuilder()

    social_media_keyboard.button(text='YouTube', url=settings_bot.youtube_link)
    social_media_keyboard.button(text='Telegram', url=settings_bot.telegram_link)
    social_media_keyboard.button(text='Instagram', url=settings_bot.instagram_link)
    social_media_keyboard.button(text='🔙 Вернуться', callback_data='menu')

    social_media_keyboard.adjust(1,1,1)
    return social_media_keyboard.as_markup()



def buisnes_kb():
    buisnes_keyboard = InlineKeyboardBuilder()

    buisnes_keyboard.button(text='Я дам ссылку на автомобиль', callback_data='go_parse'),
    buisnes_keyboard.button(text='Я впишу данные', callback_data='independent'),
    buisnes_keyboard.button(text='🔙 Вернуться', callback_data='menu')
    
    buisnes_keyboard.adjust(1,1)
    return buisnes_keyboard.as_markup()



def age_kb():
    age_keyboard = InlineKeyboardBuilder()

    age_keyboard.button(text='До 3-х лет', callback_data='age0'),
    age_keyboard.button(text='От 3-х до 5-ти лет', callback_data='age3'),
    age_keyboard.button(text='От 5-и до 7-ми', callback_data='age5')
    age_keyboard.button(text='Более 7-ми лет', callback_data='age7')
    
    age_keyboard.adjust(1,1)
    return age_keyboard.as_markup()



def back_kb():
    back_keyboard = InlineKeyboardBuilder()

    back_keyboard.button(text='🔙 Вернуться', callback_data='menu')
    return back_keyboard.as_markup()



def contact_user_kb():


    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Отправить номер", request_contact=True),
        types.KeyboardButton(text="Без номера")
    )



    return builder.as_markup(resize_keyboard=True, one_time_keyboard= True)