Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
file=open("Names.txt","r")
print(file.read())
Kiptogom
 Kimngochoch
Chemelil
Cheplambus
Cheplogoi
Chepelion

file=open("Names.txt","r")
selectedname=input("Please enter a name: ")
Please enter a name: Cheplogoi
selectedname=selectedname+"\n"
for row in file:
    if row!=selectedname:
        file=open("Names2.txt","a")
        newrecord=row
        file.write(newrecord)
        file.close()
    file.close()

    
9
13
9
11
10
