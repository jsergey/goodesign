import os
import sqlite3

db_filename = '../decoupler.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = "select author, hash, commit_date, file, file_path, added, removed from commits"

    cursor.execute(query)

    for row in cursor.fetchall():
        author, hash, commit_date, file, file_path, added, removed = row
        print ('%-30s %-25s [%-65s] [%-65s] (%s) (%s)' % (author, commit_date, file, file_path, added, removed))

