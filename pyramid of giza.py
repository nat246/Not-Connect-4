from random import *
from math import *
from turtle import *

#Create board
setup(100, 100)
title('Pyramid of Giza token')
tracer(True)
speed('fastest')

#Draw night sky background
penup()
goto(-50, -50)
pendown()
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
penup()

#Draw stars
star_coord = []
color('white')
    #Create x and y positions for star placements
for i in range(50):
    star_coord.append([randint(-50, 50), randint(0, 50)])
print(star_coord)
    #Place star placements in token
for x_coord, y_coord in star_coord:
    goto(x_coord, y_coord)
    dot(3)
    
#Draw moon
goto(-50, 20)
pendown()
color('light gray')
begin_fill()
circle(30, extent = 90)
for i in range(2):
    left(90)
    forward(30)
end_fill()
    #Draw moon outline 
setheading(0)
color('dim gray')
width(2)
circle(30, extent=90)
penup()

#Draw ground
color('burlywood')
setheading(0)
goto(-50, -20)
pendown()
begin_fill()
for i in range(2):
    forward(100)
    right(90)
    forward(30)
    right(90)
end_fill()
penup()

#Define a function to draw a pyramid
def pyramid(x_pos, y_pos, scale):
    #Pyramid Values/constants/variables
    pyramid_color = 'peru'
    pyramid_outline = 'saddle brown'
    pyramid_length = 50 * scale
    pyramid_depth = pyramid_length/5
        #Use pythagoras to find height of pyramid (b^2 = c^2 - a^2)
    pyramid_height = sqrt(pyramid_length**2 -(pyramid_length/2)**2)
        #Find the apex point of the pyramid
    pyramid_x_tip = (((pyramid_length + x_pos) + x_pos)/2)
    pyramid_y_tip = pyramid_height + y_pos
    pyramid_apex = [pyramid_x_tip, pyramid_y_tip]
    print(pyramid_height)
    #Draw pyramid shape
    setheading(0)
    goto(x_pos, y_pos)
    color(pyramid_color)
    pendown()
    begin_fill()
    for i in range(3):
        forward(pyramid_length)
        left(120)
    setheading(135)
    forward(pyramid_depth)
    goto(pyramid_apex)
    end_fill()
        #Draw pyramid outline
    setheading(0)
    width(2)
    color(pyramid_outline)
    goto(x_pos, y_pos)
    pendown()
    for i in range(3):
        forward(pyramid_length)
        left(120)
    setheading(135)
    forward(pyramid_depth)
    goto(pyramid_apex)
    penup()
    pass

#Draw Pyramid of Khufu
pyramid(15, -35, 0.7)
#Draw Pyramid of Khafre
pyramid(-20, -40, 1)
#Draw Pyramid of Menkaure
pyramid(-40, -42, 0.7)

#Exit
hideturtle()
done()
