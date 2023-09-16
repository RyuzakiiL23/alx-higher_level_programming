#!/usr/bin/python3
"""  lists all states from hbtn_0e_0_usa """
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
    data = sys.argv[4]
    cursor.execute("""SELECT cities.name FROM cities JOIN states ON
                    states.id=cities.state_id WHERE states.name=%s""", (data,))
    cities = [city[0] for city in cursor.fetchall()]
    print(', '.join(cities))
    cursor.close()
    db.close()
