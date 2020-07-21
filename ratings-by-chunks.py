import sys
import time
import numpy as np
import pandas as pd

"""
This script load the csv in chunks of max 10MB and filter the rows where "Rating"
column is greater than 4.5, then save this filtered data into a .csv.

The commented section generates the .csv necessary to use this script.
"""


## Helper function
# Returns the size of a dataframe (df) in MB rounded to (n) decimals digits
def getSize(df, n):
    return round(sys.getsizeof(df)/(1024*1024),n)

"""
### Use this scipt to create a clean version of the data csv ##
"""

"""
### Load .csv data

li = [] # This will be used to contain al frames from each csv

for i in range(1, 12):
    # Read each csv and add it to the dataframe list
    df = pd.read_csv("p" + str(i) + "_books_data.csv", usecols=["Id","Name", "Authors","Rating","pagesNumber","Publisher","Language","ISBN","PublishDay","PublishMonth","PublishYear","CountsOfReview"],
                        dtype={
                            "Id": np.uint32,
                            "Name": str,
                            "Authors": str,
                            "Rating": np.float16,
                            "pagesNumber": np.int16,
                            "Publisher": str,
                            "Language":str,
                            "ISBN": str,
                            "PublishDay": np.int8,
                            "PublishMonth":np.int8,
                            "PublishYear":np.int16,
                            "CountsOfReview": np.int16,
                            

                        })
    li.append(df)                

# Concatenate each frame into one    
frame = pd.concat(li, axis=0, ignore_index=True)
print(f'Compressed data frame with types: {getSize(frame,3)} MB')

# Merge all csv into one
frame.to_csv("clean_books_data.csv")
"""

"""
### Load data raw and print its memory usage
"""
"""
df= pd.read_csv("clean_books_data.csv")
print(f'Raw df: {getSize(df,3)}MB')
"""

"""
# Load the data in chunks of max 10 MB and 
"""

start = time.time()
chunk_num = 1
for chunk in pd.read_csv("clean_books_data.csv", chunksize=24500, dtype={
                            "Id": np.uint32,
                            "Name": str,
                            "Authors": str,
                            "Rating": np.float16,
                            "pagesNumber": np.int16,
                            "Publisher": str,
                            "Language":str,
                            "ISBN": str,
                            "PublishDay": np.int8,
                            "PublishMonth":np.int8,
                            "PublishYear":np.int16,
                            "CountsOfReview": np.int16,
                        }):

    # Print statistics: 
    # Chunk number
    print(f'Chunk: {chunk_num}')
    chunk_num +=1
    # Calculate the total of memory usage per chunk 
    sum = 0
    for i in chunk.memory_usage(deep=True):
        sum += i
    # Print the memory usage in MB, raise an alert if > 10MB   
    memory = sum/(1024*1024)
    if memory > 10:
        print(f'Memory limit reached. Chunk size: {memory}MB')
    else:
        print(f'Memory OK: {memory}MB')

    filter = chunk["Rating"] > 4.5
    df_filtered = chunk[filter]
    df_filtered.to_csv("test.csv",mode='a')
 
    
print(f'Data filtered in: {round(time.time() - start,3)} seconds')



