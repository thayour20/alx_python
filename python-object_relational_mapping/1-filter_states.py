#!/usr/bin/python
"""
    python script that list all states that start with N
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3],

    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE '%N' ORDER BY ID ASC")
    rows = cursor.fetchall()
    for row in rows:
        if row [1][0] == 'N':
            print (row)

    cursor.close()
    db.close()

