import sqlite3, time, datetime, uuid

def get_posts_from(n,community_id = None):
    conn = sqlite3.connect('example.db')
	cur = conn.cursor()
    if community_id != None:
        cur.execute("SELECT * FROM posts WHERE communityID=? LIMIT ?",(community_id,n))
    else
        cur.execute("SELECT * FROM posts LIMIT ?",(n))
	conn.commit()
	conn.close()
    return

def get_user_posts(userid):
    conn = sqlite3.connect('example.db')
	cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE username=?",(userid))
	conn.commit()
	conn.close()
    return

def get_post(userid,postid):
    conn = sqlite3.connect('example.db')
	cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE username=? postID=?",(userid,postid))
	conn.commit()
	conn.close()
    return

def delete_post(userid,postid):
    conn = sqlite3.connect('example.db')
	cur = conn.cursor()
    cur.execute("DELETE FROM posts WHERE username=? postID=?",(userid,postid))
	conn.commit()
	conn.close()
    return

def create_post(userid,message,userid,url=None,community_id):
    conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS posts (
    			postID text PRIMARY KEY,
    			username text NOT NULL,
    			message text NOT NULL),
                communityID text NOT NULL),
                URL text NOT NULL),
                date_created text NOT NULL),
                ''')
    unix=time.time()
	datestamp=datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')
    postID = str(uuid.uuid4())
    cur.execute("INSERT INTO posts VALUES (?, ?, ?, ?, ?, ?)",(postID,userid,message,community_id,url,datestamp))
	conn.commit()
	conn.close()
    return