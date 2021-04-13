# import datetime
#
# start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
# end = datetime.datetime.strptime("31-12-2019", "%d-%m-%Y")
# interval = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
# print(interval[100])
# print(len(interval))

# import csv
#
# file = open("akcje.csv", 'w')
# with file:
#     columns = ["name", "date", "open", "high", "low", "close", "volume"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerow({columns[0]: "PEKAO", columns[1]: "27-07-2017",
#                      columns[2]: 100.0, columns[3]: 102.0,
#                      columns[4]: 97.56, columns[5]: 99.0,
#                      columns[6]: 11564})
#     writer.writerow({columns[0]: "PEKAO", columns[1]: "28-07-2017",
#                      columns[2]: 99.0, columns[3]: 105.0,
#                      columns[4]: 99.99, columns[5]: 105.0,
#                      columns[6]: 55555})
#     writer.writerow({columns[0]: "PEKAO", columns[1]: "29-07-2017",
#                      columns[2]: 105.0, columns[3]: 105.5,
#                      columns[4]: 95.76, columns[5]: 100.0,
#                      columns[6]: 10})
#
# file.close()
# file = open("akcje.csv", 'r')
# with file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"], row["date"], row["open"], row["high"], row["low"], row["close"], row["volume"])



