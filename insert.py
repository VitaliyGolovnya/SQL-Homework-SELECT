import sqlalchemy

db = 'postgresql://postgres:admin@localhost:5432/py48db'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

connection.execute('''INSERT INTO artists(name)
    VALUES('Bruno Mars'), 
    ('The Weeknd'), 
    ('Alla Pugacheva'), 
    ('Eminem'),
    ('Daft Punk'),
    ('Pendulum'),
    ('Timati'),
    ('DJ Smash');
    
    INSERT INTO albums(title, year)
    VALUES('Love''s Train', 2022),
    ('24K Magic', 2016),
    ('Приглашение на закат', 2008),
    ('Showdown', 2009),
    ('Hardware Limited, Vol. 3', 2006),
    ('Groove On', 2010),
    ('Curtain Call: The Hits', 2005),
    ('The Slim Shady LP', 1999);
    
    INSERT INTO genres(genre)
    VALUES('pop'),
    ('hip-hop'),
    ('rock'),
    ('funk'),
    ('drum-and-bass');

    INSERT INTO tracks(title, duration, album_id)
    VALUES('This is real slim shady', 190, 3),
    ('Epic fail', 281, 1),
    ('Snowflakes', 321, 4),
    ('Rambo', 131, 6),
    ('Tarantula', 170, 7),
    ('Hello puppy', 201, 5),
    ('Stan', 230, 8),
    ('Rolling tinder', 480, 4),
    ('Boss of the office', 130, 1),
    ('Let me show you the sun', 166, 4),
    ('Call me by my name', 261, 6),
    ('Real talk', 155, 2),
    ('Stay awake', 199, 6),
    ('Too many tracks', 560, 7),
    ('I''m sick of it already', 247, 4),
    ('To the moon and back', 378, 8);
    
    INSERT INTO compilations(title, year)
    VALUES('Best Hits of Summer 07', 2007),
    ('Various artists', 2020),
    ('Clubhouse mixes', 2002),
    ('Unlimited dance', 2013),
    ('Music from the future', 2024),
    ('Coronavision', 2020),
    ('Epic sad music', 2009),
    ('Nostalgic hits', 1999),
    ('Epic happy music', 2010),
    ('Hits of the decade', 2019);

    INSERT INTO artistgenre (artist_id, genre_id)
    VALUES(1, 5),
    (1, 3),
    (2, 4),
    (3, 1),
    (4, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (6, 4),
    (7, 2),
    (8, 3);

    INSERT INTO trackcompilation (compilation_id, track_id)
    VALUES(10, 5),
    (2, 15),
    (3, 6),
    (8, 6),
    (8, 5),
    (8, 1),
    (5, 1),
    (5, 2),
    (5, 3),
    (9, 2),
    (9, 14),
    (7, 15),
    (7, 6),
    (6, 6),
    (6, 5),
    (6, 1),
    (6, 9),
    (6, 2),
    (6, 3),
    (3, 2),
    (5, 14);

    INSERT INTO artistalbum (artist_id, album_id)
    VALUES(8, 5),
    (2, 8),
    (3, 6),
    (8, 6),
    (8, 2),
    (8, 1),
    (5, 1),
    (5, 2),
    (5, 3),
    (1, 2),
    (1, 8),
    (7, 8),
    (7, 6),
    (6, 6),
    (6, 5),
    (6, 1),
    (6, 2),
    (6, 4),
    (6, 3),
    (3, 2),
    (5, 4);

    ''')

