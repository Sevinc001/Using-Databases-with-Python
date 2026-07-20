 import sqlite3
import csv

# 1. Connect to the database
conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

# 2. Create tables (fresh start)
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE);
CREATE TABLE Genre (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE);
CREATE TABLE Album (id INTEGER PRIMARY KEY AUTOINCREMENT, artist_id INTEGER, title TEXT UNIQUE);
CREATE TABLE Track (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER);
''')

# 3. Read CSV and insert data
with open('tracks.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # Skip header
    for row in reader:
        name, title, album, count, rating, len, genre = row
        
        # Insert/Select Artist
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (name,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (name,))
        artist_id = cur.fetchone()[0]
        
        # Insert/Select Genre
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]
        
        # Insert/Select Album
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]
        
        # Insert/Replace Track
        cur.execute('INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)', 
                    (title, album_id, genre_id, len, rating, count))

conn.commit()
conn.close()
print("Music database created successfully!")
