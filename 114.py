Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
start=int(input("Please enter the starting year: "))
Please enter the starting year: 1900
end=int(input("Please enter the end year: "))
Please enter the end year: 2023
file=list(csv.reader(open("Books.csv")))
tmp=[]
for row in file:
    tmp.append(row)
x=0
SyntaxError: invalid syntax
X=0
for row in tmp:
    if int(tmp[X][0])>=start and int(tmp[X][2])<=end:
        print(tmp[x])
        X=X+1

        




