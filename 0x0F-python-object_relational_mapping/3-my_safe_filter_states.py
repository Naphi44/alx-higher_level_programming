#!/usr/bin/python3
"""
    This script takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa
    where `name` matches the argument.
    Safe from MySQL injections
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

    mycursor.execute("SELECT * FROM states WHERE states.name=%(name_of_state)s \
                     ORDER BY states.id ASC", {"name_of_state": sys.argv[4]})

    [print(state) for state in mycursor.fetchall()]
    mycursor.close()
    db.close()
