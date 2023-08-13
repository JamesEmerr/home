# J Programming
# Drawing with Turtle

import turtle
turtle.shape("turtle")
turtle.color("Blue")
turtle.speed(0)
turtle.width(5)


def rectangle(w, l):
  for j in range(2): 
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
rectangle(100, 50)

turtle.penup()
turtle.left(180)
turtle.forward(150)
turtle.pendown()

def rectangle(w, l):
  for j in range(2): 
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
rectangle(100,50)

turtle.right(180)
turtle.penup()
turtle.forward(250)
turtle.left(90)
turtle.forward(55)
turtle.left(90)
turtle.pendown()

turtle.color("Red")
def triangle(size):
  for j in range(3):
    turtle.forward(size)
    turtle.right(120)
triangle(350)

turtle.penup()
turtle.forward(25)
turtle.left(90)
turtle.forward(60)

turtle.color("green")
turtle.pendown()
def rectangle(w, l):
  for j in range(2): 
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
rectangle(125,50)

turtle.right(90)
turtle.penup()
turtle.forward(250)
turtle.left(90)
turtle.pendown()
def rectangle(w, l):
  for j in range(2): 
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
rectangle(125,50)

turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(30)

turtle.Screen().exitonclick()



