from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("classic")
for _ in range(4):
    timmy_the_turtle.right(90)
    for n in range(10):
        if n%2 ==0:
            timmy_the_turtle.pendown()
            timmy_the_turtle.forward(10)
        else:
            timmy_the_turtle.penup()
            timmy_the_turtle.forward(10)

screen = Screen()
screen.exitonclick()