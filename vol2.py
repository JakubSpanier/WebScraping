from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from itertools import chain
import datetime
import time
import csv

start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
end = datetime.datetime.strptime("31-12-2019", "%d-%m-%Y")
interval = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days + 1) if x % 7 not in {2, 3} and x not in {0, 5, 92, 95, 120, 154, 314, 357, 358, 364, 365, 370, 449, 452, 488, 511, 592, 670, 680, 725, 736, 834, 837, 851, 853, 896, 957, 1035, 1089, 1090, 1096, 1097, 1184, 1187, 1216, 1218, 1246, 1322, 1400, 1411, 1453, 1454, 1455, 1460, 1461, 1569, 1572, 1581, 1583, 1631, 1687, 1765, 1775, 1818, 1819, 1820, 1825}]

# for i in range(len(interval)):
#     print(i, interval[i])

join_stock_companies = ["ALIOR", "ASSECOPOL", "BOGDANKA", "CCC", "CDPROJEKT",
                        "CYFRPLSAT", "DINOPL", "ENEA", "ENERGA", "EUROCASH",
                        "JSW", "KERNEL", "KGHM", "LOTOS", "LPP",
                        "MBANK", "ORANGEPL", "PEKAO", "PGE", "PGNIG",
                        "PKNORLEN", "PKOBP", "PLAY", "PZU",
                        "SANPL",
                        "SYNTHOS", "TAURONPE"]

file = open("akcje.csv", 'w')

with file:
    columns = ["name", "date", "open", "high", "low", "close", "volume"]
    writer = csv.DictWriter(file, fieldnames=columns, restval=None)
    writer.writeheader()
    for jsc in join_stock_companies:
        time_start = time.time()
        if jsc == "ASSECOPOL":
            period = [interval[x] for x in range(805)]
        elif jsc == "BOGDANKA":
            period = [interval[x] for x in range(245)]
        elif jsc == "EUROCASH":
            period = [interval[x] for x in range(1053)]
        elif jsc == "KERNEL":
            period = [interval[x] for x in range(55)]
        elif jsc == "SYNTHOS":
            period = [interval[x] for x in range(305)]
        elif jsc == "CCC":
            period = [interval[x] for x in range(245, 1247)]
        elif jsc == "CDPROJEKT":
            period = [interval[x] for x in range(805, 1247)]
        elif jsc == "CYFRPLSAT":
            period = [interval[x] for x in range(55, 1247)]
        elif jsc == "DINOPL":
            period = [interval[x] for x in range(1053, 1247)]
        elif jsc == "PLAY":
            period = [interval[x] for x in range(1053, 1247)]
        elif jsc == "ENEA":
            period = [interval[x] for x in range(55, 555)]
        elif jsc == "ENERGA":
            period = [interval[x] for x in range(55, 1052)]
        elif jsc == "JSW":
            period = [interval[x] for x in chain(range(55), range(556, 1247))]
        elif jsc == "LOTOS":
            period = [interval[x] for x in chain(range(55), range(305, 1247))]
        else:
            period = interval.copy()
        for date in period:
            # print(jsc, datetime.datetime.strftime(date, "%d-%m-%Y"))
            if jsc == "SANPL" and date not in [interval[x] for x in range(924, 1247)]:
                my_url = "https://www.gpw.pl/archiwum-notowan-full?type=10&instrument=BZWBK&date=" + datetime.datetime.strftime(date, "%d-%m-%Y")
            else:
                my_url = "https://www.gpw.pl/archiwum-notowan-full?type=10&instrument=" + jsc + "&date=" + datetime.datetime.strftime(date, "%d-%m-%Y")
            print(my_url)
            website = uReq(my_url)
            page = website.read()
            website.close()

            page_soup = soup(page, "html.parser")
            inf = page_soup.findAll("td", {"class": "left"})
            name = inf[0].contents[0]
            date = inf[1].contents[0]
            print(name, date)
            numbers = page_soup.findAll("td", {"class": "text-right"})
            values = []
            for i in {1, 2, 3, 4, 6}:
                number = str(numbers[i].contents[0])
                string = ""
                for char in number:
                    if char in "0123456789,":
                        if char == ",":
                            string += "."
                        else:
                            string += char
                values.append(float(string))

            open_stock = values[0]
            max_stock = values[1]
            min_stock = values[2]
            close_stock = values[3]
            volume = int(values[4])
            writer.writerow({"name": jsc, "date": date,
                             "open": open_stock, "high": max_stock, "low": min_stock, "close": close_stock,
                             "volume": volume})
            print(open_stock, max_stock, min_stock, close_stock, volume)
        time_end = time.time()
        print(time.strftime("%H:%M:%S", time.gmtime(time_end-time_start)))

file.close()
