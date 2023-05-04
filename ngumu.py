Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
pswd1=input("Please enter a password: ")
Please enter a password: TALGUGUPHOEBE
pswd2=input("Please enter a password: ")
Please enter a password: talguguphoebe
if pswd1==pswd2:
    print("Thankyou")
elif pswd1.lower()==pswd2.lower():
    print("They must be in the same case!")
else:
    print("Incorrect!")

    
They must be in the same case!


word=input("Please enter a word: ")
Please enter a word: phobeasiyo kimpembe
length=len(word)
num=1
for x in word:
    position=length - word
    letter=word[position]
    print(letter)
    num=num+1

    
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    position=length - word
TypeError: unsupported operand type(s) for -: 'int' and 'str'
wordd=input("Please enter a word: ")
Please enter a word: Kibowen Phoebe
length=len(wordd)
print(length)
14
num=1
for x in wordd:
    position=length - wordd
    letter=wordd[position]
    print(letter)
    num=num+1

    
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    position=length - wordd
TypeError: unsupported operand type(s) for -: 'int' and 'str'
