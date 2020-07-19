import sqlite3
import pandas as pd
import numpy as np
import sys


# Function that is responsible for reading each dataframe, and storing them in a database
def index_data():
    sizedata = 0
    # Connection to the database
    db = sqlite3.connect("books.sqlite")
    for i in range(1, 12):
        # Reading of the dataframe, rescuing only useful data
        df = pd.read_csv("p" + str(i) + "_books_data.csv", usecols=["Name", "PublishYear", "Rating"],
                         dtype={
                             "Name": "string",
                             "PublishYear": np.int16,
                             "Rating": np.float16
                         })
        df.to_sql("books", db, if_exists="append")
        sizedata += sys.getsizeof(df)/(1024*1024)

    # Create a index
    db.execute("CREATE INDEX PublishYear ON books(PublishYear)")
    db.close()
    print("Total bytecount from dataframe: ", round(sizedata, 3), " MB")
    sizedata = sys.getsizeof(db)/(1024*1024)
    print("Total bytecount from database: ", sizedata, " MB")