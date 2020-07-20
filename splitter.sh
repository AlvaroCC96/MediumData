#!/bin/sh
# Split the csv
echo Splitting books_data.csv
echo part 1/11
sed -n 1,58293p books_data.csv > p1_books_data.csv
echo part 2/11
sed -n 58294,99363p books_data.csv > p2_books_data.csv
echo part 3/11
sed -n 99364,156410p books_data.csv > p3_books_data.csv
echo part 4/11
sed -n 156411,212593p books_data.csv > p4_books_data.csv
echo part 5/11
sed -n 212594,269180p books_data.csv > p5_books_data.csv
echo part 6/11
sed -n 269181,324336p books_data.csv > p6_books_data.csv
echo part 7/11
sed -n 324337,379196p books_data.csv > p7_books_data.csv
echo part 8/11
sed -n 379197,436040p books_data.csv > p8_books_data.csv
echo part 9/11
sed -n 436041,491955p books_data.csv > p9_books_data.csv
echo part 10/11
sed -n 491956,543440p books_data.csv > p10_books_data.csv
echo part 11/11
sed -n 543441,585607p books_data.csv > p11_books_data.csv
echo 'done'