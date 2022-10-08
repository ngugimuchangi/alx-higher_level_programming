#!/usr/bin/python3
""" Script that list all starts with a name starting with N(upper N)
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name, password, db_name = sys.argv[1:]
    conn = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY'N%' ORDER BY id ASC"
    cur.execute(query)
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    conn.close()
