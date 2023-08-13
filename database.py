import sqlite3
import os

def create_table():
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS accounts
                  (id TEXT PRIMARY KEY, username text, password text, email text, phno text)''')
        conn.commit()
        conn.close()

def fetch_data():
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('SELECT * FROM accounts')
        data = c.fetchall()
        conn.close()
        return data

def insert_customer(id, username, password, email, phno):
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('''INSERT INTO accounts
                  (id, username, password, email, phno) VALUES (?,?,?,?,?)''', (id, username, password, email, phno))
        conn.commit()
        conn.close()

def delete_customer(id):
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('''DELETE FROM accounts WHERE id = ?''', (id,))
        conn.commit()
        conn.close()

def update_customer(new_username, new_password, new_email, new_phno, id):
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('''UPDATE accounts SET username = ?, password = ?, email = ?, phno = ? WHERE id = ?''', (new_username, new_password, new_email, new_phno, id))
        conn.commit()
        conn.close()

def id_exists(id):
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('''SELECT COUNT(*) FROM accounts WHERE id = ?''', (id,))
        result=c.fetchone()
        conn.close()
        return result[0] > 0
    
create_table()
