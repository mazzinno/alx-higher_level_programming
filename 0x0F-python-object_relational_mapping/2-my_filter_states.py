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
    query = "SELECT * FROM states WHERE name LIKE '{}'".format(nm)
    cur.execute(query + " ORDER BY id ASC")
    mylist = cur.fetchall()
    for row in mylist:
        if row[1] == nm:
            print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
