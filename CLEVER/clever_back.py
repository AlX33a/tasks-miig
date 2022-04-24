from msilib.schema import Error
import sqlite3
import re


def start():
    conn = sqlite3.connect('first_db.db', check_same_thread=False)
    curs = conn.cursor()
    
    curs.execute("""CREATE TABLE IF NOT EXISTS 'first' (
        'name' TEXT,
        'type' TEXT,
        'cost' INTEGER,
        'value' TEXT
        )""")
    conn.commit()
    
def check(name):
    conn = sqlite3.connect('first_db.db', check_same_thread=False)
    curs = conn.cursor()
    
    curs.execute("SELECT name, type, cost, value FROM first WHERE name = ?",(name,))
    strin = str(curs.fetchone()).replace("'","") 
    string = strin[1:] + strin[:-1]
    return string

def first_add(list):
    conn = sqlite3.connect('first_db.db', check_same_thread=False)
    curs = conn.cursor()

    curs.executemany("INSERT INTO first VALUES (?, ?, ?, ?)", list)
    conn.commit()

def first_check():
    conn = sqlite3.connect('first_db.db', check_same_thread=False)
    curs = conn.cursor()
    
    curs.execute("SELECT name FROM first WHERE name = 'clever'")
    if str(curs.fetchone()) == "('clever',)":
        return True
    else:
        return False

'''    
def add_new_id(name, type, cost, value):
    conn = sqlite3.connect('first_db.db', check_same_thread=False)
    curs = conn.cursor()

    curs.execute("INSERT INTO first (name, type, cost, value) VALUES (?, ?, ?, ?)",(name, type, cost, value))
    conn.commit()
'''

#clever_back.check('ножки').split(',')[0]

'''    
import clever_back

# name, type, cost, value

clever_back.start()
if clever_back.first_check():
    pass
else:
    list = [
        ('clever', 'clever', 1, 'clever'),
        ('ножки', 'материал', 3000, 'шт'),
    ]
    clever_back.first_add(list)
'''