Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
file=open("Star.csv","a")
name=input("Please enter your name: ")
Please enter your name: Nasenya
age=input("Please enter your age: ")
Please enter your age: 89
star=input("Please enter your star: ")
Please enter your star: Libra
newRecord = name+ "," + age + "," + star
file.write(str(newRecord))
16
file.close()
