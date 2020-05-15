import sqlite3, time, datetime, uuid

def delete_message(messageID):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM messages WHERE messageID=?", [messageID])
    conn.commit()
    conn.close()
    return True

def favorite_message(messageID):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute("UPDATE messages SET flag=? WHERE messageID=?", [1,messageID])
    conn.commit()
    conn.close()
    return True

def get_user_message(userID):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages WHERE userTo=?",(userid))
    user_messages_info = cur.fetchall()
    conn.commit()
    conn.close()
    return user_messages_info

def create_message(senderID,contents,receiveID):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS messages (
                messageID text PRIMARY KEY,
                userFrom text NOT NULL,
                userTo text NOT NULL,
                timestamp text NOT NULL,
                contents text NOT NULL,
                flag binary Default 0)
                ''')
    unix=time.time()
    datestamp=datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')
    messageID = str(uuid.uuid4())
    cur.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?, 0)",(messageID,senderID,receiveID,datestamp,contents))
    conn.commit()
    conn.close()
