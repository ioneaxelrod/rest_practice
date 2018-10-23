import MySQLdb

db = MySQLdb.connect(host="localhost",
                    user="root",
                    passwd="",
                    db="teamdata")

cursor = db.cursor()
# cursor.execute("""SELECT * FROM teams""")
# print(cursor.fetchall())
# for row in cursor:
#     print(row)
# cursor.execute("""SELECT * FROM users""")
# print(cursor.fetchall())
# for row in cursor:
#     print(row)
# cursor.execute("""SELECT * FROM points""")
# print(cursor.fetchall())
# for row in cursor:
#     print(row)

