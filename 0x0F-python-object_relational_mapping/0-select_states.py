#!/usr/bin/python3
""" Script to connect to MySQL server on localhost at port 3306
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name, password, db_name = sys.argv[1:]
    conn = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    conn.close()
