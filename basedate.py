import sqlite3
import random

'''conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute("""CREATE TABLE Sticker
                  (Sticker_id text, Unique_id_code)
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
    cursor.executemany("INSERT INTO Sticker VALUES (?,?)", (update_table))
    conn.commit()
    conn.close()


def read_sql():
    conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    sql = "SELECT * FROM Sticker"
    cursor.execute(sql)
    all_list = cursor.fetchall()
    conn.close()
    #check_reading()попытка чека прочтения
    return all_list


'''def check_reading():
    global basedate_check_reading
    basedate_check_reading = 1
    return basedate_check_reading'''

#sql_function()
#basedate_check_reading = 0
#bd_list_all = read_sql()


# print(type(Sticker))

#conn.commit()