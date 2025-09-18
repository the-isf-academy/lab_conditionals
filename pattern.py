# pattern.py

from turtle import *

pensize(2)
speed(0)
for i in range(8):
    if i%2 == 0: 
        color("red")
    else:
        color("blue")

    for j in range(4):
        forward(150)
        right(90)

    right
    penup()
    right(45)
    forward(50)
    left(45)
    pendown()

hideturtle()
input()
