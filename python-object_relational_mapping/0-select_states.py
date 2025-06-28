#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <username> <password> <database>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
