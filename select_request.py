from sqlalchemy import create_engine

db = 'postgresql://postgres:admin@localhost:5432/py48db'
engine = create_engine(db)
connection = engine.connect()

connection.execute('''SELECT title, year FROM albums
   WHERE year=2018;''').fetchall()

connection.execute('''SELECT title, duration FROM tracks
   WHERE duration = (SELECT MAX(duration) FROM tracks);''').fetchall()

connection.execute('''SELECT title from tracks
   WHERE duration >= 210;''').fetchall()

connection.execute('''SELECT title from compilations
   WHERE year BETWEEN 2018 AND 2020;''').fetchall()

connection.execute('''SELECT name from artists
   WHERE name NOT LIKE '%% %%';''').fetchall()

connection.execute('''SELECT title from tracks
   WHERE title LIKE '%%my%%';''').fetchall()