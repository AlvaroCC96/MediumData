import Compressor
import FileAverage
import FileWriter
import sys
import time

# (1)
# Compressor of data from books_data.csv
Compressor.index_data()

# (2)
# TODO: FIX
# data = FileWriter.get_books_rating45()
# sizedata = sys.getsizeof(data) / (1024 * 1024)
# print("Total bytecount from database: ", sizedata, " MB")

# (3)
# Average of the ratings for the books of the year 2002
start = time.time()
average = FileAverage.calculate_average()
print("Average: ", average.values[0][0])  # TODO: Fix , get otherwise
print("Time: ", round(time.time() - start, 3))
