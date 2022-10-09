#!/usr/bin/python3
"""
    This script lists all cities from the database hbtn_0e_4_usa
    Usage: ./5-filter_cities.py <mysql username> \
                                <mysql password> \
                                <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()

    mycursor.execute("SELECT cities.name \
                     FROM cities \
                     INNER JOIN states \
                     ON cities.state_id = states.id \
                     WHERE states.name = %(city_name)s \
                     ORDER BY cities.id ASC", {"city_name": sys.argv[4]})

    print(", ".join([city[0] for city in mycursor.fetchall()]))
    mycursor.close()
    db.close()
