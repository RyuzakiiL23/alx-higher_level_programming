#!/usr/bin/python3
"""  Lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    JOIN states ON states.id=cities.state_id""")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
