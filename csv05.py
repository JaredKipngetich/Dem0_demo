Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
file=open("stars.csv","r")
reader = csv.reader(file)
rows=list(reader)
print(rows[0])
['Brian', '73', 'Taurus']
