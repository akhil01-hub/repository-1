"""
This program uses the turtle library to draw a cake with multiple colorful layers
a candle on top, and a cherry, all placed on a table with four legs. The user is asked
to input dimensions for the table and cake, as well as colors for the table. The cake consist of four layers with predefined colors
and the candle and cherry are fixed in size and position.

Functions:

draw_table(width, height, color, table):
  Draws a rectangular table on the screen with the specified width, height, and color.

draw_leg(x, y, width, height, color, legs):
  Draws one leg of the table with the given dimensions and starting position.

draw_cake(width, height, color, legs):
  Draws one leg of the table with the given dimensions and starting position.

draw_cake(width, height, cake):
  Draws a layered cake with predefined colors for each layer, based on the given width and height.

darw_candle(x, y, candle_width, candle_height, candle):
  Draws a candle on top of the cake, along with a flame.

draw_cherry(x, y, cherry_radius, cursor):
  Draws a small cherry at the given position with the specified radius.
   
The program ends by printing "Your cake is ready! Happy Birthday!" to the console.
"""
from turtle import Screen, Turtle

sc = Screen()
sc.bgcolor("purple")
table_cursor = Turtle()
legs_cursor = Turtle()
cake_cursor = Turtle()
candle_cursor = Turtle()


def draw_table(width, height, color, table):
    """
    Draws a rectangular table using turtle graphics.

    Parameters:
    width(int): The width of the table.
    height(int): The height of the table.
    color(str): The color of the table.
    table(Turtle): The turtle object responsible for drawing the table.
    """
    table.color(color)
    table.fillcolor(color)
    table.penup()
    table.goto(-width / 2, -height / 2)  # Center the table vertically
    table.pendown()
    table.begin_fill()
    table.forward(width)
    table.left(90)
    table.forward(height)
    table.left(90)
    table.forward(width)
    table.left(90)
    table.forward(height)
    table.left(90)
    table.end_fill()
    table.hideturtle()



def draw_leg(x, y, width, height, color, legs):
    """
    Draws one leg of the table using turtle library.

    Parameters:
    x(int): The x-coordinate of the leg's starting position.
    y(int): The y-coordinate of the leg's starting position.
    width(int): The width of the leg.
    height(int): The height of the leg.
    color(str): The color of the leg.
    legs(Turtle): The turtle object responsible for drawing the leg.

    """
    
    # Front of the leg
    legs.color(color) 
    legs.fillcolor(color)
    legs.penup()
    legs.goto(x, y)
    legs.pendown()
    legs.begin_fill()
    legs.forward(width)
    legs.right(90)
    legs.forward(height)
    legs.right(90)
    legs.forward(width)
    legs.right(90)
    legs.forward(height)
    legs.end_fill()
    legs.right(90)



def draw_cake(width, height, cake):
    """
    Draws a multi-layered cake using turtle library.

    Parameters:
    width(int): The width of the cake.
    height(int): The width of the cake.
    cake(Turtle): The turtle object responsible for drawing the cake.
    The for loop in this block of code is used so that the we don't have to manually repeate the same same block of code four times
    for each layer, the loop itrates through the colors list and fills the color in each layer in the same order and moves up to draw the next layer on top of the previous one.
    """
    
    colors = ["brown", "pink", "red", "yellow"]
    layer_height = height // len(colors)
    cake.penup()
    cake.goto(-width / 2, 0)

    for color in colors:
        cake.fillcolor(color)
        cake.pendown()
        cake.begin_fill()
        cake.forward(width)
        cake.left(90)
        cake.forward(layer_height)
        cake.left(90)
        cake.forward(width)
        cake.left(90)
        cake.forward(layer_height)
        cake.left(90)
        cake.end_fill()
        cake.penup()
        cake.goto(-width / 2, cake.ycor() + layer_height)

def draw_candle(x, y, candle_width, candle_height, candle):
    """
    Draws a candle on top of the cake using turtle library, including a flame.

    Parameters:
    x(int): The x-coordinate of the candle's base.
    y(int): The y-coordinate of the candle's base.
    candle_width(int): The width of the candle.
    candle_height(int): The height of the candle.
    candle(Turtle): Thhe turtle object responsible for tdrawing the candle.

    """
    candle.color("sky blue")
    candle.fillcolor("sky blue")
    candle.penup()
    candle.goto(x, y)
    candle.pendown()
    candle.begin_fill()
    candle.setheading(90)  # Face upwards
    candle.forward(candle_height)
    candle.right(90)
    candle.forward(candle_width)
    candle.right(90)
    candle.forward(candle_height)
    candle.right(90)
    candle.forward(candle_width)
    candle.end_fill()

    # Candle flame
    candle.fillcolor("orange")
    candle.begin_fill()
    candle.penup()
    candle.goto(x + candle_width / 2, y + candle_height)
    candle.pendown()
    candle.circle(7)  # Flame size
    candle.end_fill()
    candle.hideturtle()

def draw_cherry(x, y, cherry_radius, cursor):
    """
    Draws a chherry on top of the cake using turtle library.

    Parameters:
    x(int): The x-coordinate for the cherry's center.
    y(int): The y-coordinate for the cherry's center.
    cherry_radius(int): The radius of the cherry.
    cursor(Turtle): The turtle object responsible for drawing the cherry.

    """

    cursor.penup()
    cursor.goto(x, y)
    cursor.pendown()
    cursor.color("red")
    cursor.begin_fill()
    cursor.circle(cherry_radius)
    cursor.end_fill()
    cursor.hideturtle()

# Get user inputs

table_width = int(input("Enter the table width: "))
table_height = int(input("Enter the table height: "))
table_color = input("Enter the table color: ")
cake_width = int(input("Enter the cake width: "))
cake_height = int(input("Enter the cake height: "))
cherry_radius = 10 # cherry radius fixed



# Draw the objects
draw_table(table_width, table_height, table_color, table_cursor)

draw_leg((-table_width/2), (table_height/2), (table_height/2), (table_width/2), table_color, legs_cursor)
draw_leg((-table_width/4), (table_height/2), (table_height/2), (table_width/2), table_color, legs_cursor)
draw_leg((table_width/4), (table_height/2), (table_height/2), (table_width/2), table_color, legs_cursor)
draw_leg((table_width/2), (table_height/2), (table_height/2), (table_width/2), table_color, legs_cursor)

draw_cake(cake_width, cake_height, cake_cursor)




candle_width = 10
candle_height = 50
draw_candle(20, cake_height, candle_width, candle_height, candle_cursor)  # Centered on the cake's top

# Draw cherry on top of the cake
draw_cherry(0, cake_height / 2 + candle_height, cherry_radius, candle_cursor)

print("Your cake is ready! Happy Birthday!")

sc.exitonclick()
