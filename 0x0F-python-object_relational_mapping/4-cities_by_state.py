#!/usr/bin/python3
"get all of the states"
import sys
import MySQLdb


def main():
    user = sys.argv[1]
    ps = sys.argv[2]
    dbn = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=ps, db=dbn, charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    mylist = cur.fetchall()
    for row in mylist:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
