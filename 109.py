Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Create a new file.")
Create a new file.
print("Display the new file.")
Display the new file.
print("Add a new item to the file")
Add a new item to the file
selection=int(input("Make a selection 1,2 or 3."))
Make a selection 1,2 or 3.9
if selection ==1:
    subject=input("Please enter a subject: ")
    file=open("Subject.txt","w")
    file.write(subject +"\n")
    file.close()
elif selection==2:
    file=open("Subject.txt","r")
    print(file.read())
elif selection==3:
    file=open("Subject.txt","a")
    file.write(subject+"\n")
    file.close()
    file=open("subject.txt","r")
    print(file.read())
else:
    print("Invalid option")

    
Invalid option
