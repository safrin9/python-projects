from turtle import Turtle,Screen
import turtle as t
tim=Turtle()
tim.shape("turtle")
t.colormode(255)
# for _ in range(4):
#   timmy_the_turtle.forward(100)
#   timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
#
#
#
# for _ in range(15):
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)
#   tim.pendown()
#
#
import random
def random_color():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  return (r,g,b)
colors=["blue","red","yellow","cyan","dark green","pale green","firebrick","orange"]
directions=[0,90,180,270]
# def draw(num_of_sides):
#   angle=360/num_of_sides
#
#   for _ in range(num_of_sides):
#
#     tim.forward(100)
#     tim.right(angle)
# for num_of_sides in range(3,11):
#   tim.color(random.choice(colors))
#   draw(num_of_sides)
# ttim.color(random_color())
#   tim.forward(30)
#   tim.setheading(random.choice(directions))
#
#
# # im.pensize(10)
# tim.speed(6)
# for _ in range(200):
#
tim.speed("fastest")
def s_draw(size):

  for _ in range(int(360/size)):

    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading()+size)
s_draw(10)






screen=Screen()
screen.exitonclick()