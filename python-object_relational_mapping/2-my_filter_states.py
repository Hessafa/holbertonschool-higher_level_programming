#!/usr/bin/python3
"""This script lists all states matching a given name from the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of args (no validation needed per instructions)
    user, passwd, db, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to the database
    db_conn = MySQLdb.connect(host="localhost", port=3306,
                              user=user, passwd=passwd, db=db,
                              charset="utf8")
    cursor = db_conn.cursor()

    # Format query string exactly as requested (use format)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db_conn.close()
