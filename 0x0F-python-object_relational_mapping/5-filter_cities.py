#!/usr/bin/python3
"arisnkr"
import sys
import MySQLdb


def main():
    user = sys.argv[1]
    ps = sys.argv[2]
    dbn = sys.argv[3]
    st = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=ps, db=dbn, charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                LIKE %s=states.name
                ORDER BY cities.id ASC""", (st,))
    mylist = cur.fetchall()
    re = ""
    for r in mylist:
        re += r[0] + ", "
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
