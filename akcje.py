from bs4 import BeautifulSoup
import requests

my_url = 'https://www.gpw.pl/archiwum-notowan?fetch=0&type=10&instrument=KGHM&date=&show_x=Pokaż+wyniki'
get_html = requests.get(my_url)
html_text = get_html.text

soup = BeautifulSoup(html_text, "html.parser")
options = soup.find("select", {"id": "selectInstrument"}).findAll("option")

with open("stock_names.csv", 'w') as csv:
    for option in options[1:]:
        print(option.string, file=csv)
