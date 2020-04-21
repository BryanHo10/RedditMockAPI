import sqlite3, time, datetime

def get_unique_post_score(postid):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("SELECT votes FROM posts WHERE postID=?", [postid])
	post_score = cur.fetchall()
	conn.commit()
	conn.close()
	return post_score

def get_scores(list_size):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM posts ORDER BY votes DESC LIMIT ?", [list_size])
	post_scores = cur.fetchall()
	conn.commit()
	conn.close()
	return post_scores

def get_list_scores(postIDset):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM posts where postID IN (?) ORDER BY votes DESC", [",".join(postIDset)] )
	post_scores = cur.fetchall()
	conn.commit()
	conn.close()
	return post_scores

def upvote_post(userID,postID):
	new_vote = get_unique_post_score(postID) + 1
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("UPDATE posts SET vote=? WHERE postID=?", [new_vote,postID])
	conn.commit()
	conn.close()
	return True

def downvote_post(userID,postID):
	new_vote = get_unique_post_score(postID) - 1
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("UPDATE posts SET vote=? WHERE postID=?", [new_vote,postID])
	conn.commit()
	conn.close()
	return True