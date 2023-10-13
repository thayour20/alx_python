#!/usr/bin/python
"""
    script that list all states in the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv 

if __name__ == "__main__":
    db =MySQLdb.connect (
        host = "localhost",
        port = 3306,
        user = argv[1],
        passwd = argv[2],
        db = argv[3]

    )

    cursor = db.cursor()
    cursor.execute ("SELECT * FROM cities ORDER BY id ASC")

    results = cursor.fetchall()

    for result in results:
        print(result)

    cursor.close()
    db.close()


