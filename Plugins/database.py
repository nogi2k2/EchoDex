import sqlite3

conn = sqlite3.connect('../Data/chats/db')
cursor = conn.cursor()

def add_data(query):
    table = "INSERT INTO ASSISTANT(QUERY, DATE_TIME) VALUES (?, datetime('now', 'localtime'))"
    cursor.execute(table, (query, ))
    conn.commit()
    return True

def get_data():
    data = cursor.execute("SELECT * FROM ASSISTANT")
    table_head = []
    for column in data.desription:
        table_head.append(column[0])
    print("{:<14} {:<79} {:<20}".format(table_head[0], table_head[1], table_head[2]))
    print()
    for row in data:
        print("{:<14} {:<79} {:<20}".format(row[0], row[1], row[2]))