import sys
import time
import numpy as np
import pandas as pd
### Load .csv data

li = [] # This will be used to contain al frames from each csv

for i in range(1, 12):
    # Read each csv and add it to the dataframe list
    df = pd.read_csv("p" + str(i) + "_books_data.csv", usecols=["Id","Name", "Authors","Rating","pagesNumber","Publisher","Language","ISBN","PublishDay","PublishMonth","PublishYear","CountsOfReview"],
                        dtype={
                            "Id": np.uint32,
                            "Name": str,
                            "Authors": str,
                            "Rating": np.float,
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

start = time.time()
# Filter the frame by publish year = 2002
year2002 = frame["PublishYear"] == 2002
filt_df = frame[year2002]
# Print avg
print(f'Avg rating: {filt_df["Rating"].mean()}')
print(f'In {round(time.time() - start,3)} seconds')

