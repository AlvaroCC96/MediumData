import sqlite3
import pandas as pd


def get_books_rating45():
    conn = sqlite3.connect("books.sqlite")
    query = "Select * from books where rating > 4.5"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data
