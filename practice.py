
import sqlite3

conn = sqlite3.connect("data.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE Employees(
    id integer PRIMARY KEY,
    name text NOT NULL,
    salary float NOT NULL
)"""
cursor.execute(sql_query)


sql_query1 = """ CREATE TABLE Employees1(
    id integer PRIMARY KEY,
    name text NOT NULL,
    salary float NOT NULL
)"""

cursor.execute(sql_query1)
