from turtle import Turtle, Screen
import random

polygon = Turtle()
screen = Screen()
polygon.shape("classic")
start_size = 100
screen.colormode(255)

for n in range(3, 11):
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    for side in range(n):
        polygon.pencolor((red, green, blue))
        polygon.forward(start_size)
        polygon.right(360/n)    

screen.exitonclick()