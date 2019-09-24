#https://docs.python.org/3/library/csv.html
#https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime


import csv
from datetime import datetime

import csv



data = []

with open('BANK.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        
        BANK_ID = row[0]
        NAME = row[1]
        SHORT_NAME = row[-2]
        UPDATE_DATE = None
        try:
            UPDATE_DATE = datetime.strptime(row[-1][0:10],'%Y-%m-%d')
        except ValueError:
            pass                
        data.append([BANK_ID,NAME,SHORT_NAME,UPDATE_DATE])
        
        #print(BANK_ID,NAME,UPDATE_DATE)

return_file = "BANK2.csv"
file = open(return_file, "w")
write = csv.writer(file)
write.writerow(["BANK_ID","NAME","SHORT_NAME","UPDATE_DATE"])
write.writerows(data)
file.close()
        


#Without CSV module
'''
path = "BANK.csv"
lines = [line for line in open(path)]
print(lines[1])
'''