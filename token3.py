from random import *
from turtle import *

#Create board
setup(100, 100)
title('Leaning Tower of Pisa')
tracer(True)
speed('fast')

#Draw background
penup()
setheading(0)
goto(-50, 0)
color('sky blue')
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()

#Draw ground
goto(-50, 0)
setheading(0)
color('sea green')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(20)
    (left(90))
end_fill()
#Draw ground tiles
x = 0
for i in range(5):
    # while i % 2:
    #     color("sea green")
    if i % 2:
        color('sea green')
    else:
        color('light green')
    goto(-50 + x, 0)
    begin_fill()
    pendown()
    goto(0, 20)
    x += 20
    goto(-50 + x, 0)
    end_fill()
    penup()

#Draw border
setheading(0)
goto(-50, 0)
color('dark goldenrod')
width(2)
pendown()
for i in range(4):
    forward(100)
    left(90)
penup()

#Draw Eiffel Tower
#Tower constants
first_divider_coord = [-13.16, 38.79]
second_divider_coord = [-7.28, 58.28]
top_pillar_coord = [-4.28, 63.28]
bottom_leg_length = 20
bottom_leg_angle = 70
mid_leg_length = 15
mid_leg_angle = 75
color('dark goldenrod')
width(1)

#Draw base
#Draw left leg
setheading(0)
goto(-20, 20)
pendown()
forward(5)
left(bottom_leg_angle)
forward(bottom_leg_length)
setheading(180)
forward(5)
goto(-20, 20)
penup()
#Draw right leg
setheading(180)
goto(20, 20)
pendown()
forward(5)
right(bottom_leg_angle)
forward(bottom_leg_length)
setheading(0)
forward(5)
goto(20, 20)
penup()
#Draw Arc
setheading(0)
goto(-20, 20)
forward(5)
left(90)
pendown()
circle(-15, 180)
penup()
#Draw divider
setheading(0)
goto(first_divider_coord)
pendown()
for i in range(2):
    forward(first_divider_coord[0] * -2)
    left(90)
    forward(5)
    left(90)
penup()

#Draw 2nd floor
#Draw left leg
setheading(90)
forward(5)
right(90)
forward(2)
pendown()
forward(5)
left(mid_leg_angle)
forward(mid_leg_length)
setheading(180)
forward(5)
goto(-11.16, 43.79)
penup()
#Draw right leg
setheading(180)
goto(11.16, 43.79)
pendown()
forward(5)
right(mid_leg_angle)
forward(mid_leg_length)
setheading(0)
forward(5)
goto(11.16, 43.79)
penup()
#Draw divider
setheading(0)
goto(second_divider_coord)
pendown()
for i in range(2):
    forward(second_divider_coord[0] * -2)
    left(90)
    forward(5)
    left(90)
penup()

#Draw top pillar
#left side
goto(top_pillar_coord)
pendown()
setheading(80)
forward(15)
setheading(90)
forward(10)
penup()
#Right side
goto(top_pillar_coord[0] * -1, top_pillar_coord[1])
setheading(100)
pendown()
forward(15)
setheading(90)
forward(10)
penup()

#Draw tip
setheading(0)
forward(1)
setheading(180)
pendown()
for i in range(4):
    forward(6)
    right(90)
penup()
forward(3)
right(90)
forward(6)
width(3)
pendown()
forward(4)
penup()

#Exit
hideturtle()
done()