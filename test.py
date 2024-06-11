import pygsheets
import sqlite3
import pandas as pd

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

#cur.execute("CREATE TABLE movie(title, year, score)")
#cur.execute("""
#    INSERT INTO movie VALUES
#        ('Monty Python and the Holy Grail', 1975, 8.2),
#        ('And Now for Something Completely Different', 1971, 7.5)
#""")
#data = [
#    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#    ("Monty Python's The Meaning of Life", 1983, 7.5),
#    ("Monty Python's Life of Brian", 1979, 8.0),
#]
#cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
#con.commit()  # Remember to commit the transaction after executing INSERT.

#for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
#    print(row)

query='SELECT * from movie'
df = pd.read_sql(query,con)
print(df.head())

path = '/home/laxmij/ebento_backend-pandas/src/ebento-f8dcf-128ecabe0b5e.json'
gc = pygsheets.authorize(service_account_file=path)
sh=gc.open('Ebento_tc_events')
wrkb = sh[9]
wrkb.clear()
wrkb.set_dataframe(df,(1,1))
