from turtle import Turtle,Screen
from random import random
#timmy=Turtle()
#my_screen=Screen()
#
'''timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.right(120)

timmy.backward(100)
timmy.left(120)
#for steps in range(100):
 #   for c in ('blue', 'red', 'green'):
  #      timmy.color(c)
   #     timmy.forward(steps)
    #    timmy.right(30)
timmy.home()
timmy.begin_fill()
#while True:
 #  timmy. forward(200)
  # timmy. left(170)

   #if abs(timmy.pos()) < 1:
     #   break
timmy.end_fill()
timmy.color("DarkOrchid")
#timmy.fillcolor("yellow")

#for i in range(100):
 #   steps = int(random() * 100)
  #  angle = int(random() * 360)
   # timmy.right(angle)
    #timmy.fd(steps)

print(my_screen.canvheight)
my_screen.exitonclick()
'''
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon name",["pikachu","raichu","biduf"])
table.add_column("Type",["electric","electric","normal"])

table.align="l"
print(table.align)
print(table)