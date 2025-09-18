# rainbow.py

from turtle import *
speed(0)

num = int(input("How many squares do you want? "))

for i in range(num):
    if i%7 == 0:
        color("red")
    elif i%7 == 1:
        color("orange")
    elif i%7 == 2:
        color("yellow")
    elif i%7 == 3:
        color("green")
    elif i%7 == 4:
        color("blue")
    elif i%7 == 5:
        color("purple")
    else:
        color("violet")

    begin_fill()
    for j in range(4):
        forward(100)
        right(90)
    end_fill()
    penup()
    right(45)
    forward(10)
    left(45)
    pendown()

input()