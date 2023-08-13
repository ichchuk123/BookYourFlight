import sqlite3
import os

def create_table():
    if os.path.exists("NewSystem2.db"):
        conn = sqlite3.connect("NewSystem2.db")
    else:
        conn = sqlite3.connect("NewSystem2.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS accounts
                  (id username TEXT PRIMARY KEY, password integer, email text, phno text)''')
        conn.commit()
        conn.close()

def fetch_data():
    if os.path.exists("NewSystem2.db"):
        conn = sqlite3.connect("NewSystem2.db")
    else:
        conn = sqlite3.connect("NewSystem2.db")
        c = conn.cursor()
        c.execute('SELECT * FROM accounts')
        data = c.fetchall()
        conn.close()
        return data

def insert_customer(username, password, email, phno):
    if os.path.exists("NewSystem2.db"):
        conn = sqlite3.connect("NewSystem2.db")
    else:
        conn = sqlite3.connect("NewSystem2.db")
        c = conn.cursor()
        c.execute('''INSERT INTO accounts
                  (username, password, email, phno) VALUES (?,?,?,?)''', (username, password, email, phno))
        conn.commit()
        conn.close()

def delete_customer(username):
    if os.path.exists("NewSystem2.db"):
        conn = sqlite3.connect("NewSystem2.db")
    else:
        conn = sqlite3.connect("NewSystem2.db")
        c = conn.cursor()
        c.execute('''DELETE FROM accounts WHERE id = ?''', (username,))
        conn.commit()
        conn.close()

def update_customer(new_username, new_password, new_email, new_phno):
    if os.path.exists("NewSystem2.db"):
        conn = sqlite3.connect("NewSystem2.db")
    else:
        conn = sqlite3.connect("NewSystem2.db")
        c = conn.cursor()
        c.execute('''UPDATE accounts SET username = ?, password = ?, email = ?, phno = ? WHERE username = ?''', (new_username, new_password, new_email, new_phno))
        conn.commit()
        conn.close()

def id_exists(username):
    if os.path.exists("NewSystem2.db"):
        conn = sqlite3.connect("NewSystem2.db")
    else:
        conn = sqlite3.connect("NewSystem2.db")
        c = conn.cursor()
        c.execute('''SELECT COUNT(*) FROM accounts WHERE id = ?''', (username,))
        result=c.fetchone()
        conn.close()
        return result[0] > 0
    
create_table()
