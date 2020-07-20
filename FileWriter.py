import sqlite3
import pandas as pd
import sys

"""
@author Alvaro Castillo , Patricio Araya
"""


# Gets the books with rating 4.5 and stores them in a csv.
def get_books_rating45():
    conn = sqlite3.connect("books.sqlite")
    query = "Select * from books where rating > 4.5"
    dataFrame = pd.read_sql_query(query, conn)
    conn.close()
    sizedata = sys.getsizeof(dataFrame) / (1024 * 1024)
    print("Total bytecount from dataframe: ", sizedata, " MB")
    # save dataframe on csv , index false because it already exists inside the dataframe
    dataFrame.to_csv('csv_rating.csv', index=False)
