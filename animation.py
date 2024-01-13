Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/khali/OneDrive/Desktop/fst/python/animation.py
t.clear()
>>> import turtle
... 
... # Function to draw the number 7 using turtle graphics
... def draw_number_7(size):
...     turtle.penup()
...     turtle.goto(0, 0)
...     turtle.pendown()
... 
...     turtle.forward(2 * size)  # Draw the horizontal line
...     turtle.right(90)
...     turtle.forward(size)      # Draw the vertical line
... 
... # Set up the turtle window
... turtle.speed(1)  # Set the drawing speed (1 is slowest, 10 is fastest)
... turtle.pensize(5)  # Set the pen size
... 
... # Set the size of the number 7
... number_size = 50
... 
... # Draw the number 7 with the specified size
... draw_number_7(number_size)
... 
... # Close the turtle graphics window on click
... turtle.exitonclick()
