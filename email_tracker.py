import sqlite3

# Connect to the database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Clean start: Drop table if it exists
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Get filename from user
fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox.txt'

try:
    fh = open(fname)
except FileNotFoundError:
    print('File not found! Please check the filename and try again.')
    exit()

for line in fh:
    if not line.startswith('From: '): continue
    
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    
    # Database logic: Check if domain exists
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))

conn.commit()
cur.close()
print("Processing complete! email_db.sqlite is ready.")
