import sqlite3
import os
from tkinter import messagebox,messagebox

def create_table():
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS accounts
                  (id TEXT PRIMARY KEY, username text, password text, email text, phno text)''')
        conn.commit()
        conn.close()

def create_table_flight():
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS flightticket
                  (flight_id INTEGER PRIMARY KEY AUTOINCREMENT, passenger_name text, passenger_phno text, seat integer, boarding_time text, departure_date text, destination text)''')
        conn.commit()
        conn.close()

def add_flight(name, p_phno, seat, time, date, destination):
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('''INSERT INTO flightticket
                  (passenger_name, passenger_phno, seat, boarding_time, departure_date, destination) VALUES (?,?,?,?,?,?,?)''', (name, p_phno, seat, time, date, destination))
        conn.commit()
        conn.close()

def for_login(username, password):
        conn = sqlite3.connect("NewSystem3.db")
        c = conn.cursor()
        c.execute('SELECT * FROM accounts WHERE username = ? and password = ?', (username,password))
        if c.fetchone() is None:
                messagebox.showerror("Error","Invalid Credentials")
        else:
                print("Logged IN")
                

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
create_table_flight()