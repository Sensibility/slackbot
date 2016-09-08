import MySQLdb

# db = MySQLdb.connect(host="superphage.us",    # your host, usually localhost
#                      user="username",         # your username
#                      passwd='normies get out',  # your password
#                      db="laravel")        # name of the data base

# cur = db.cursor()

# cur.execute("SELECT * FROM users")

# for row in cur.fetchall():
# 	print row

# db.close()

class DB():
	def __init__(self, host, user, passwd, db):
		self.host = host
		self.user = user
		self.pw = passwd
		self.db = db
		self.connect()

	def connect(self):
		self.db = MySQLdb.connect(self.host, self.user, self.pw, self.db)
		self.cur = self.db.cursor()