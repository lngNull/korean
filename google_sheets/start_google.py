import gspread
from loguru import logger

class GoogleSheets:

    def __init__(self):
        self.gc = gspread.service_account(filename=r'.\google_sheets\creds.json')
        self.wks = self.gc.open('calculate').sheet1

    async def get_for_korea(self, data):

        if isinstance(data['price'], str):
            data['price'] = int(data['price']) // 10000

        
        self.wks.update(values=[[data['price']]], range_name='I4')
        card_price = self.wks.acell('H14').value
        self.wks.batch_clear(['I4'])

        card_price = int(card_price.replace('₽', '').replace(' ', '').replace('\xa0', ''))
        price_no_extra_charge = card_price - 182604

        data['card_price'] = card_price
        data['price_no_extra_charge'] = price_no_extra_charge

        # logger.success(data)

        return data


    async def get_for_russia(self,data):

        # logger.success(data)

        self.wks.update(values=[[data['price_to_tamojka']]], range_name='H18')
        tamojka_card = self.wks.acell('H29').value
        self.wks.batch_clear(['H18'])

        tamojka_card = int(tamojka_card.replace('₽', '').replace(' ', '').replace('\xa0', ''))
        tamojka_card_no_extra_charge = tamojka_card - 182000

        data['tamojka_card'] = tamojka_card
        data['tamojka_card_no_extra_charge'] = tamojka_card_no_extra_charge

        # logger.success(data)

        return data



