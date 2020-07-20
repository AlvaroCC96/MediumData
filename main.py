import Compressor
import FileAverage
import FileWriter
import sys
import time


"""
@author Alvaro Castillo , Patricio Araya
"""


# (1)
# Compressor of data from books_data.csv
start = time.time()
Compressor.index_data()
print("Time: ", round(time.time() - start, 3))
print()

# (2)
start = time.time()
FileWriter.get_books_rating45()
print("Time: ", round(time.time() - start, 3))
print()

# (3)
# Average of the ratings for the books of the year 2002
start = time.time()
average = FileAverage.calculate_average()
print("Average: ", round(average, 3))
print("Time: ", round(time.time() - start, 3))
