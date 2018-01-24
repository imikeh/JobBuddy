import sqlite3
sqlite_file = '/Users/mikehuang/Desktop/Demo/building_user_login_system-master/finish/database.db'
conn = sqlite3.connect(sqlite_file)

c = conn.cursor()

c.execute('SELECT * FROM {tn}'.format(tn='user'))
all_rows = c.fetchall()
print('1):', all_rows)

conn.commit()
conn.close()