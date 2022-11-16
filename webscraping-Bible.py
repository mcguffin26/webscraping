import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request





random_chapter = random.randint(1,21)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

page_verses = soup.findAll('div',class_='main')

#print(page_verses)

for verse in page_verses:
    verse_list = verse.text.split('.')

#print(verse_list)

myverse = random.choice(verse_list[:len(verse_list)-5])

#print(f"Chapter: {random_chapter} , Verse: {myverse}")

message = "Chapter: " + random_chapter + " Verse: " + myverse

print(message)

import keys
from twilio.rest import Client

client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+14632416814"

myCell = "+18322483338"

#send text message
textmessage = client.messages.create(to=myCell, from_=TwilioNumber, body=message)

print(textmessage.status)
