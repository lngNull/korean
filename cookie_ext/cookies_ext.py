#Пиздим куки с Драмматургом за 5 сек

import json
from pathlib import Path
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:
    browser = pw.firefox.launch(
        headless=False,
        slow_mo=300,
        proxy={
            "server": "http://172.245.188.178:8000",
            "username": "VFpTSF",
            "password": "T05pdE"
                }
    )

    context = browser.new_context()
    page = context.new_page()

    page.goto('http://www.encar.com/index.do', wait_until='commit')
    page.goto('http://www.encar.com/dc/dc_cardetailview.do?pageid=dc_carsearch&listAdvType=pic&carid=37402505&view_type=hs_ad&wtClick_korList=015&advClickPosition=kor_pic_p1_g3', wait_until='commit')
    time.sleep(10)

    cookies = context.cookies()
    Path("cookies.json").write_text(json.dumps(cookies))
    
    print("Аккаунт сохранен успешно!")
