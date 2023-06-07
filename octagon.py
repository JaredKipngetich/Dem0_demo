Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
import random
turtle.pensize(3)
for i in range(0,8):
    turtle.color(random.choice(["blue","black","orange","yellow","green","pink"]))
    turtle.forward(50)
    turtle.right(45)

    
