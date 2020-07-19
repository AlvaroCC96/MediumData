import pandas as pd
import numpy as np
import sys

"""
Dataframe que almacena solamente las columnas (id,name,publishYear,ratting), debido a que el resto
no son necesarias para efectos academicos
"""

totalSize = 0

for i in range(1, 12):

    df = pd.read_csv("p"+str(i)+"_books_data.csv", usecols=["Name", "PublishYear", "Rating"],
                     dtype={
                         "Name": "string",
                         "PublishYear": np.int16,
                         "Rating": np.float16
                    })
    totalSize = totalSize + sys.getsizeof(df) / (1024 * 1024)

print("Total bytecount: ", round(totalSize, 3), " MB")


