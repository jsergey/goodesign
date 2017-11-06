import os
import sqlite3

db_filename = '../decoupler.db'
schema_filename = 'decoupler_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        conn.commit()
    else:
        print('Database exists, assume schema does, too.')
