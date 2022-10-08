#!/usr/bin/python3
""" Script to connect to MySQL server on localhost at port 3306
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name, password, db_name = sys.argv[1:]
    db = MySQLdb.connect('localhost', user_name, password, db_name)
    cur = db.cursor()
    states = cur.execute("SELECT * FROM states ORDER BY id ASC")
    print(states)
    cur.close()
    db.close()
