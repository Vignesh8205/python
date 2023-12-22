import sqlite3
con=sqlite3.connect("test.db")
print("coneted")
# ************************
cursor=con.cursor() #conection the line
# ################################3
def viwe_data():
    cursor.execute("select * from vicky")
    row=cursor.fetchall()
    for i in row:
        print(i)
    cursor.close()
    con.close()
viwe_data()