#!/usr/bin/python3
"""
    This script lists all cities from the database hbtn_0e_4_usa
    Usage: ./4-cities_by_state.py <mysql username> \
                                  <mysql password> \
                                  <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities \
             INNER JOIN states \
             ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    mycursor.execute(query)

    [print(city) for city in mycursor.fetchall()]
    mycursor.close()
    db.close()
