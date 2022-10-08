#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and
    lists all cities of that state, using database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name, password, db_name, state = sys.argv[1:]
    conn = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities {} {} '{}' {}".format(
            "JOIN states ON cities.state_id=states.id",
            "WHERE states.name LIKE", state,
            "ORDER BY cities.id ASC")
    cur.execute(query)
    data = cur.fetchall()
    states = ", ".join(row[0] for row in data)
    print(states)
    cur.close()
    conn.close()
