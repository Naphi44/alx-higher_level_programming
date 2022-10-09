#!/usr/bin/python3
"""
    This script lists all states with a name starting with `N`
    from the database hbtn_0e_0_usa
    Usage: ./1-filter_states.py <mysql username> \
                                <mysql password> \
                                <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
    mycursor.execute(query)

    [print(state) for state in mycursor.fetchall()]
