#https://docs.python.org/3/library/csv.html

import csv
from datetime import datetime

import csv
with open('BANK.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(row)