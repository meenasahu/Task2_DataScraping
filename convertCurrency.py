import requests as rq

EUrl = "https://api.coinbase.com/v2/exchange-rates"

EHeaders = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'

}

stockData = [
    {
        'name':'TCS',
        'current_price': 3000,
        'currency': 'INR',
        'Con_price': '?'
    },
    {
        'name':'GOOG',
        'current_price': 166,
        'currency': 'USD',
        'Con_price': '?'
    },
]

EResp = rq.get(url=EUrl, headers=EHeaders).json()
#print('EResp :',EResp)

currencyData = EResp['data']['rates']

#print('currencyData :',currencyData)

def convert_USD(currencyData):
    for stocks in stockData:
        currency = stocks['currency']
        price = stocks['current_price']

        if currency == 'INR':
            con_rate = float(currencyData['INR'])
            stocks['Con_price'] = round(price / con_rate, 2)
        
        elif currency == 'USD':
            inr_rate = float(currencyData['INR'])
            stocks['Con_price'] = round(price * inr_rate,2)

        else: 
            stocks['Con_price'] = 'Rates are not in the list'


convert_USD(currencyData)

for stocks in stockData:
    print(f'name = {stocks['name']},current_price = {stocks['current_price']},currency = {stocks['currency']},Con_price = {stocks['Con_price']}')