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
    cur.execute(sql, (userid,))
    conn.commit()

    return

def update_email(userid,email_addr):
    return

def get_user(userid):
    return

def inc_karma(userid):
    return

def dec_karma(userid):
    return

def create_user(username,email,password):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS user (
    			username text PRIMARY KEY,
    			email text NOT NULL,
    			password text NOT NULL)''')
    cur.execute("INSERT INTO user VALUES (username, email, password)")
	conn.commit()
	conn.close()
    return

def get_all_users():
    return