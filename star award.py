from turtle import *

#Create board
setup(100, 100)
title('Star')
tracer(True)
speed('slowest')

#Draw star
penup()
setheading(0)
forward(100)
pendown()
begin_fill()
for i in range(5):
    right(180- 36)
    forward(20)
    left(72)
    forward(20)
end_fill()
#Exit
hideturtle()
done()
