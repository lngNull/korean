
# from ruCaptcha import solve_captcha
import asyncio
from playwright.async_api import Page
from loguru import logger
from translate import Translator


class PageActions:
    def __init__(self, page: Page):
        self.page = page


    async def _startd_and_hold(self):
            try:
                await self.page.goto('http://www.encar.com/index.do', wait_until='commit')
                logger.info('Закончили')
            except Exception:
                logger.info('Ошиблись')


    async def _opening_website(self) -> None:
        await self.page.goto('http://www.encar.com/dc/dc_cardetailview.do?carid=38046588')
        await self.page.wait_for_load_state('load')
        await asyncio.sleep(30)



    async def buy_product(self):
        self.page.set_default_timeout(3000) 
        while True:
            try:
                exec(input("Код: "))
            except Exception as e:
                print(e)
    