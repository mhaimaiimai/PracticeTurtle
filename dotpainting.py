from turtle import Turtle, Screen
import colorgram
import random 


def extract_color(picture):
    colors = colorgram.extract(picture, 30)
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_list.append((r,g,b))
    return color_list

def main(dots):    
    brush = Turtle()
    brush.shape("circle")
    brush.penup()
    brush.color("white")
    screen = Screen()
    screen.colormode(255)
    step = 30
    colors = extract_color("sample_picture.jpg")
    for dot in range(1, dots+1):
        color = random.choice(colors)
        brush.dot(20, color)
        brush.forward(step)
        if dot%10 ==0 and dot>0:
            brush.setheading(270)
            brush.forward(step)
            if dot%20 ==0:
                brush.left(90)
            else:
                brush.right(90)
            brush.forward(step)
                
    screen.exitonclick()
main(100)