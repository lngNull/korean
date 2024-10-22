import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright
from loguru import logger

from page_actions import PageActions

class BrowserAutomation:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self.page_actions = None


    async def _create_object(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.firefox.launch(
            headless=False,
            proxy={
            "server": "http://172.245.188.178:8000",
            "username": "VFpTSF",
            "password": "T05pdE"
                }
        )
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()
        self.page_actions = PageActions(self.page)


    async def _close(self):
        await self.context.close()
        await self.browser.close()
        await self.playwright.stop()


    async def _run(self):
        await self._create_object()
        await self.page_actions._startd_and_hold()


    async def parsing_website(self):
        try:
            await self.page_actions._opening_website()
            cookies = await self.context.cookies()
            Path("cookies.json").write_text(json.dumps(cookies))
            await self._close()
        except Exception as ex:
            await self._close()
            logger.error(f'Ошибка в {ex}')
            return '[WARNING] ПРОИЗОШЛА НЕПРЕДВИДЕННАЯ ОШИБКА. ПОПРОСИТЕ АДМИНИСТРАТОРА О ПЕРЕЗАГРУЗКЕ БОТА'


    async def menu(self):
        await self._run()
        await self.parsing_website()
        await self._close()

aui = BrowserAutomation()
asyncio.run(aui.menu())