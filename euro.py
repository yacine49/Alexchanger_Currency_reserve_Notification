from bs4 import BeautifulSoup
import os,time,json
import schedule
from fbchat import Client;from fbchat.models import *
import requests as res
from notify_run import Notify

notify = Notify()

def job():
	try:
		link = 'https://alexchanger.com/exchange_BRDZD_to_PSREUR/'
		re = res.get(link)
		page = BeautifulSoup(re.content, 'lxml')
		amount = page.find_all(class_="xchange_data_div")[1]
		# print(amount)
		amount = amount.find(class_="span_get_max").find_all('span')[1].text.replace("max.:","").replace("EUR","")
		amount = float(amount)
		# amount 
		print(amount)
		if amount > 23 :

			notify.send(f'Hurry Up {amount} '  )
		# with open("euro.txt","a") as f :
		#     f.write(f"{amount} \n")
	except:
		pass

schedule.every(5).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
