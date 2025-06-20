import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'Data', 'chats.db')
conn = sqlite3.connect(DATA_PATH)
cursor = conn.cursor()

def add_data(query):
    table = "INSERT INTO ASSISTANT(QUERY, DATE_TIME) VALUES (?, datetime('now', 'localtime'))"
    cursor.execute(table, (query, ))
    conn.commit()
    return True

def get_data():
    data = cursor.execute("SELECT * FROM ASSISTANT")
    table_head = []
    for column in data.description:
        table_head.append(column[0])
    print("{:<14} {:<79} {:<20}".format(table_head[0], table_head[1], table_head[2]))
    print()
    for row in data:
        print("{:<14} {:<79} {:<20}".format(row[0], row[1], row[2]))