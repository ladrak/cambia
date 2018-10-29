#!/usr/bin/python
import sys, csv
    
with open("input.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

with open('output.csv', mode='w') as sorted_csv:
    writer = csv.writer(sorted_csv,
     delimiter=',')
    writer.writerow(sorted(reader, reverse))