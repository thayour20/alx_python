#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a
given name and is safe from MySQL injections
"""
import MySQLdb
import sys

def states_search():
    db = MySQLdb.connect (
        host = "localhost",
        port = 3306,
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name iIS LIKE %s ORDER BY id ASC".format(sys.argv[4]))

    results = cursor.fetchall()
    for result in results:
        if result == sys.argv[4]:
            print(result)
    cursor.close()
    db.close()

if __name__ == "__main__":
    states_search()

