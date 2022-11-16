from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

import keys
from twilio.rest import Client

url = 'https://coinmarketcap.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

tables = soup.findAll('table')

title = soup.title

client = Client(keys.accountSID, keys.authToken)
TwilioNumber = "+14632416814"
myCell = "+18322483338"

crypto_rows = soup.findAll('tr')

for x in range(1,6):
    td = crypto_rows[x].findAll('td')
    name = td[2].text
    #symbol = td[counter+1].text
    current_price = float(td[3].text.replace(',','').replace('$',''))
    change = float(td[4].text.replace('%',''))
    
    corresponding_price = current_price * change

    print(name)
    print(f"Current Price: ${current_price:,.2f}")
    print(f"Change in price over 24 hours: {change}%")
    print(f"Corresponding Price: ${corresponding_price:,.2f}")
    print()
    input()

    if name == 'Bitcoin1BTC' and current_price < float(40000):
        textmessage = client.messages.create(to=myCell, from_=TwilioNumber, body='Bitcoin is currently below $40,000!')

    if name == 'Ethereum2ETH' and current_price < float(3000):
        textmessage = client.messages.create(to=myCell, from_=TwilioNumber, body='Ethereum is currently below $3,000!')