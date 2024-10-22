from translate import Translator
from bs4 import BeautifulSoup
from loguru import logger
import aiohttp
import asyncio

import settings_bot



class EncarScraper:
    def __init__(self, car_id : str):
        self.car_id = car_id
        self.headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                        # остальные заголовки
                    }
        self.params = {
                        'pageid': 'dc_carsearch',
                        'listAdvType': 'pic',
                        'carid': self.car_id,
                        'view_type': 'hs_ad',
                        'wtClick_korList': '015',
                        'advClickPosition': 'kor_pic_p1_g2',
                    }
        
        self.proxies = settings_bot.PROXY
        # 'http://VFpTSF:T05pdE@172.245.188.178:8000'

        self.cookies = {
                'RecentViewTruck': '',
                '_gcl_au': '1.1.1864935778.1729007162',
                'PCID': '17290071617297112088414',
                'OAX': 'rPW8smcOjj0AAoUK',
                'afUserId': '364333e8-8ee5-4002-ae80-ec5c2364214b-p',
                'AF_SYNC': '1729007166692',
                '_fbp': 'fb.1.1729007171234.970068484754082446',
                'WMONID': 'QLBWfOtgrdJ',
                '_fwb': '2271Sq2ofgPEfE9joOefTga.1729007379890',
                '_ga': 'GA1.2.1422705952.1729007396',
                '_gid': 'GA1.2.1492275783.1729007396',
                'RECENT_CAR_CARID_38238908_0': '38238908%253A%25EA%25B8%25B0%25EC%2595%2584%2B%25EC%258F%2598%25EB%25A0%258C%25ED%2586%25A0%2B4%25EC%2584%25B8%25EB%258C%2580%2B%25EB%2594%2594%25EC%25A0%25A4%2B2.2%2B4WD%25241',
                'RECENT_CAR_CARID_37130504_0': '37130504%253A%25ED%2598%2584%25EB%258C%2580%2B%25EB%258D%2594%2B%25EB%2589%25B4%2B%25EC%2595%2584%25EB%25B0%2598%25EB%2596%25BC%2BAD%2B1.6%25241',
                'RECENT_CAR_CARID_38065868_1': '38065868%253A%25EA%25B8%25B0%25EC%2595%2584%2B%25EB%258B%2588%25EB%25A1%259C%2BEV%2B%25EB%2585%25B8%25EB%25B8%2594%25EB%25A0%2588%25EC%258A%25A4%25241',
                'RECENT_CAR_CARID_37666815_1': '37666815%253AKG%25EB%25AA%25A8%25EB%25B9%258C%25EB%25A6%25AC%25ED%258B%25B0%2528%25EC%258C%258D%25EC%259A%25A9%2529%2B%25EB%25A0%2589%25EC%258A%25A4%25ED%2584%25B4%2B%25EC%258A%25A4%25ED%258F%25AC%25EC%25B8%25A0%2B%25EB%2594%2594%25EC%25A0%25A4%2B2.2%2B4WD%25241',
                'RECENT_CAR_CARID_38074330_0': '38074330%253A%25ED%2598%2584%25EB%258C%2580%2B%25EB%258D%2594%2B%25EB%2589%25B4%2B%25EA%25B7%25B8%25EB%259E%259C%25EC%25A0%2580%2BIG%2B2.5%25241',
                'RECENT_CAR_CARID_38046588_0': '38046588%253ABMW%2B5%25EC%258B%259C%25EB%25A6%25AC%25EC%25A6%2588%2B%2528G30%2529%2B530i%2B%25EB%259F%25AD%25EC%2585%2594%25EB%25A6%25AC%25241',
                'RecentViewAllCar': '38079265%2C38157264%2C37522731%2C38074330%2C38340550%2C37402505',
                'RecentViewCar': '38079265%2C38157264%2C37522731%2C38074330%2C38340550%2C37402505',
                'cto_bundle': '03exdF9lWFg5ZVhQZVVZeDRhbDNYdFpsNkhQT3AyZkRnYzFic2oyVDBsSXVWZVJwZnhDT0RNcFpSNnkwMHVUN01FQXlISzR1N21FQUVnajFaYVMlMkJobGJUeUNYVVMyZFd0ZWNTdWJRN01ZQlFNQUEydFlwaFBZVmNTY29KRlZibTVOY1dzNG5YRHFQeGpFa21rdUJVWkNQRFgyZyUzRCUzRA',
                'RECENT_CAR_CARID_37402505_0': '37402505%253A%25EC%259E%25AC%25EA%25B7%259C%25EC%2596%25B4%2BNew%2BXF%2B2.2D%2B%25ED%2594%2584%25EB%25A6%25AC%25EB%25AF%25B8%25EC%2597%2584%25241',
                'RECENT_CAR_CARID_38079265_1': '38079265%253A%25ED%2598%2584%25EB%258C%2580%2B%25EA%25B7%25B8%25EB%259E%259C%25EB%2593%259C%2B%25EC%258A%25A4%25ED%2583%2580%25EB%25A0%2589%25EC%258A%25A4%2B12%25EC%259D%25B8%25EC%258A%25B9%2B%25EC%2599%259C%25EA%25B1%25B4%25241',
                'RECENT_CAR_CARID_38157260_0': '38157260%253A%25EC%2589%2590%25EB%25B3%25B4%25EB%25A0%2588%2528GM%25EB%258C%2580%25EC%259A%25B0%2529%2B%25EC%259E%2584%25ED%258C%2594%25EB%259D%25BC%2B2.5%2BLTZ%25241',
                'RECENT_CAR_CARID_38157264_0': '38157264%253A%25EC%25A0%259C%25EB%2584%25A4%25EC%258B%259C%25EC%258A%25A4%2BG80%2B3.8%2BGDI%2BAWD%25241',
                '_encar_hostname': 'http://www.encar.com',
                '_enlog_lpi': 'a109.aHR0cDovL3d3dy5lbmNhci5jb20vZGMvZGNfY2FyZGV0YWlsdmlldy5kbz9wYWdlaWQ9ZGNfY2Fyc2VhcmNoJmxpc3RBZHZUeXBlPXBpYyZjYXJpZD0zNzc4ODk4MSZ2aWV3X3R5cGU9aHNfYWQmd3RDbGlja19rb3JMaXN0PTAxNSZhZHZDbGlja1Bvc2l0aW9uPWtvcl9waWNfcDFfZzI%3D.8d9',
                'RECENT_CAR_CARID_37788981_0': '37788981%253A%25ED%2598%2584%25EB%258C%2580%2B%25EC%2595%2584%25EB%25B0%2598%25EB%2596%25BC%2B%2528CN7%2529%2B1.6%25241',
                'wcs_bt': '4b4e532670e38c:1729185551',
                '_ga_WY0RWR65ED': 'GS1.2.1729185527.11.1.1729185554.0.0.0',
                'JSESSIONID': 'cc1mYjyJ9O9Sec1qP16ssmW5stWlPxK0XgStjgascC4XA423v869lEfPZPKBst1O.mono-was2-prod_servlet_encarWeb6',
                }
        
        self.data = []

    async def to_be_translated(self, results, lang):
        if lang is None:
            return results
        if isinstance(results, str):
            return await asyncio.to_thread(Translator(to_lang=lang, from_lang="ko").translate, results)
        if isinstance(results, list):
            return await asyncio.gather(*[asyncio.to_thread(Translator(to_lang=lang, from_lang="ko").translate, res) for res in results])

    async def get_data(self, html):
            soup = BeautifulSoup(html, 'html.parser')
            
            data = [
                {'model_name': ('en', 'WT.z_model_name')},
                {'model_trim': ('en', 'WT.z_model_trim')},
                {'fuel': ('ru', 'whatfuel')},
                {'miles': (None, 'WT.mileage')},
                {'year': (None, 'WT.z_year')},
                {'mont': (None, 'WT.z_month')}
            ]

            meta_contents = {lang_meta[1]: soup.find('meta', attrs={'name': lang_meta[1]}).get('content')
                            for lang_meta in (list(model.values())[0] for model in data)}

            engine_displacement = soup.find('span', class_='blind', string='배기량:').find_next_sibling(string=True).strip().replace('cc', '')
            img_src = soup.find('div', class_='gallery_photo').find('img')['src']
            price_str = int(soup.find('meta', attrs={'name': 'WT.z_price'}).get('content'))


            tasks = [self.to_be_translated(meta_contents[lang_meta[1]], lang_meta[0]) for model in data for lang_meta in [list(model.values())[0]]]
            translated_results = await asyncio.gather(*tasks)

            car_data = {list(model.keys())[0]: result for model, result in zip(data, translated_results)}
            car_data['engine_displacement'] = engine_displacement
            car_data['link'] = img_src
            car_data['price'] = price_str

            # json_output = json.dumps({'car': car_data}, ensure_ascii=False)
            # logger.success(f'Вернули {car_data}')
            return car_data


    async def main(self):
        try:
            async with aiohttp.ClientSession() as session:
                # async with session.get('http://www.encar.com/',
                #                         proxy=self.proxies,
                #                         cookies=self.cookies,
                #                         # params=self.params,
                #                         headers=self.headers) as respo:
                #     logger.info(respo.status)
                #     hlm = await respo.text()

                #     with open(f'response_testo', 'a', encoding='utf-8') as f:
                #         f.write(f'Status: {respo.status}\n')
                #         f.write(f'HTML:\n{hlm}\n\n')

                async with session.get('http://www.encar.com/dc/dc_cardetailview.do',
                                        proxy=self.proxies,
                                        cookies=self.cookies,
                                        params=self.params,
                                        headers=self.headers) as response:
                    
                    logger.info(response.status)

                    
                    html = await response.text()
                    
                    # with open(f'response_{self.car_id}', 'a', encoding='utf-8') as f:
                    #     f.write(f'Status: {response.status}\n')
                    #     f.write(f'HTML:\n{html}\n\n')

                    return await self.get_data(html)
        except Exception as ex:
            logger.error(f'EnCar Scraper = {ex}')
            return { 'en_car' : None }
                
