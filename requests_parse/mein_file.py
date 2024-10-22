import re
from aiogram import types
from loguru import logger
from .encar_scraper import EncarScraper
from .calculator_scraper import CalculatorScraper
from .calculator_scraper_dabl import DubbleCalculatorScraper

from google_sheets import GoogleSheets

async def parse_encar(message : types.Message):
    google = GoogleSheets()

    carId = await extract_carid(message.text)

    try:
        google = GoogleSheets()
        encar_data = await EncarScraper(carId).main()
        card_data = await google.get_for_korea(encar_data)
        calculate = CalculatorScraper(card_data).main()
        en_car = await google.get_for_russia(calculate)
        # price_to_tamojka


        
        return {"en_car" : en_car}
    except Exception as ex:
        logger.error(f'Ошибка в {ex}')
        return { 'en_car' : None }

async def duble_parse(data):
    try:
        google = GoogleSheets()
        google_data = await google.get_for_korea(data)
        car_data = DubbleCalculatorScraper(google_data).main()
        return await google.get_for_russia(car_data)
    except Exception as ex:
        logger.error({ex})
        return None




async def extract_carid(url):
    try:
        pattern = r'(\d+)'
        match = re.search(pattern, url)
        
        if match:
            return match.group(1)
        else:
            return None
        
    except Exception as ex:
        logger.error(f'Ошибка в {ex}')
        return { 'en_car' : None }