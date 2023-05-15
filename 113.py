Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
file=open("Books.csv","w")
num=int(input("Please enter the number of entries that you want to add: "))
Please enter the number of entries that you want to add: 4
for i in range(0,num):
    title=input("Please enter the title of the book: ")
    author=input("Please enter the name of the author: ")
    year=input("Please enter the year the book was released: ")

    
Please enter the title of the book: Chesawil nebo Kimoso
Please enter the name of the author: Darfur Katikibeu
Please enter the year the book was released: 1989
Please enter the title of the book: The Origin of Bokoria
Please enter the name of the author: Charles Boruett
Please enter the year the book was released: 1889
Please enter the title of the book: Fifty Shades of Grey
Please enter the name of the author: Annaconda Kingfisher
Please enter the year the book was released: 1902
Please enter the title of the book: My Life in Crime
Please enter the name of the author: John Kiriamiti
Please enter the year the book was released: 1999
newrecord=title + "," + author + "," + year + "\n"
file.write(str(newrecord))
37
file.close()
search=input("Please enter a name of the author in the above books: ")
Please enter a name of the author in the above books: Kiriamiti
file=open("Books.csv","r")
count=0
for row in file:
    if search in str(row):
        print(row)
        count=count+1
        if count==0:
            print("Entry not found.")
            file.close()

            
My Life in Crime,John Kiriamiti,1999

