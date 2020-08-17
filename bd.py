import sqlite3
import random

'''conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute("""CREATE TABLE Sticker
                  (Sticker_id text)
               """)'''

def random_sticker():
    conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    sql = "SELECT * FROM Sticker"
    cursor.execute(sql)
    exit_sql = (cursor.fetchall())
    large = len(exit_sql)
    a = random.randint(0, (large - 1))
    random_sticker_id = exit_sql[a]
    return random_sticker_id


def sql_function(update_table):
    conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Sticker VALUES (?)", (update_table))
    conn.commit()
    conn.close()


def read_sql():
    conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    sql = "SELECT * FROM Sticker"
    cursor.execute(sql)
    print(cursor.fetchall())
    conn.close()


#sql_function()
read_sql()



# print(type(Sticker))

#conn.commit()