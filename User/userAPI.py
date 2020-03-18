import sqlite3
#conn = sqlite3.connect('example.db')

#cur = conn.cursor()

# Create table
#cur.execute('''CREATE TABLE stocks
			 #(date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
#cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()


def delete_user(userid):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	sql = 'DELETE FROM user WHERE userid=?'
	cur.execute(sql, (userid))
	conn.commit()

	return True

def update_email(userid,email_addr):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("UPDATE user SET email=? WHERE userid=?", (email_addr,userid))
	conn.commit()
	conn.close()
	return True

def get_user(userid):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM user WHERE userid=?", (userid))

	user_info = cur.fetchall()

	conn.commit()
	conn.close()
	return user_info



def inc_karma(userid):
	new_karma = get_karma(userid) + 1
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("UPDATE user SET karma=? WHERE userid=?", (new_karma,userid))
	conn.commit()
	conn.close()
	return True

def dec_karma(userid):
	new_karma = get_karma(userid) - 1
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("UPDATE user SET karma=? WHERE userid=?", (new_karma,userid))
	conn.commit()
	conn.close()
	return True

def get_karma(userid):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("SELECT karma FROM user WHERE userid=?", (userid))

	user_karma = cur.fetchall()

	conn.commit()
	conn.close()
	return user_karma

def create_user(username_in,email_in,password_in):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS user (
				username text PRIMARY KEY,
				email text NOT NULL,
				password text NOT NULL,
				karma real DEFAULT 0)''')
	cur.execute("INSERT INTO user VALUES (?, ?, ?, 0)",(username_in,email_in,password_in))
	conn.commit()
	conn.close()

def get_all_users():
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()

	cur.execute("SELECT * FROM user")
	users_info = cur.fetchall()

	conn.commit()
	conn.close()
	return users_info