from aiogram.utils import markdown
from pycbrf.toolbox import ExchangeRates

#============================================================
# Основные
#============================================================

TG_BOT = '8136160818:AAFLgelGb2X5eh9eiyMOE0ngV2ESiBw2Pw4'


# Правильно: http://ЛОГИН:ПАРОЛЬ@АйПи:ПОРТ
PROXY = 'http://VFpTSF:T05pdE@172.245.188.178:8000'




#============================================================
#Клавиатуры
#============================================================

#Главная Клавиатура

contacts = 'Контакты'
start_calculation = 'Начать расчет'
leave_request = 'Оставить заявку'
social_media = 'Социальные сети'

auto_delivery_text = 'Доставка авто'
auto_delivery_link = 'https://t.me/c/2345465549/7'

pay_auto_text = 'Оплата автомобиля'
pay_auto_link = 'https://t.me/c/2345465549/6'

sey_chat_text = 'Болталка'
sey_chat_text_link = 'https://t.me/c/2345465549/5'

purchase_steps_text = 'Шаги покупки'
purchase_steps_link = 'https://t.me/c/2345465549/2'

#================================================================

#Клавиатура Контактов

first_button_text = 'LiPan Russ'
first_button_link = 'https://t.me/lipan_trade'

second_button_text = 'LiPan Korea'
second_button_link = 'https://t.me/OlegLiMir'


#=================================================================

#Социальные Сети

youtube_link = 'https://www.youtube.com/@LIPANAUTO'
telegram_link = 'https://t.me/lipan_auto'
instagram_link = 'https://instagram.com/lipan_auto'

#=================================================================




# РАСЧЕТ ПО ВВОДИМЫМ ДАННЫМ
async def vrite_data(base):
    rates = ExchangeRates()
    ftamojka_card_no_extra_charge = base['price_to_tamojka']
    tamojka_card_no_extra_charge = f"{ftamojka_card_no_extra_charge:,}".replace(',', '.')

    ftotal_price = base['card_price'] + base['tamojka_card']
    total_price = f"{ftotal_price:,}".replace(',', '.')

    fcustoms_fee = base['customs_fee']
    customs_fee = f"{fcustoms_fee:,}".replace(',', '.')

    return markdown.text(
                f'💰 Предварительная стоимость во Владивостоке: <b>{total_price}₽</b>',
                '',
                'В том числе расходы в <b>РФ:</b>',
                f'▪️Единая таможенная ставка (ЕТС): <b>{tamojka_card_no_extra_charge}₽</b>',
                f'▪️Утилизационный сбор: <b>{customs_fee}₽</b>',
                '',
                '▪️Прохождение лаборатории, получение СБКТС, ЭПТС, вывоз авто с СВХ: <b>38.000₽</b>',
                '▪️ПРР ( погрузочно-разгрузочные работы +стоимость <b>5</b> дней на СВХ) <b>от 35.000₽ до 45.000₽</b>  (зависит от СВХ, на котором размещается авто): <b>46.000₽</b>',
                '▪️Бронирование гостиницы <b>ОТ 4.000р.</b> (зависит от СВХ, на котором размещается авто): <b>4.500₽</b>',
                '▪️Услуги брокера: <b>21.000₽</b>',
                '▪️Перегон авто в ТК: <b>5.500₽</b>',
                '',
                'А также расходы по <b>Южной Корее:</b>',
                '▪️Стояночные (Комиссия площадки):<b>₩ 440 000</b>',
                '▪️Перегон по Корее ( С площадки до нашей стоянки, от нашей стоянки до порта): <b>₩ 300 000 </b>',
                '▪️Фракт: <b>₩ 960 000 </b>',
                '▪️Подготовка экспортных документов: <b>₩150 000</b>',
                '▪️Город доставки: <b>Владивосток</b>',
                '',
                'Расчет составлен с учетом курса валют:',
                f'- USDT к RUB: <b>{rates['USD'].rate} ₽</b>',
                f'- KRW к RUB <b>{rates['KRW'].rate} ₽</b>',  sep='\n'
                )

#==============================================================================


# РАСЧЕТ ПО ССЫЛКЕ


async def link_data(en_car):
    rates = ExchangeRates()

    ftamoojka = en_car['price_to_tamojka']
    tamojka_pri = f"{ftamoojka:,}".replace(',', '.')


    ftotal_price = en_car['tamojka_card'] + en_car['card_price'] 
    total_price = f"{ftotal_price:,}".replace(',', '.')

    fkorean_price = en_car['price']*10000
    korean_price = f"{fkorean_price:,}".replace(',', '.')

    fprice_no_extra_charge = en_car['price_no_extra_charge']
    price_no_extra_charge = f"{fprice_no_extra_charge:,}".replace(',', '.')

    fmiles = int(en_car['miles'])
    miles = f"{fmiles:,}".replace(',', '.')

    return markdown.text(
        f'Модель: <b>{en_car['model_name']} {en_car['model_trim']}</b>',
        '',
        f'▪️Год выпуска: <b>{en_car["year"]}/{en_car["mont"]}</b>',
        f'▪️Пробег: <b>{miles} км</b>',
        f'▪️Топливо: <b>{en_car["fuel"]}</b>',
        f'▪️Объем двигателя: <b>{en_car["engine_displacement"]} cc</b>',
        f'▪️Цена: <b>{korean_price} ₩</b>',
        '',
        f'▪️Стоимость авто в рублях: <b>{price_no_extra_charge} ₽</b>',
        f'▪️Таможенные расходы: <b>{tamojka_pri} ₽</b>',
        '',
        '▪️Стояночные (Комиссия площадки):<b>₩ 440 000</b>',
        '▪️Перегон по Корее ( С площадки до нашей стоянки, от нашей стоянки до порта): <b>₩ 300 000 </b>',
        '▪️Фракт: <b>₩ 960 000 </b>',
        '▪️Подготовка экспортных документов: <b>₩150 000</b>',
        '▪️Город доставки: <b>Владивосток</b>',
        '',
        f'▪️Итоговая стоимость*: <b>{total_price} ₽</b>',
        f'<i><b>*С учетом нашей комиссии</b></i>',
        '',
        f'Курсы расчета стоимости авто:',
        f'- USDT к KRW: <b>1379.15 ₽</b>',
        f'- USDT к RUB: <b>{rates['USD'].rate} ₽</b>',
        f'- KRW к RUB: <b>{rates['KRW'].rate} ₽</b>',
        '',
        '<i>Доставка по России до вашего города рассчитывается отдельно</i>',sep='\n'
        )