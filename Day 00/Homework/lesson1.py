from turtle import *

width(5)
#body
color("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

penup()
goto(200,200)
pendown()


right(90)
right(45)

#roof
color("green")
begin_fill()
forward(141)
left(90)
forward(141)
end_fill()
color("red")
left(45)
forward(200)
left(90)
forward(80)

#door
color("brown")
begin_fill()
left(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()

penup()
goto(20,180)
pendown()


#window 1
color("orange")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(180,180)
pendown()

#WINDOW 2
color("orange")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()

