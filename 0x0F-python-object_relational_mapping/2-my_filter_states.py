#!/usr/bin/python3
"""
    This script takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa
    where `name` matches the argument.
    Usage: ./2-my_filter_states.py <mysql username> \
                                   <mysql password> \
                                   <database name>  \
                                   <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}'\
             ORDER BY states.id".format(sys.argv[4])
    mycursor.execute(query)

    [print(state) for state in mycursor.fetchall()]
    mycursor.close()
    db.close()
