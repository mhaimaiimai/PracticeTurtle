from turtle import Turtle, Screen
import random

def draw_shape(drawline):
    direction = random.randrange(0,360,90)
    drawline.setheading(direction)
    drawline.forward(20)
    
def line_setting(drawline):
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    drawline.color((red, green, blue))

def main():
    drawline = Turtle()
    screen = Screen()
    screen.colormode(255)
    drawline.pensize(15)
    drawline.speed("fast")
    
    while True:
        line_setting(drawline)
        draw_shape(drawline)
    
main()