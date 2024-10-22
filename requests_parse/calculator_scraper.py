from bs4 import BeautifulSoup
from loguru import logger
import requests

cookies = {
    '__ucgi': 'cda02e2a7145728d15ea17efdfc195a8',
    '_ym_d': '1729047842',
    '_ym_uid': '1729047842453071181',
    'user_city': '%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA',
    'user_fo': '%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9',
    'user_region': '%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA%D0%B0%D1%8F',
    'user_timezone': 'UTC%2B3',
    '_ga': 'GA1.1.203815327.1729047842',
    'region_cached': '%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C',
    'region_city': '%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA',
    'region_code': '4832',
    'region_phone': '300060',
    'PHPSESSID': 'ni4uoc34baacjl05i19t72s0u6',
    'hcru_cur': '1',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    '_ga_TEVN8E3DR0': 'GS1.1.1729200427.4.1.1729200754.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '__ucgi=cda02e2a7145728d15ea17efdfc195a8; _ym_d=1729047842; _ym_uid=1729047842453071181; user_city=%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA; user_fo=%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9; user_region=%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA%D0%B0%D1%8F; user_timezone=UTC%2B3; _ga=GA1.1.203815327.1729047842; region_cached=%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C; region_city=%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA; region_code=4832; region_phone=300060; PHPSESSID=ni4uoc34baacjl05i19t72s0u6; hcru_cur=1; _ym_isad=2; _ym_visorc=b; _ga_TEVN8E3DR0=GS1.1.1729200427.4.1.1729200754.0.0.0',
    'Origin': 'https://www.alta.ru',
    'Referer': 'https://www.alta.ru/auto-vat/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

class CalculatorScraper:
    def __init__(self, car_data):

        self.car_data = car_data
        self.age = self.get_age()
        self.fuel = self.get_fuel()
        self.price = self.car_data['price'] * 10000
        self.engine_displacement = self.get_engine_displacement()
        self.data = {
            'forCountry': '643', 
            'age': self.age,
            'price': self.price,
            'currency': '410',  
            'dtype': self.fuel,
            'obyem': self.engine_displacement,
            'pwr_val': '82',
            'pwr': 'ls',  
            'hybrid1': '1',
            'lico': 'fiz_personal_use',
        }

    def get_age(self):
        year = 2024 - int(self.car_data['year'])

        if year < 3:
            return 'age0'
        elif year < 5:
            return 'age3'
        elif year < 7: 
            return 'age5'
        else:
            return 'age7'

    def get_fuel(self):
        fuel = self.car_data['fuel'].lower()
        if "бен" in fuel:
            return 'ben'
        elif "диз" in fuel:
            return 'dis'
        else:
            return 'electric'

    def get_engine_displacement(self):
        engine_displacement = float(self.car_data['engine_displacement'].replace(",", ""))
        x = int(engine_displacement)
        # logger.error(x)
        return x


    def main(self):
        try:
            response = requests.post('https://www.alta.ru/auto-vat/',
                                    cookies=cookies,
                                    headers=headers,
                                    data=self.data
                                    )
            data = response.text
            soup = BeautifulSoup(data, 'html.parser')

            total_rub = soup.find('tr', class_='bg-yellow black').find_all('td', class_='t-right')[0].get_text(strip=True).replace(' ', '')
            total_rub = int(float(total_rub.replace('руб', '').replace(' ', '').replace(',', '.')))
            # total_usd = soup.find('tr', class_='bg-yellow black').find_all('td', class_='t-right')[1].get_text(strip=True).replace(' ', '')

            self.car_data['price_to_tamojka']= total_rub
            # logger.error(self.data)
            return self.car_data
        except Exception as ex:
            logger.error(f'Calculator Error = {ex}')
            return {'en_care': None}