Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
file=open("Stars.csv","r")
search=input("Please enter the data you are searching for: ")
Please enter the data you are searching for: Brian
reader=csv.reader(file)
for row in file:
    if search in str(row):
        print(row)

        
Brian,73,Taurus

file=open("Stars.csv","r")
search=input("Please enter the data you are looking for: ")
Please enter the data you are looking for: Brian
reader=csv.reader(file)
for row in file:
    if search in str(row):
        print(row)

        
Brian,73,Taurus

