
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10792864
#    Student name: Paul Nathanael Ang
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  NOT CONNECT-4
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "play_game".  You are required to
#  complete this function so that when the program is run it fills
#  a grid with various rectangular tokens, using data stored in a
#  list to determine which tokens to place and where.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *

# Define constant values for setting up the drawing canvas
cell_size = 100 # pixels (default is 100)
num_columns = 7 # cells (default is 7)
num_rows = 6 # cells (default is 6)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the board
y_margin = cell_size // 2 # pixels, the size of the margin below/above the board
canvas_height = num_rows * cell_size + y_margin * 2
canvas_width = num_columns * cell_size + x_margin * 2

# Validity checks on board size
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert num_columns >= 7, 'Board must be at least 7 columns wide'
assert num_rows >= 6, 'Board must be at least 6 rows high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(mark_legend_spaces = True, # show text for legend
                          mark_axes = True, # show labels on axes
                          bg_colour = 'light grey', # background colour
                          line_colour = 'slate grey'): # line colour for board
    
    # Set up the drawing canvas with enough space for the board and
    # legend
    setup(canvas_width, canvas_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the board
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the board
    left_edge = -(num_columns * cell_size) // 2 
    bottom_edge = -(num_rows * cell_size) // 2

    # Draw the horizontal grid lines
    setheading(0) # face east
    for line_no in range(0, num_rows + 1):
        penup()
        goto(left_edge, bottom_edge + line_no * cell_size)
        pendown()
        forward(num_columns * cell_size)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for line_no in range(0, num_columns + 1):
        penup()
        goto(left_edge + line_no * cell_size, bottom_edge)
        pendown()
        forward(num_rows * cell_size)

    # Mark the centre of the board (coordinate [0, 0])
    penup()
    home()
    dot(10)

    # Optionally label the axes
    if mark_axes:

        # Define the font and position for the labels
        small_font = ('Arial', (18 * cell_size) // 100, 'normal')
        y_offset = (27 * cell_size) // 100 # pixels

        # Draw each of the labels on the x axis
        penup()
        for x_label in range(0, num_columns):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('a')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, num_rows):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

    # Optionally mark the spaces for drawing the legend
    if mark_legend_spaces:
        # Font for marking the legend's position
        big_font = ('Arial', (24 * cell_size) // 100, 'normal')
        # Left side
        goto(-(num_columns * cell_size) // 2 - 50, -25)
        write('Put your token\ndescriptions here', align = 'right', font = big_font)    
        # Right side
        goto((num_columns * cell_size) // 2 + 50, -25)
        write('Put your token\ndescriptions here', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the "play_game" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_game" function appearing below.
# Your program must work correctly for any data set that can be
# generated by the "random_game" function.
#
# Each of the data sets is a list of instructions, each specifying
# in which column to drop a particular type of game token.  The
# general form of each instruction is
#
#     [column, token_type]
#
# where the columns range from 'a' to 'g' and the token types
# range from 1 to 4.
#
# Note that the fixed patterns below all assume the board has its
# default dimensions of 7x6 cells.
#

# The following data sets each draw just one token type once
fixed_game_a0 = [['a', 1], ['a', 1], ['a', 1]]
fixed_game_a1 = [['b', 2]]
fixed_game_a2 = [['c', 3]]
fixed_game_a3 = [['d', 4]]

# The following data sets each draw just one type
# of token multiple times
fixed_game_a4 = [['c', 1], ['f', 1], ['g', 1], ['c', 1]] 
fixed_game_a5 = [['d', 2], ['d', 2], ['a', 2], ['c', 2]] 
fixed_game_a6 = [['c', 3], ['f', 3], ['g', 3], ['c', 3]] 
fixed_game_a7 = [['f', 4], ['f', 4], ['c', 4], ['c', 4]]

# The following small data sets each draw all four kinds
# of token
fixed_game_a8 = [['e', 3], ['e', 4], ['f', 3], ['e', 1],
                 ['c', 2], ['g', 4]]
fixed_game_a9 = [['g', 3], ['d', 4], ['b', 3], ['e', 1],
                 ['f', 2], ['g', 4], ['c', 2], ['g', 4]]
fixed_game_a10 = [['f', 3], ['d', 1], ['c', 3], ['c', 4],
                  ['e', 2], ['b', 1], ['b', 3]]
fixed_game_a11 = [['e', 3], ['c', 3], ['d', 3], ['c', 2],
                  ['c', 3], ['d', 4], ['a', 4], ['f', 1]]
fixed_game_a12 = [['f', 1], ['b', 4], ['f', 1], ['f', 4],
                  ['e', 2], ['a', 3], ['c', 3], ['b', 2],
                  ['a', 2]]
fixed_game_a13 = [['b', 3], ['f', 4], ['d', 4], ['b', 1],
                  ['b', 4], ['f', 4], ['b', 2], ['c', 4],
                  ['d', 3], ['a', 1], ['g', 3]]
fixed_game_a14 = [['c', 1], ['c', 4], ['g', 2], ['d', 4],
                  ['d', 1], ['f', 3], ['f', 4], ['f', 1],
                  ['g', 2], ['c', 2]]
fixed_game_a15 = [['d', 3], ['d', 4], ['a', 1], ['c', 2],
                 ['g', 3], ['d', 3], ['g', 1], ['a', 2],
                 ['a', 2], ['f', 4], ['a', 3], ['c', 2]]

# The following large data sets are each a typical game
# as generated by the "play_game" function.  (They are
# divided into five groups whose significance will be
# revealed in Part B of the assignment.)
fixed_game_b0_0 = [['d', 4], ['e', 1], ['f', 1], ['d', 1],
                   ['e', 2], ['c', 3], ['a', 2], ['e', 4],
                   ['g', 1], ['d', 4], ['a', 2], ['f', 2]]
fixed_game_b0_1 = [['f', 3], ['a', 2], ['d', 2], ['f', 4],
                   ['b', 2], ['a', 2], ['f', 3], ['f', 3],
                   ['e', 1], ['b', 2], ['e', 1], ['c', 1],
                   ['a', 3], ['d', 3], ['f', 1], ['f', 4],
                   ['b', 4], ['b', 1], ['c', 4], ['d', 1],
                   ['a', 3], ['e', 1], ['b', 2], ['c', 3],
                   ['d', 3], ['c', 2], ['c', 1], ['a', 2],
                   ['d', 4], ['b', 4], ['g', 2]]
fixed_game_b0_2 = [['d', 3], ['d', 4], ['a', 4], ['g', 3],
                   ['d', 2], ['g', 2], ['f', 1], ['b', 2],
                   ['a', 1], ['a', 3], ['a', 4], ['c', 3],
                   ['f', 3], ['b', 2], ['c', 3], ['a', 4],
                   ['g', 1]]

fixed_game_b1_0 = [['e', 3], ['a', 4], ['c', 2], ['f', 1],
                   ['a', 1], ['c', 4], ['g', 3], ['d', 1],
                   ['f', 3], ['d', 1], ['f', 1], ['g', 1],
                   ['e', 3], ['f', 3], ['f', 3], ['e', 4],
                   ['b', 2], ['a', 2], ['g', 1], ['d', 1],
                   ['a', 1], ['a', 1]]
fixed_game_b1_1 = [['f', 3], ['g', 1], ['g', 2], ['b', 1],
                   ['c', 2], ['c', 2], ['f', 3], ['g', 3],
                   ['b', 4], ['g', 4], ['d', 4], ['b', 1],
                   ['e', 3], ['e', 3], ['a', 2], ['c', 1],
                   ['f', 4], ['f', 3], ['e', 3], ['a', 2],
                   ['f', 4], ['g', 1], ['f', 4], ['a', 1]]
fixed_game_b1_2 = [['d', 2], ['f', 1], ['f', 1], ['c', 1],
                   ['c', 4], ['c', 4], ['d', 1], ['d', 4],
                   ['b', 2], ['d', 4], ['b', 1], ['d', 3],
                   ['d', 1], ['a', 1], ['f', 2], ['c', 2],
                   ['c', 4], ['c', 1], ['g', 1], ['g', 1],
                   ['g', 4], ['g', 2], ['a', 1], ['g', 1],
                   ['f', 2], ['e', 4], ['b', 1], ['e', 3],
                   ['b', 4], ['a', 4], ['b', 1], ['a', 4],
                   ['f', 2], ['g', 2], ['a', 1], ['f', 4],
                   ['e', 1], ['b', 4], ['a', 4], ['e', 2],
                   ['e', 3], ['e', 1]]

fixed_game_b2_0 = [['g', 2], ['d', 2], ['f', 2], ['f', 2],
                   ['b', 2], ['e', 1], ['d', 1], ['d', 3],
                   ['e', 1], ['e', 1], ['b', 1], ['b', 1],
                   ['d', 3], ['f', 3], ['d', 3]]
fixed_game_b2_1 = [['c', 2], ['g', 3], ['e', 4], ['g', 2],
                   ['a', 2], ['f', 2], ['f', 2], ['c', 1],
                   ['d', 2], ['b', 3], ['f', 2], ['d', 4],
                   ['b', 4], ['e', 2], ['g', 3], ['b', 4],
                   ['a', 1], ['g', 3], ['f', 1], ['e', 4],
                   ['d', 3], ['a', 1], ['a', 1], ['d', 2],
                   ['g', 3], ['d', 2], ['c', 4], ['f', 2],
                   ['g', 1], ['e', 4], ['f', 3], ['e', 3],
                   ['e', 3], ['b', 1], ['d', 2], ['c', 1],
                   ['c', 3]]
fixed_game_b2_2 = [['e', 2], ['b', 2], ['e', 2], ['g', 2],
                   ['f', 3], ['e', 3], ['e', 2], ['g', 2],
                   ['d', 2], ['e', 2], ['a', 1], ['c', 2],
                   ['e', 2], ['a', 3], ['f', 1], ['a', 3],
                   ['d', 2], ['g', 3], ['b', 4], ['b', 2],
                   ['f', 2], ['g', 4], ['d', 3], ['f', 1],
                   ['d', 3], ['a', 1], ['a', 4], ['g', 1],
                   ['f', 3], ['b', 3], ['c', 4], ['a', 3],
                   ['g', 2], ['c', 1], ['f', 3], ['b', 2],
                   ['b', 4], ['c', 3], ['d', 4], ['c', 4],
                   ['d', 1], ['c', 1]]

fixed_game_b3_0 = [['b', 2], ['d', 4], ['g', 2], ['e', 3],
                   ['d', 3], ['f', 4], ['g', 3], ['a', 3],
                   ['g', 2], ['d', 4], ['g', 4], ['f', 4],
                   ['a', 4], ['a', 4], ['f', 2], ['b', 1]]
fixed_game_b3_1 = [['d', 2], ['b', 2], ['e', 4], ['e', 3],
                   ['d', 3], ['c', 2], ['e', 3], ['b', 4],
                   ['b', 4], ['d', 4], ['f', 1], ['c', 2],
                   ['a', 1], ['e', 3], ['b', 4], ['f', 3],
                   ['c', 3], ['b', 3], ['c', 2], ['b', 2],
                   ['d', 3], ['e', 4], ['f', 2], ['g', 3],
                   ['g', 4], ['e', 2], ['c', 1], ['d', 3],
                   ['d', 1], ['f', 3], ['g', 3], ['f', 3],
                   ['c', 3], ['g', 4], ['g', 3], ['g', 3]]
fixed_game_b3_2 = [['a', 2], ['c', 1], ['f', 2], ['d', 2],
                   ['a', 3], ['c', 2], ['b', 3], ['e', 3],
                   ['e', 3], ['f', 4], ['a', 1], ['a', 2],
                   ['b', 1], ['c', 3], ['a', 2], ['c', 2],
                   ['g', 3], ['g', 3], ['d', 3], ['b', 2],
                   ['c', 4], ['g', 3], ['f', 3], ['a', 3],
                   ['f', 2], ['f', 1], ['d', 4], ['d', 4],
                   ['g', 2], ['e', 3], ['e', 4], ['f', 3],
                   ['d', 3], ['e', 4], ['g', 4], ['c', 3],
                   ['d', 1], ['e', 2], ['b', 2], ['b', 1],
                   ['g', 1]]

fixed_game_b4_0 = [['g', 3], ['f', 3], ['e', 4], ['a', 4],
                   ['a', 4], ['c', 4], ['e', 3], ['e', 4],
                   ['a', 4], ['a', 2], ['a', 2], ['c', 4],
                   ['f', 4], ['d', 4], ['c', 4], ['f', 3],
                   ['e', 1], ['b', 2], ['c', 2], ['a', 3],
                   ['g', 4], ['d', 3], ['f', 1], ['f', 2],
                   ['e', 2], ['d', 1], ['c', 4]]
fixed_game_b4_1 = [['a', 3], ['d', 4], ['g', 4], ['b', 3],
                   ['e', 1], ['b', 4], ['e', 3], ['f', 1],
                   ['f', 4], ['b', 4], ['d', 2], ['e', 4],
                   ['g', 4], ['d', 2], ['c', 3], ['b', 2],
                   ['f', 4], ['d', 2], ['b', 2], ['e', 4],
                   ['c', 3], ['d', 2], ['a', 1], ['e', 1],
                   ['d', 2], ['g', 1], ['g', 3]]
fixed_game_b4_2 = [['c', 1], ['c', 4], ['d', 1], ['c', 2],
                   ['d', 3], ['d', 4], ['g', 3], ['e', 1],
                   ['g', 4], ['c', 3], ['f', 1], ['b', 4],
                   ['a', 3], ['c', 4], ['e', 2], ['e', 3],
                   ['b', 3], ['d', 1], ['c', 3], ['f', 4],
                   ['e', 1], ['g', 4], ['b', 4], ['g', 3],
                   ['b', 4], ['b', 3], ['b', 3], ['g', 3],
                   ['e', 3], ['f', 1], ['e', 1], ['a', 1],
                   ['a', 4], ['a', 1], ['f', 4], ['f', 2],
                   ['f', 3], ['d', 1], ['d', 3], ['a', 3],
                   ['a', 1], ['g', 2]]

# If you want to create your own test data sets put them here,
# otherwise call function random_game to obtain data sets.
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.

# The following function creates a random data set describing a
# game to draw.  Your program must work for any data set that
# can be returned by this function.  The results returned by calling
# this function will be used as the argument to your "play_game"
# function during marking.  For convenience during code development
# and marking this function also prints each move in the game to the
# shell window.  NB: Your code should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
# To maximise the amount of "randomness" the function makes no attempt
# to give each of the four "players" the same number of turns.  (We
# assume some other random mechanism, such as rolling a die, determines
# who gets to drop a token into the board at each turn.)  However the
# function has been designed so that it will never attempt to overfill
# a column of the board.  Also, the function will not necessarily
# generate enough moves to fill every cell in the board.
#
def random_game():
    # Welcoming message
    print('Welcome to the game!')
    print('Here are the randomly-generated moves:')
    # Initialise the list of moves
    game = []
    # Keep track of free spaces
    vacant = [["I'm free!"] * num_rows] * num_columns
    # Decide how many tokens to insert
    num_tokens = randint(0, num_rows * num_columns * 1.5)
    # Drop random tokens into the board, provided they won't
    # overfill a column
    for move in range(num_tokens):
        # Choose a random column and token type
        column_num = randint(0, num_columns - 1)
        column = chr(column_num + ord('a'))
        token = randint(1, 4)
        # Add the move, provided it won't overfill the board
        if vacant[column_num] != []:
            # Display the move
            print([column, token])
            # Remember it
            game.append([column, token])
            vacant[column_num] = vacant[column_num][1:]
    # Print a final message and return the completed game
    print('Game over!')
    if len(game) == 0:
        print('Zero moves were generated')
    elif len(game) == 1:
        print('Only one move was generated')
    else:
        print('There were', len(game), 'moves generated')
    return game

#
#--------------------------------------------------------------------#


#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "play_game" function.
#

#Token placements ------------------------------------------------------------------
#Row Counter
row_counter = [0, 0, 0, 0, 0, 0, 0]

#Function that places token to the righ column and row
def place_token_to(column):
    #Base row
    base_row = cell_size * -3

    #Dictionary that finds the column coordinate that the token will be placed on 
    # and idendtifies the row counter that will be used to update row_coutner list
    drop_to = {
        'a' : {
            'column_coord' : [cell_size * -3],
            'row_counter_identifier' : 0,
        },
        'b' : {
            'column_coord' : [cell_size * -2],
            'row_counter_identifier' : 1,
        },
        'c' : {
            'column_coord' : [cell_size * -1],
            'row_counter_identifier' : 2,
        },
        'd' : {
            'column_coord' : [cell_size * 0],
            'row_counter_identifier' : 3,
        },
        'e' : {
            'column_coord' : [cell_size * 1],
            'row_counter_identifier' : 4,
        },
        'f' : {
            'column_coord' : [cell_size * 2],
            'row_counter_identifier' : 5,
        },
        'g' : {
            'column_coord' : [cell_size * 3],
            'row_counter_identifier' : 6,
        }
    }

    placement = drop_to[column]['column_coord']
    row_coord = base_row + row_counter[drop_to[column]['row_counter_identifier']]
    placement.append(row_coord)
    row_counter[drop_to[column]['row_counter_identifier']] += cell_size

    return placement

# Draw Token1 ------------------------------------------------------------------------------

# Create a random list of star coordinates
star_coord = []
    #Create x and y positions for star placements
for i in range(50):
    star_coord.append([randint(-50, 50), randint(50, 100)])

#Draw function for token 1
def draw_token_1(coord):
    #Import coordinates where the token will be placed upon
    coord_x = coord[0]
    coord_y = coord[1]

    #Draw night sky background
    penup()
    setheading(0)
    color('black')
    goto(-50 + coord_x, 0 + coord_y)
    pendown()
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    penup()

    #Draw stars
    color('white')
        #Place star placements in token
    for x_coord, y_coord in star_coord:
        goto(x_coord + coord_x, y_coord + coord_y)
        dot(3)
        
    #Draw moon
    goto(-50 + coord_x, 70 + coord_y)
    pendown()
    width(2)
    color('dim gray')
    fillcolor('light gray')
    begin_fill()
    circle(30, extent = 90)
    for i in range(2):
        left(90)
        forward(30)
    end_fill()

    #Draw ground
    color('burlywood')
    setheading(0)
    goto(-50 + coord_x, 30 + coord_y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(100)
        right(90)
        forward(30)
        right(90)
    end_fill()
    penup()

    #Draw token border
    color('saddle brown')
    setheading(0)
    goto(-50 + coord_x, 0 + coord_y)
    width(2)
    pendown()
    for i in range(4):
        forward(100)
        left(90)
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
        #Draw pyramid shape
        setheading(0)
        width(2)
        goto(x_pos, y_pos)
        color(pyramid_outline)
        fillcolor(pyramid_color)
        pendown()
        begin_fill()
        for i in range(3):
            forward(pyramid_length)
            left(120)
        setheading(135)
        forward(pyramid_depth)
        goto(pyramid_apex)
        end_fill()
        penup()
        pass

    #Draw Pyramid of Khufu
    pyramid(15 + coord_x, 15 + coord_y, 0.7)
    #Draw Pyramid of Khafre
    pyramid(-20 + coord_x, 10 + coord_y, 1)
    #Draw Pyramid of Menkaure
    pyramid(-40 + coord_x, 8 + coord_y, 0.7)
    pass

# Draw token 2 --------------------------------------------------------------------------------
#Draw function for token 2
def draw_token_2(coord):
    #Import coordinates where the token will be placed upon
    coord_x = coord[0]
    coord_y = coord[1]

    #Draw day time background
    penup()
    setheading(0)
    goto(-50 + coord_x, 0 + coord_y)
    color('sky blue')
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()

    #Draw Sun
    setheading(0)
    goto(-50 + coord_x, 70 + coord_y)
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
    goto(-50 + coord_x, 0 + coord_y)
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
    color('black')
    setheading(0)
    goto(-50 + coord_x, 0 + coord_y)
    width(2)
    pendown()
    for i in range(4):
        forward(100)
        left(90)
    penup()

    #Draw Tower of Pizza
    #Tower of Pisa constants
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
    goto(15 + coord_x, 5 + coord_y)
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
    goto(15 + coord_x, 5 + coord_y)
    color('forest green')
    forward(5)
    left(90)
    begin_fill()
    for i in range(2):
        forward(5)
        left(90)
        forward(30)
        left(90)
    end_fill()
    penup()
    pass

# Draw token 3 -------------------------------------------------------------------------------
#Draw function for token 3
def draw_token_3(coord):
    #Import coordinates where the token will be placed upon
    coord_x = coord[0]
    coord_y = coord[1]
    
    #Draw background
    penup()
    setheading(0)
    goto(-50 + coord_x, 0 + coord_y)
    color('light sky blue')
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()

    #Draw ground
    goto(-50 + coord_x, 0 + coord_y)
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
        goto(-50 + x + coord_x, 0 + coord_y)
        begin_fill()
        pendown()
        goto(0 + coord_x, 20 + coord_y)
        x += 20
        goto(-50 + x + coord_x, 0 + coord_y)
        end_fill()
        penup()

    #Draw border
    setheading(0)
    goto(-50 + coord_x, 0 + coord_y)
    color('dark goldenrod')
    width(2)
    pendown()
    for i in range(4):
        forward(100)
        left(90)
    penup()

    #Draw Eiffel Tower
    #Tower constants
    first_divider_coord = [-13.16 + coord_x, 38.79 + coord_y]
    second_divider_coord = [-7.28 + coord_x, 58.28 + coord_y]
    top_pillar_coord = [-4.28 + coord_x, 63.28 + coord_y]
    bottom_leg_length = 20
    bottom_leg_angle = 70
    mid_leg_length = 15
    mid_leg_angle = 75
    color('dark goldenrod')
    width(1)

    #Draw base
    #Draw left leg
    setheading(0)
    goto(-20 + coord_x, 20 + coord_y)
    pendown()
    forward(5)
    left(bottom_leg_angle)
    forward(bottom_leg_length)
    setheading(180)
    forward(5)
    goto(-20 + coord_x, 20 + coord_y)
    penup()
    #Draw right leg
    setheading(180)
    goto(20 + coord_x, 20 + coord_y)
    pendown()
    forward(5)
    right(bottom_leg_angle)
    forward(bottom_leg_length)
    setheading(0)
    forward(5)
    goto(20 + coord_x, 20 + coord_y)
    penup()
    #Draw Arc
    setheading(0)
    goto(-20 + coord_x, 20 + coord_y)
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
        forward((first_divider_coord[0] - coord_x) * -2)
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
    goto(-11.16 + coord_x, 43.79 + coord_y)
    penup()
    #Draw right leg
    setheading(180)
    goto(11.16 + coord_x, 43.79 + coord_y)
    pendown()
    forward(5)
    right(mid_leg_angle)
    forward(mid_leg_length)
    setheading(0)
    forward(5)
    goto(11.16 + coord_x, 43.79 + coord_y)
    penup()
    #Draw divider
    setheading(0)
    goto(second_divider_coord)
    pendown()
    for i in range(2):
        forward((second_divider_coord[0] - coord_x) * -2)
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
    goto(top_pillar_coord)
    setheading(0)
    forward((top_pillar_coord[0] - coord_x) * -2)
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
    pass

#Draw token 4 -------------------------------------------------------------------------------
#Create random coordinates for buldings
buildings_coord = []
for i in range(100):
    buildings_coord.append([randint(-50, 42), randint(0, 20)])
#Create random coordinates for lights
lights_coord = []
for i in range(100):
    lights_coord.append([randint(-45, 45), randint(5, 35)])

#Draw function for token 4
def draw_token_4(coord):
    #Import coordinates where the token will be placed upon
    coord_x = coord[0]
    coord_y = coord[1]

    #Draw background
    setheading(0)
    width(1)
    goto(-50 + coord_x, 0 + coord_y)
    color('dark slate blue')
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()

    #Draw buildings background
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
    #Draws random buildings
    for x_coord, y_coord in buildings_coord:
        goto(x_coord + coord_x, y_coord + coord_y)
        buildings(randint(15, 30))
    #Draws lights
    for x_coord, y_coord in lights_coord:
        color('yellow')
        goto(x_coord + coord_x, y_coord + coord_y)
        dot(3)
    penup()

    #Draw moon
    color('white')
    goto(-20 + coord_x, 75 + coord_y)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
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
    setheading(0)
    color('royal blue')
    goto(-length_b/2 + coord_x, 1 + coord_y)
    pendown()
    trapez(length_a, length_b, height)
    goto(-length_b/2 + coord_x, 5 + coord_y)
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
    penup()

    #Draw border
    setheading(0)
    goto(-50 + coord_x, 0 + coord_y)
    width(2)
    color('blue')
    pendown()
    for i in range(4):
        forward(100)
        left(90)
    penup()
    pass

#Make a function that descript the tokens
def descript():
    desc_font = ('Arial', 14, "normal")
    desc_color = 'black'
    #Descript Token 1
    draw_token_1([-500, 150])
    goto(-550, 100)
    color(desc_color)
    write('Token 1: Pyramids \n of Giza', font = desc_font)

    #Descript Token 2
    draw_token_2([-500, -150])
    goto(-550, -200)
    color(desc_color)
    write('Token 2: Tower \n of Pisa', font = desc_font)

    #Descript Token 3
    draw_token_3([500, 150])
    goto(450, 100)
    color(desc_color)
    write('Token 3: Eiffel \n Tower', font = desc_font)

    #Decript Token 4
    draw_token_4([500, -150])
    goto(450, -200)
    color(desc_color)
    write('Token 4: \n Taipei 101', font = desc_font)

    return

#Make a function that shows the winner of the game
def end_result(result):
    penup()

    result_font = ('Arial', 18, 'bold')
    if result == 'tie':
        #tie
        tie_color = 'black'
        goto(-50, 300)
        color(tie_color)
        write("It's a tie!", font = result_font)
    else:
        winner_color = 'black'
        goto(-150, 300)
        color(winner_color)
        write('Game over ' + result + ' Wins!', font = result_font)

    award_coord = {
        'Player 1' : [-420, 230],
        'Player 2' : [-420, -70],
        'Player 3' : [580, 230],
        'Player 4' : [580, -70],
    }

    if result != 'tie':
        award(award_coord[result], 'gold')
    elif result == 'tie':
        for i in range(4):
            i += 1
            award(award_coord['Player ' + str(i)], 'silver')

    pass

#Make a function that draws a star to award the winning player/token
def award(token_coord, color):
    penup()
    goto(token_coord)
    setheading(0)
    fillcolor(color)
    width(1)
    pendown()
    begin_fill()
    for i in range(5):
        right(180- 36)
        forward(20)
        left(72)
        forward(20)
    end_fill()
    pass

# Draw tokens on the board as per the provided data set---------------------------------------
def play_game(game):
    #Variables:
    #Create a list to show which tokens are on the surface
    token_surface = [0, 0 , 0, 0, 0, 0, 0]
    #Stores the moves that has occured
    moves_occured = []
    #Create a dictionary the identifies the token_surface with column placed
    token_surface_identifier = {
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6
    }

    #Create descriptions for the tokens
    descript()

    #Plays the game
    for next_move in game:
        #If the token type is called, draw the token type
        if next_move[1] is 1:
            draw_token_1(place_token_to(next_move[0]))
        elif next_move[1] is 2:
            draw_token_2(place_token_to(next_move[0]))
        elif next_move[1] is 3:
            draw_token_3(place_token_to(next_move[0]))
        elif next_move[1] is 4:
            draw_token_4(place_token_to(next_move[0]))

        #Updates the tokens on the surface
        token_surface[token_surface_identifier[next_move[0]]] = next_move[1]
        #Saves the moves that has occured 
        moves_occured.append(next_move)

        #Token top column counters (token 1 is [0], token 2 is [1] etc.)
        token_surface_occurence = [0, 0, 0, 0]
        #Adds counter to the token of the token is on the top columns
        for i in token_surface:
            if i > 0:
                token_surface_occurence[i-1] += 1
        
        #Game Result
        #Break the the for loop if the same token has occured 4 times on the top column
        if (token_surface_occurence[0] or token_surface_occurence[1] or token_surface_occurence[2] or token_surface_occurence[3]) == 4:
            #If Token 1 wins:
            if token_surface_occurence[0] == 4:
                end_result('Player 1')
                print('Token 1 Wins!')
            #If Token 2 wins:
            elif token_surface_occurence[1] == 4:
                end_result('Player 2')
                print('Token 2 Wins!')
            #If Token 3 wins:
            elif token_surface_occurence[2] == 4:
                end_result('Player 3')
                print('Token 3 Wins!')
            #If Token 4 wins:
            elif token_surface_occurence[3]  == 4:
                end_result('Player 4')
                print('Token 4 Wins!')
            break
        #If the game has finished without a winner, the game is a tie
        elif len(moves_occured) == len(game):
            end_result("tie")
            print("It's a tie!")
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to label the axes and mark the places for the
# ***** legend, by providing arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** theme and its tokens
title('Describe your theme and tokens here')

### Call the student's function to play the game
### ***** While developing your program you can call the "play_game"
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument.  Your "play_game" function must work for any data
### ***** set that can be returned by the "random_game" function.
# play_game(fixed_game_b4_2) # <-- use this for code development only
play_game(random_game()) # <-- this will be used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
