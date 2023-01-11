from turtle import Turtle, Screen
import random

def draw_shape(drawline, step):
    drawline.right(step)
    drawline.circle(100)
    
def line_setting(drawline):
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    drawline.color((red, green, blue))

def main():
    drawline = Turtle()
    screen = Screen()
    screen.colormode(255)
    #drawline.pensize(15)
    drawline.speed("fast")
    step = 10
    
    for n in range(int(360/step)):
        line_setting(drawline)
        draw_shape(drawline, step)

    screen.exitonclick()
    
main()