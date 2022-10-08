#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name, password, db_name = sys.argv[1:]
    conn = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name {} {} {}".format(
            "FROM cities",
            "LEFT OUTER JOIN states ON cities.state_id=states.id",
            "ORDER BY cities.id ASC")
    cur.execute(query)
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    conn.close()
