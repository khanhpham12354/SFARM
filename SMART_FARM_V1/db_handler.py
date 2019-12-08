import sqlite3 as sql
from datetime import datetime
# hàm insert dữ liệu nhiệt độ độ ẩm vào databases


def insert_data(Name, Id, Signal, Battery, Value, Temp):
    path = "databases\\DB_OF_SFARM.db"
    con = sql.connect(path)
    table_name = "data_of_"+str(datetime.now().day) + "_" + \
        str(datetime.now().month) + "_" + str(datetime.now().year)
    with con:
        cur = con.cursor()
        cmd = "CREATE TABLE IF NOT EXISTS " + table_name + '''(
			name TEXT NOT NULL,
			id TEXT NOT NULL,
			signal TEXT NOT NULL,
			battery INT,
			value   INT,
			temp  INT,
			time TEXT NOT NULL )
			'''
        cur.execute(cmd)
        cmd = "INSERT INTO " + table_name + " VALUES(?,?,?,?,?,?,?)"
        Time_read = str(datetime.now().hour) + ":" + \
            str(datetime.now().minute) + ":" + \
            str(datetime.now().second)
        # print("Name: ", Name, "ID: ",
        #       Id, " Signal: ", Signal, "Battery: ", Battery, "Value: ", Value, "Temp: ", Temp, "time: ", Time_read)
        cur.execute(cmd, (Name, Id, Signal, Battery, Value, Temp, Time_read))
    con.close()


def Delete_all_tb():
    path = "databases\\DB_OF_SFARM.db"
    con = sql.connect(path)
    with con:
        cur = con.cursor()
        tables = list(cur.execute(
            "select name from sqlite_master where type is 'table'"))
        cur.executescript(
            ';'.join(["drop table if exists %s" % i for i in tables]))
    con.close()
