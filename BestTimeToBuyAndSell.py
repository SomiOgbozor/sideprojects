import bs4
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uReq
my_url = 'https://www.nasdaq.com/symbol/aapl/after-hours'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
price_div = page_soup.find("div", id="qwidget_lastsale")
price = price_div.text
price = price[1:]

# access csv data
import csv
from datetime import datetime
date = datetime.today().strftime('%Y-%m-%d')
row = [date, price]
with open('/Users/somiogbozor/Documents/apple.csv', 'a') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(row)
csvFile.close()

# calculate max profit
running_max_profit = 0;
min_price = 999999;
with open('/Users/somiogbozor/Documents/apple.csv') as csvFile:
	for row in csv.reader(csvFile, delimiter=','):
		temp_price = float(row[1])
		if(temp_price < min_price):
			min_price = temp_price
		if(temp_price - min_price > running_max_profit):
			running_max_profit = temp_price - min_price
csvFile.close()
print(running_max_profit)