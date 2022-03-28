from random import *
from turtle import *
from math import *

#Create board
setup(100, 100)
title('Taipei 101')
tracer(True)
speed('fastest')

#Draw background
goto(-50, 0)
color('dark slate blue')
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()

#Draw buildings background
#Create random coordinates for buldings
buildings_coord = []
for i in range(100):
    buildings_coord.append([randint(-50, 42), randint(0, 20)])
#Create randome coordinates for lights
lights_coord = []
for i in range(100):
    lights_coord.append([randint(-45, 45), randint(5, 35)])
#Draw building function
def buildings(size):
    color('grey')
    setheading(90)
    pendown()
    for i in range(2):
        forward(size)
        right(90)
        forward(size/4)
        right(90)
    penup()
#Draws buildings
for x_coord, y_coord in buildings_coord:
    goto(x_coord, y_coord)
    buildings(randint(15, 30))
#Draws lights
for x_coord, y_coord in lights_coord:
    color('yellow')
    goto(x_coord, y_coord)
    dot(3)
penup()

#Draw moon
color('white')
goto(-20, 75)
pendown()
begin_fill()
circle(10)
end_fill()
penup()

#Draw border
setheading(0)
goto(-50, 0)
width(2)
color('blue')
pendown()
for i in range(4):
    forward(100)
    left(90)
penup() 

#Draw Tower
#Make a function that creates a trapezium as there are many trapeziums to be drawn
def trapez(length_a, length_b, height):
    # Find adjacent length
    adjacent_length = (length_a - length_b) / 2
    #Create top and bottom lines
    begin_fill()
    pendown()
    forward(length_b)
    left(90)
    penup()
    forward(height)
    top_right = pos()
    left(90)
    pendown()
    forward(length_b)
    top_left = pos()
    penup()

    #Complete left side
    left(90)
    forward(height)
    right(90)
    pendown()
    forward(adjacent_length)
    goto(top_left)
    penup()

    #Complete right side
    goto(top_right)
    left(90)
    forward(height)
    left(90)
    pendown()
    forward(adjacent_length)
    goto(top_right)
    penup()
    end_fill()

#Draw base
length_a = 30
length_b = 15
height = 15
color('royal blue')
goto(-length_b/2, 1)
pendown()
trapez(length_a, length_b, height)
goto(-length_b/2, 5)
setheading(0)
begin_fill()
for i in range(4):
    forward(height)
    left(90)
end_fill()
penup()
left(90)
forward(height)
right(90)
forward(length_b)
#Draw next 8 levels
length_a = 20
length_b = 15
height = 7.5
for i in range(8):
    setheading(90)
    forward(height)
    setheading(180)
    trapez(length_a, length_b, height)
    right(90)
    forward(height)
    right(90)
    forward(length_b)
penup()

#Draw tip base
setheading(180)
forward(5)
setheading(90)
pendown()
for i in range(4):
    forward(5)
    left(90)
penup()
#Draw tip
forward(5)
left(90)
forward(2.5)
right(90)
width(3)
pendown()
forward(5)
width(1)
forward(10)
#Exit
hideturtle()
done()