'''
Ethan R Feldman
Bowties
CSCI 141 Lab 2
'''

# Imports the needed lbraries
import turtle


# ~ #


def draw_bowtie0(size):
	'''
	Draws nothing
	'''
	
	pass


def draw_bowtie1(size):
	'''
	Draws one bowite
	Preconditions: turtle facing East
	Postconditions: turtle facing East in the starting location
	'''

	# Draws the bowtie
	turtle.left(30)
	turtle.forward(size)
	turtle.right(120)
	turtle.forward(size)
	turtle.right(120)
	turtle.forward(2 * size)
	turtle.left(120)
	turtle.forward(size)
	turtle.left(120)
	turtle.forward(size)
	turtle.right(30)

	# Gets in position to draw the circle by moving down without drawing
	turtle.penup()
	turtle.right(90)
	turtle.forward(size/4)
	turtle.left(90)
	turtle.pendown()

	# Draws the circle in the center and fill it in pink
	turtle.begin_fill()
	turtle.circle(size/4)
	turtle.end_fill()

	# Puts the pen in the position it was at the beginning, ready to draw again
	turtle.penup()
	turtle.left(90)
	turtle.forward(size/4)
	turtle.right(90)
	turtle.pendown()


def draw_bowtie2(size):
	'''
	Draws 4 bowties around the center bowtie
	Preconditions: turtle facing East
	Postconditions: turtle facing East in the starting location
	'''
	# Draws the first bowtie
	draw_bowtie1(size)

	# Draws the upper-outer bowties
	turtle.penup()
	turtle.left(150)
	turtle.forward(size*2)
	turtle.right(180)
	turtle.pendown()
	draw_bowtie1(size/3)
	turtle.penup()
	turtle.forward(size*2)
	turtle.left(60)
	turtle.forward(size*2)
	turtle.pendown()
	draw_bowtie1(size/3)
	turtle.penup()
	turtle.forward(-size*2)
	turtle.right(60)

	# Draws the lower-outer bowties
	turtle.forward(size*2)
	turtle.pendown()
	draw_bowtie1(size/3)
	turtle.penup()
	turtle.forward(-size*2)
	turtle.right(120)
	turtle.forward(size*2)
	turtle.pendown()
	draw_bowtie1(size/3)
	turtle.penup()
	turtle.forward(-size*2)
	turtle.left(150)
	turtle.pendown()


def draw_bowtie3(size):
	'''
	Draws a total of 9 bowties
	Preconditions: turtle facing East
	Postconditions: turtle facing East in the starting location
	'''

	# Draws teh first bowtie
	draw_bowtie1(size)

	# Draws the upper-outer bowties
	turtle.penup()
	turtle.left(150)
	turtle.forward(size*2)
	turtle.right(180)
	turtle.pendown()
	draw_bowtie2(size/3)
	turtle.penup()
	turtle.forward(size*2)
	turtle.left(60)
	turtle.forward(size*2)
	turtle.pendown()
	draw_bowtie2(size/3)
	turtle.penup()
	turtle.forward(-size*2)
	turtle.right(60)

	# Draws the lower-outer bowties
	turtle.forward(size*2)
	turtle.pendown()
	draw_bowtie2(size/3)
	turtle.penup()
	turtle.forward(-size*2)
	turtle.right(120)
	turtle.forward(size*2)
	turtle.pendown()
	draw_bowtie2(size/3)
	turtle.penup()
	turtle.forward(-size*2)
	turtle.left(150)
	turtle.pendown()


def draw_bowties(size, depth):
	'''
	Draws the bowtie fractal for as many itterations as depth
	Preconditions: turtle facing East
	Postconditions: turtle facing East in the starting location
	'''

	# If the depth reaches 0, then the recursion stops
	if depth == 0:
		pass
	else:
		# Draws the first bowtie
		draw_bowtie1(size)

		# Draws the upper-outer bowties
		turtle.penup()
		turtle.left(150)
		turtle.forward(size*2)
		turtle.right(180)
		turtle.pendown()
		draw_bowties(size/3, depth-1)
		turtle.penup()
		turtle.forward(size*2)
		turtle.left(60)
		turtle.forward(size*2)
		turtle.pendown()
		draw_bowties(size/3, depth-1 )
		turtle.penup()
		turtle.forward(-size*2)
		turtle.right(60)

		# Draws the lower-outer bowties
		turtle.forward(size*2)
		turtle.pendown()
		draw_bowties(size/3, depth-1)
		turtle.penup()
		turtle.forward(-size*2)
		turtle.right(120)
		turtle.forward(size*2)
		turtle.pendown()
		draw_bowties(size/3, depth-1)
		turtle.penup()
		turtle.forward(-size*2)
		turtle.left(150)
		turtle.pendown()


def main():
	'''
	Calls the bowtie functions in order
	'''

	# Sets the canvas size
	turtle.setup(720,720)

	# Sets the pen color and fill color
	turtle.color("cyan", "pink")

	# Makes the pen really fast
	turtle.speed(0)
	
	# Makes the 0th depth fractal
	draw_bowtie0(turtle.window_width()/6)

	# Makes the 1th depth fractal
	a = input("Press ENTER to continue to 1th depth fractal: ")
	turtle.clear()
	draw_bowtie1(turtle.window_width()/6)

	# Makes the 2th depth fractal
	a = input("Press ENTER to continue to 2th depth fractal: ")
	turtle.clear()
	draw_bowtie2(turtle.window_width()/6)

	# Makes the 3th depth fractal
	a = input("Press ENTER to continue to 3th depth fractal: ")
	turtle.clear()
	draw_bowtie3(turtle.window_width()/6)
	
	# Makes the 4th depth fractal
	a = input("Press ENTER to continue to 4th depth fractal: ")
	turtle.clear()
	draw_bowties(turtle.window_width()/6, 4)

	# Makes the 5th depth fractal
	a = input("Press ENTER to continue to 5th depth fractal: ")
	turtle.clear()
	draw_bowties(turtle.window_width()/6, 5)

	# Makes the d-th depth fractal
	d = int(input("What depth would you like for the fractal? "))
	turtle.clear()
	draw_bowties(turtle.window_width()/6, d)

	print("Close the window to end the program.")
	turtle.done()

if __name__ == "__main__":
	main()