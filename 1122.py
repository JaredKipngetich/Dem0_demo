Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
file=open("Books.csv","a")
num=int(input("Please enter the number of data entries you wish to add: "))
Please enter the number of data entries you wish to add: 4
for x in range(0,num):
    name=input("Please enter the name of the book you want to add: ")
    author=input("Please enter the name of the author: " )
    year=input("Please enter the year this was released: " )

    
Please enter the name of the book you want to add: James the Sweeper
Please enter the name of the author: Jacob Morrison
Please enter the year this was released: 2003
Please enter the name of the book you want to add: When The Sun Goes Down
Please enter the name of the author: Andrew Kibe
Please enter the year this was released: 2001
Please enter the name of the book you want to add: Damu Nyeusi
Please enter the name of the author: Ken Walibora
Please enter the year this was released: 2009
Please enter the name of the book you want to add: Alibaba and the seven thieves
Please enter the name of the author: Jackie Chandiru
Please enter the year this was released: 1997
newrecord = name + "," + author + "," + year + "\n"
file.write(str(newrecord))
51
file.close()

file.open("Books.csv","r")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    file.open("Books.csv","r")
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
file=open("Books.csv","r")
for row in file:
    print(row)
    file.close()

    
To kill a mockingbird, Harper Lee, 1960A brief history of Time, Stephen Hawkin, 1988A Great Gatsby, F.Scott Fitzgerald, 1922The Man Who Mistook His Wife For a Hat, Oliver Sacks, 1985Pride and Prejudice, Jane Austen, 1813You are Too Good to Feel this Way,Hellen Oyeyemi,2020

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for row in file:
ValueError: I/O operation on closed file.
