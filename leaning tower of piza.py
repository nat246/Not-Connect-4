from random import *
from turtle import *

#Create board
setup(100, 100)
title('Leaning Tower of Pisa')
tracer(True)
speed('slowest')
penup()

#Draw day time background
goto(-50, 0)
color('sky blue')
pendown()
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
penup()

#Draw Sun
setheading(0)
goto(-50, 70)
pendown()
width(2)
color('goldenrod')
fillcolor('gold')
begin_fill()
circle(30, extent = 90)
for i in range(2):
    left(90)
    forward(30)
end_fill()
penup()

#Draw ground
setheading(0)
goto(-50, 0)
color('forest green')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(30)
    left(90)
end_fill()
penup()

#Draw token border
color('goldenrod')
setheading(0)
goto(-50 , 0)
width(2)
pendown()
for i in range(4):
    forward(100)
    left(90)
penup()

#Draw Tower of Pizza
#Tower constants
tower_tilt = -10
wall_length_ground_level = 20
wall_height_ground_level = 15
wall_length_mid_levels = wall_length_ground_level * 0.84
wall_height_mid_levels = wall_height_ground_level * 0.5
wall_length_top_level = wall_length_mid_levels * 0.84
wall_height_top_level = wall_height_mid_levels
divider_edges = [-2, 180]

#Draw ground floor
width(1)
setheading(90 + tower_tilt)
goto(15, 5)
color('black')
pendown()
fillcolor('white smoke')
begin_fill()
for i in range(2):
    forward(wall_height_ground_level)
    left(90)
    forward(wall_length_ground_level)
    left(90)
penup()
#Draw ground floor divider_edges
forward(wall_height_ground_level)
left(90)
pendown()
for i in range(3):
    forward(wall_length_ground_level)
    circle(divider_edges[0], divider_edges[1])
penup()

#Draw next 5 levels
forward(2)
left(90)
for i in range(5):
    pendown()
    for i in range(3):
        forward(wall_height_mid_levels)
        right(90)
        forward(wall_length_mid_levels)
        right(90)
    right(90)
    penup()
    #Draw floor divider_edgess
    pendown()
    for i in range(2):
        forward(wall_length_mid_levels)
        circle(divider_edges[0], divider_edges[1])
    penup()
    forward(wall_length_mid_levels)
    right(90)
    forward(4)
#Draw top level
right(90)
forward(2)
left(90)
pendown()
for i in range(3):
        forward(wall_height_top_level)
        right(90)
        forward(wall_length_top_level)
        right(90)
right(90)
penup()
    #Draw top floor divider edges
pendown()
for i in range(2):
    forward(wall_length_top_level)
    circle(divider_edges[0], divider_edges[1])
end_fill()
penup()

#Refine ground
setheading(0)
goto(15, 5)
color('forest green')
forward(5)
left(90)
pendown()
begin_fill()
for i in range(2):
    forward(5)
    left(90)
    forward(30)
    left(90)
end_fill()

#Exit
hideturtle()
done()
