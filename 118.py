Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def ask_value():
    num=int(input("Please enter a number: "))
    return(num)

def count(num):
    n = 1
    while n <=num:
        print(n)
        n = n + 1

        
def main():
    num=ask_value()
    count(num)

    
main()
Please enter a number: 7
1
2
3
4
5
6
7
