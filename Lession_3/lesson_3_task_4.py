from turtle import *

screen = Screen()
screen.setup(800, 600)

t = Turtle()
t.speed(0.75)  

def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

draw_circle("light blue", 80, 0, -20)

draw_circle("white", 48, 0, -50)

draw_circle("light blue", 60, 0, 100)

t.color("light blue")

t.begin_fill()

t.penup()
t.goto(-50, -20)  
t.pendown()

radius_x = 100
radius_y = 50

t.left(70)  
t.circle(radius_x, 90)  
t.left(90)  
t.circle(radius_y, 90)  

t.end_fill()

t.color("light blue")

t.begin_fill()

t.penup()
t.goto(10, 0) 
t.pendown()

radius_x = 100
radius_y = 50

t.left(20)  
t.circle(radius_x, 90)  
t.left(90)  
t.circle(radius_y, 90)  

t.end_fill()

draw_circle("black", 5, -25, 120)
draw_circle("black", 5, 25, 120)

t.penup()
t.goto(0, 100)
t.pendown()
t.color("orange")
t.begin_fill()
t.goto(10, 90)
t.goto(-10, 90)
t.goto(0, 100)
t.end_fill()

t.hideturtle()

screen.mainloop()