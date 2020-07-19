import sqlite3
import pandas as pd


# Query to calculate the average rating of the 2002 books
def calculate_average():
    conn = sqlite3.connect("books.sqlite")
    query = "Select avg(Rating) as promedio from books where PublishYear = 2002"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data
