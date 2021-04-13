import sqlite3 as sql

wig20 = sql.connect("akcje.sqlite")
wig20.execute("DROP TABLE akcje")
wig20.execute("CREATE TABLE akcje (name VARCHAR(10), date DATE, open FLOAT, max FLOAT, min FLOAT, close FLOAT)")
wig20.execute("INSERT INTO akcje(name, date, open, max, min, close) VALUES('test', '20150227', 1.0, 2.5555, 3, 45.12343)")

c = wig20.cursor()
c.execute("SELECT * FROM akcje")
for row in c:
    print(row)

wig20.close()
