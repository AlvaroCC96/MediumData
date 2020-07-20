import numpy as np
import pandas as pd
import sys

# Returns the size of a dataframe (df) in MB rounded to (n) decimals digits
def getSize(df, n):
    return round(sys.getsizeof(df)/(1024*1024),n)

######### Uncompressed #########

li = [] # This will be used to contain al frames from each csv

for i in range(1, 12):
    # Read each csv and add it to the dataframe list
    df = pd.read_csv("p" + str(i) + "_books_data.csv", usecols=["Id","Name", "Authors", "Rating","pagesNumber","Publisher","Language","ISBN","PublishDay","PublishMonth","PublishYear","CountsOfReview"])
    li.append(df)                

# Concatenate each frame into one    
frame = pd.concat(li, axis=0, ignore_index=True)
#print(frame)
uc_size = getSize(frame,3)
print(f'Uncompressed data frame: {uc_size} MB')

######### Compressed #########

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
#print(frame)
c_size =getSize(frame,3)
print(f'Compressed data frame with types: {c_size} MB')

factor = ((uc_size - c_size) / uc_size)*100
print (f'Compressed by {round(factor)}%')



