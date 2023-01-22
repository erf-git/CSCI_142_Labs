'''
Ethan R Feldman
Arrows
CSCI 141 Lab 3
'''

# Imports the needed libraries
import turtle
import math
import random

# Defines the global variables
MAX_FIGURES = 500
BOUNDING_BOX = 200
BOUNDING_BOX_DIFFERENCE = 60
MAX_DISTANCE = 30
MAX_SIZE = 30
MAX_ANGLE = 30


# ~ #


def check_ahead(t):
	'''
	Checks if the position of the next arrow will fit within the BOUNDING_BOX
	Precondition: t is a counter when I want to debug the code, otherwise it has no effect on the program
	Postcondition: none
	'''

	# Pen up
	turtle.penup()

	# Calculates a random angle for the next arrow using the MAX_ANGLE
	ranAngle = random.randint(-MAX_ANGLE,MAX_ANGLE)
	turtle.right(ranAngle)

	# Calculates a random distance for the next arrow using the MAX_DISTANCE
	ranDistance = random.randint(1,MAX_DISTANCE)
	turtle.forward(ranDistance)

	# Checks to see if the next arrow will be within the BOUNDING_BOX by comparing it's position
	checkX,checkY = turtle.pos()
	if -BOUNDING_BOX+BOUNDING_BOX_DIFFERENCE<=checkX and -BOUNDING_BOX+BOUNDING_BOX_DIFFERENCE<=checkY and checkX<=BOUNDING_BOX-BOUNDING_BOX_DIFFERENCE and checkY<=BOUNDING_BOX-BOUNDING_BOX_DIFFERENCE:
		# It found a suitable place for the next arrow
		turtle.pendown()

		#print(f"{t}: ({checkX},{checkY}) inside")

	else:
		# It DIDN'T find a suitable place for the next arrow, so it goes backwards
		turtle.backward(ranDistance)
		turtle.right(180)

		#print(f"{t}: ({checkX},{checkY}) outside")

		# Calls check_ahead to find a new location
		check_ahead(t)


def change_color():
	'''
	Changes the fillcolor and pencolor of the arrow randomly
	Precondition: none
	Postcondition: none
	'''

	# Calculates the random R,G,B
	ranRed = random.random()
	ranGre = random.random()
	ranBlu = random.random()

	# Sets the fillcolor and pencolor to the random color
	turtle.fillcolor(ranRed,ranGre,ranBlu)
	turtle.pencolor(ranRed,ranGre,ranBlu)

	# Begins fill
	turtle.begin_fill()


def eq_tri_area(side):
	'''
	Computes the area of an equilateral triangle with a given side length
	Precondition: side length
	Postcondition: triangle area
	'''

	# Calculates the area of the equalateral triangle
	triangleArea = (math.sqrt(3)*side**2)/4

	# Returns the area value
	return triangleArea


def draw_figures_rec(num, len, t):
	'''
	Draws the spiral triangle shape by recursion
	Preconditon: parameters num, len, t
	Postcondition: returns totalArea
	'''

	# It will continue to make triangles until the num reaches 0
	if num == 0:
		# Returns 0
		return 0

	else:
		# Begins fill
		change_color()

		# Makes the triangles
		turtle.forward(len)
		turtle.left(120)
		turtle.forward(len)
		turtle.left(120)
		turtle.forward(len)
		turtle.left(120)

		# Ends fill
		turtle.end_fill()
		
		# Sets the pointer up for the next triangle
		check_ahead(t)

		# Gets the totalArea and adds previous totalAreas to return the total totalArea
		totalArea = draw_figures_rec(num-1,random.randint(1,MAX_SIZE),t+1)
		return eq_tri_area(len) + totalArea


def draw_figures_iter(num, len, t):
	'''
	Draws the spiral triangle shape by iteration
	Preconditon: parameters num, len, t
	Postcondition: returns totalArea
	'''

	# Defines the parimeter at the beginning at 0
	totalArea = 0

	# Draws the triangles repeatedly in the spiral pattern
	while num > 0:
		# Begins fill
		change_color()

		# Draws the triangle
		turtle.forward(len)
		turtle.left(120)
		turtle.forward(len)
		turtle.left(120)
		turtle.forward(len)
		turtle.left(120)

		# Ends fill
		turtle.end_fill()

		# Sets the pointer up for the next triangle
		check_ahead(t)

		# Adds the new triangle's perimeter to the total perimeter
		# Counts down num and len
		totalArea += eq_tri_area(len)
		num -= 1
		len = random.randint(1,MAX_SIZE)
		t += 1
	
	# Returns total perimeter at the end
	return totalArea 


def main():
	'''
	Takes user input for the functions
	'''

	# Gets the arrow amount
	arrowAmount = int(input("Arrows (0-500): "))

	# Check to see if the arrow amount is viable
	if 0<=arrowAmount and arrowAmount<=500:
		# Sets:
		# the turtle speed
		# the window size
		turtle.speed(0)
		turtle.setup(400,400)

		print()

		# Let the user know
		print("Drawing arrows with Recursion...")

		# Prints the totalArea of the arrows
		a = draw_figures_iter(arrowAmount,random.randint(1,MAX_SIZE),1)
		print(f"The total area painted is {a} units.")

		print()

		# Starts the next round
		temp = input("Press ENTER to continue.")

		# Sets:
		# the pen up
		# the pen to the center
		# the pen down
		# clears the screen
		#turtle.reset()
		turtle.penup()
		turtle.setpos(0,0)
		turtle.pendown()
		turtle.clear()

		print()

		# Let the user know
		print("Drawing arrows with Iteration...")

		# Prints the totalArea of the arrows
		a = draw_figures_rec(arrowAmount,random.randint(1,MAX_SIZE),1)
		print(f"The total area painted is {a} units:")

		print()

		# Waits for the user to close the window to exit the program
		print("Close the canvas window to quit.")
		turtle.done()

	else:
		print("Arrows must be between 0 and 500 inclusive!")
	

if __name__ == "__main__":
	main()