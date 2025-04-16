"""
module4ch16.py
IvyTecy SDEV220 
April 16, 2025
by Paul Renaud
Most of this code is not actually part of the assignment, as it was just me creating the db.
So it is commented out.
The first part (with the zoo) is from the textbook. The second part (books) is from the question,
but the final part (with sqlalchemy) will likely fail unless the books db is created first, and
you pip install sqlalchemy.

"""

import sqlite3

'''
conn = sqlite3.connect("enterprise.db")
curs = conn.cursor()
create_new = False
if create_new:
	curs.execute("""CREATE TABLE zoo
		(critter VARCHAR(20) PRIMARY KEY,
		count INT,
		damages FLOAT)""")
	
	curs.execute("INSERT INTO zoo VALUES ('duck', 5, 0.0)")
	curs.execute("INSERT INTO zoo VALUES ('bear', 2, 1000.0)")
	ins = "INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)"
	curs.execute(ins, ("weasel", 1, 2000.0))
	
print("In order by count")
curs.execute("SELECT * from zoo ORDER BY count")
print(curs.fetchall())

print("In order by count descending")
curs.execute("SELECT * from zoo ORDER BY count DESC")
print(curs.fetchall())

print("Show line with max damages")
curs.execute("""SELECT * FROM zoo WHERE
		damages = (SELECT MAX(damages) FROM zoo)""")
print(curs.fetchall())

conn.commit()
curs.close()
conn.close()

'''

'''
# new database
print("\n New database")

conn = sqlite3.connect("books.db")
curs = conn.cursor()

create_new = False
if create_new:
	curs.execute("""CREATE TABLE books
		(title VARCHAR(50) PRIMARY KEY,
		author VARCHAR(50),
		year INT)""")

	ins = "INSERT INTO books (title, author, year) VALUES(?, ?, ?)"
	curs.execute(ins, ("The Weirdstone of Brisingamen", "Alan Garner", 1960))
	curs.execute(ins, ("Perdido Street Station", "China Miéville", 2000))
	curs.execute(ins, ("Thud!", "Terry Pratchett", 2005))
	curs.execute(ins, ("The Spellman Files", "Lisa Lutz", 2007))
	curs.execute(ins, ("Small Gods", "Terry Pratchett", 1992))
	
curs.execute("SELECT * FROM books")
print(curs.fetchall())

conn.commit()

curs.close()
conn.close()
'''

# 16.8 Using sqlalchemy
# Note, had to install sqlalchemy first with
# pip install sqlalchemy
# Also, textbook not quite right in implementation, as Engine does not have an execute() method, but
# Engine.connect() does. Also had to import text method.
print("\nUsing sqlalchemy")
import sqlalchemy as sa
from sqlalchemy import text
engine = sa.create_engine("sqlite:///books.db")
with engine.connect() as conn:
	rows = conn.execute(text("SELECT title FROM books ORDER BY title"))
	for row in rows:
		print(row)

"""
The output I got from this was:

Using sqlalchemy
('Perdido Street Station',)
('Small Gods',)
('The Spellman Files',)
('The Weirdstone of Brisingamen',)
('Thud!',)

"""
