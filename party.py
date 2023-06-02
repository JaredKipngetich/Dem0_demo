Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fruit_tuple=("apple","mango","cherry","strawberry","lemon")
frint(fruit_tuple.index("strawberry"))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    frint(fruit_tuple.index("strawberry"))
NameError: name 'frint' is not defined. Did you mean: 'print'?
print(fruit_tuple.index("stawberry"))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(fruit_tuple.index("stawberry"))
ValueError: tuple.index(x): x not in tuple
fruit_tuple=("mango","Lemon","cherry","strawberry","guava")
print(fruit_tuple.index("strawberry"))
3

print(fruit_tuple[2])
cherry

name_list=["John","Omwenga","Phillip","Jones","Jordan"]
del names_list[1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del names_list[1]
NameError: name 'names_list' is not defined. Did you mean: 'name_list'?
del name_list[1]
print(name_list)
['John', 'Phillip', 'Jones', 'Jordan']
name_list.append(input("Please add a name"))
Please add a name Jared
print(name_list)
['John', 'Phillip', 'Jones', 'Jordan', ' Jared']
name_list.sort()
print(name_list)
[' Jared', 'John', 'Jones', 'Jordan', 'Phillip']
print(sorted(name_list))
[' Jared', 'John', 'Jones', 'Jordan', 'Phillip']

colors={1:"Yellow",2:"Blue",3:"Orange",4:"Green"}
color[2]="Violet"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    color[2]="Violet"
NameError: name 'color' is not defined. Did you mean: 'colors'?
colors[2]="Yellow"
print(colors)
{1: 'Yellow', 2: 'Yellow', 3: 'Orange', 4: 'Green'}
colors[2]="Violet"
print(colors)
{1: 'Yellow', 2: 'Violet', 3: 'Orange', 4: 'Green'}
colors[0]="indigo"
print(colors)
{1: 'Yellow', 2: 'Violet', 3: 'Orange', 4: 'Green', 0: 'indigo'}

x=[123,678,987,24091996,2350,967,543]
print(len(x))
7
print(x[1:4])
[678, 987, 24091996]
for i in x:
    print(i)

    
123
678
987
24091996
2350
967
543
num=int(input("Please enter a number"))
Please enter a number90
if num in x:
    print(num,"is in the list")
    else:
        
SyntaxError: invalid syntax
num=int(input("Please enter a number: "))
Please enter a number: 90
if num in x:
    print(num," is in the list. ")
    else:
        
SyntaxError: invalid syntax
num=int(input("Please enter a number : "))
Please enter a number : 98
if num in x:
    print(num, "is in the list ")
else:
    print(num," is not in the list. ")

    
98  is not in the list. 
x.insert(2,420)
print(x)
[123, 678, 420, 987, 24091996, 2350, 967, 543]
x.remove(24091996)
print(x)
[123, 678, 420, 987, 2350, 967, 543]

countries_tuple=("Kenya","Morocco","Senegal","Ghana","Angola")
country=input("Please enter a country in the list: ")
Please enter a country in the list: Ghana
print(countries_tuple.index(country))
3
state=input("Please enter a country in the list: ")
Please enter a country in the list: Angola
print(countries_tuple.index(state))
4
num=int(input("Please enter a number : "))
Please enter a number : 3
print(countries_tuple[num])
Ghana
numb=int(input("Please enter a position: "))
Please enter a position: 2
print(countries_tuple[numb])
Senegal


sports=["Rugby","Soccer","Athletics"]
fav=input("Please enter your favourite sport : ")
Please enter your favourite sport : Tennis
sports.append(fav)
print(sports)
['Rugby', 'Soccer', 'Athletics', 'Tennis']
sports.sort()
print(sports)
['Athletics', 'Rugby', 'Soccer', 'Tennis']
sports=["Golf","Cricket","Athletics"]
sports.append("Add a sport")
sports.append("Add a sport")
print(sports)
['Golf', 'Cricket', 'Athletics', 'Add a sport', 'Add a sport']
sports.insert(3,"Javelin")
sports.insert(2,"Formula ")
sports.sort()
print(sports)
['Add a sport', 'Add a sport', 'Athletics', 'Cricket', 'Formula ', 'Golf', 'Javelin']
sports.remove("Add a sport")
print(sports)
['Add a sport', 'Athletics', 'Cricket', 'Formula ', 'Golf', 'Javelin']
sports.remove("Add a sport")
print(sports)
['Athletics', 'Cricket', 'Formula ', 'Golf', 'Javelin']
sports.append("Kilimanjaro")
print(sports)
['Athletics', 'Cricket', 'Formula ', 'Golf', 'Javelin', 'Kilimanjaro']
subjects=["English","Structures","Calculus","Materials","Philosophy","Matrices"]
sub=input("What subject do you like the least ? ")
What subject do you like the least ? English
subjects.remove(sub)
subjects.sort()
print(subjects)
['Calculus', 'Materials', 'Matrices', 'Philosophy', 'Structures']
foods={1:"Matoke",2:"Pilau",3:"Githeri",4:"Tunbukiza"}
print(foods)
{1: 'Matoke', 2: 'Pilau', 3: 'Githeri', 4: 'Tunbukiza'}
fud=input("What food do you like the least ? ")
What food do you like the least ? Githeri
del foods[3]
foods.sort()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    foods.sort()
AttributeError: 'dict' object has no attribute 'sort'
del food[fud]
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    del food[fud]
NameError: name 'food' is not defined. Did you mean: 'foods'?
del foods[fud]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    del foods[fud]
KeyError: 'Githeri'
foods={1:"Githeri",2:"Matoke",3:"Tumbukiza",4:"Matumbo"}
fud=input("Which of the foods do you like the least ? ")
Which of the foods do you like the least ? Matumbo
del foods[fud]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    del foods[fud]
KeyError: 'Matumbo'
del foods[2]
print(foods)
{1: 'Githeri', 3: 'Tumbukiza', 4: 'Matumbo'}
del foods[3]
sort.foods()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    sort.foods()
NameError: name 'sort' is not defined. Did you mean: 'sports'?
foods.sort()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    foods.sort()
AttributeError: 'dict' object has no attribute 'sort'
colors=["Orange","Black","Green","Blue","Yellow","Brown","Indigo","Violet","Grey","Purple","Maroon"]
start=int(input("Please enter a start number between 0 and 4 : "))
Please enter a start number between 0 and 4 : 0
end=int(input("Please enter a end number between 5 and 9: "))
Please enter a end number between 5 and 9: 0
for i in range(start,end):
    print(i)

    
print(colors[start:end])
[]



colors=["Red","Maroon","Grey","Blue","White","Indigo","Pink","Purple","Black","Brown"]
start=int(input("Please enter a starting number between 0 and 4: "))
Please enter a starting number between 0 and 4: 0
end=int(input("Please enter an ending number between 5 and 9: "))
Please enter an ending number between 5 and 9: 9
print(colors[start:end])
['Red', 'Maroon', 'Grey', 'Blue', 'White', 'Indigo', 'Pink', 'Purple', 'Black']
numbers=[234,786,907,398]
for i in numbers:
    print(i)

    
234
786
907
398
num=int(input("Please enter a number : "))
Please enter a number : 234
if num in numbers:
    print("The number is in position",numbers.index(num))
else:
    print(num," Is not in the list ")

    
The number is in position 0
for i in range(0,4):
    Friends=input("Whom do you want invited to the party ? ")

    
Whom do you want invited to the party ? Ken
Whom do you want invited to the party ? Tim
Whom do you want invited to the party ? Bob
Whom do you want invited to the party ? Jacob
party=[friends]
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    party=[friends]
NameError: name 'friends' is not defined. Did you mean: 'Friends'?
name1=input("Whom do you want invited ? ")
Whom do you want invited ? Jacob
name2=input("Whom do you want invited ? ")
Whom do you want invited ? Henry
name3=input("Whom do you want invited? ")
Whom do you want invited? Tom
party=[name1,name2,name3]
print(party)
['Jacob', 'Henry', 'Tom']
party.append(input("Please add another another guest : "))
Please add another another guest : Jerry
print(party)
['Jacob', 'Henry', 'Tom', 'Jerry']
more=input("Do you wish to add more people to the list of invited guests y/n ? :")
Do you wish to add more people to the list of invited guests y/n ? :y
if more == "y":
    name=party.append(input("Please enter the name of the guest: "))
else:
    print("You have",len(party)," people coming to your party" )

    
Please enter the name of the guest: Twiri











name1=input("Please enter a name of one you want invited to the party: ")
Please enter a name of one you want invited to the party: Jared
name2=input("Please enter a name of another one one you want invited to the party : ")
Please enter a name of another one one you want invited to the party : Jerry
name3=input("Please enter the name of another person you want invited to the party: ")
Please enter the name of another person you want invited to the party: Collins
party=[name1,name2,name3]
print(party)
['Jared', 'Jerry', 'Collins']
more=input("Do you wish to invite more people to the party? : y/n ")
Do you wish to invite more people to the party? : y/n y
while more =="y":
    newname=party.append(input("Please enter another name: "))
    more=input("Do you wish to invite more people to the party ? ")
    print("You have ",len(party),"People coming to the party")

    
Please enter another name: Hamisi
Do you wish to invite more people to the party ? y
You have  4 People coming to the party
Please enter another name: Barry
Do you wish to invite more people to the party ? Opiyo
You have  5 People coming to the party
