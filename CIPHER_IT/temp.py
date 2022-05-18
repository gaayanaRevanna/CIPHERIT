import sqlite3
con=sqlite3.connect(database=r'hacked.db')
cur=con.cursor()
cur.execute("select * from Hacked_Database where phoneno LIKE '9481041406'")
rows=cur.fetchall()
print(rows)
self.new_win=Toplevel(self.root)
self.new_obj=databaseClass(self.new_win)
      