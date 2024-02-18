#!/usr/bin/python3
"get states"
import sys
import MySQLdb


def main():
    user = sys.argv[1]
    ps = sys.argv[2]
    dbn = sys.argv[3]
    nm = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=ps, db=dbn, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (nm,))
    mylist = cur.fetchall()
    for row in mylist:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
