from bs4 import BeautifulSoup
from datetime import datetime
import requests
import os

with open("stock_wig20_20210319.csv", 'r') as csv:
    for stock_name in csv:
        if os.path.isfile(f"notowania/{stock_name}.csv"):
            print("The stock quotations are already in the directory.")
        else:
            print("The stock quoations have been added:)")
    # stock_name = '01NFI'
    # my_url = f'https://www.gpw.pl/archiwum-notowan?fetch=0&type=10&instrument={stock_name}&date=&show_x=Pokaż+wyniki'
    # get_html = requests.get(my_url)
    # html_text = get_html.text
    #
    # soup = BeautifulSoup(html_text, "html.parser")
    # stock_quotes_list = soup.find("tbody").findAll("tr")
    # with open(f"notowania/{stock_name}.csv", 'w') as stock_quotes_file:
    #     print("date,currency,open,max,min,close,volume", file=stock_quotes_file)
    #     for stock_soup in stock_quotes_list:
    #         stock_quote = stock_soup.findAll('td')
    #         date = datetime.strptime(stock_quote[0].string, "%d-%m-%Y").date()
    #         currency = stock_quote[1].string
    #         open_price = float(stock_quote[2].string.replace(',', '.'))
    #         max_price = float(stock_quote[3].string.replace(',', '.'))
    #         min_price = float(stock_quote[4].string.replace(',', '.'))
    #         close_price = float(stock_quote[5].string.replace(',', '.'))
    #         volume = float(stock_quote[7].string.replace('\xa0', '').replace(',', '.'))
    #         print(date, currency, open_price, max_price, min_price, close_price, volume,
    #               sep=',', file=stock_quotes_file)

