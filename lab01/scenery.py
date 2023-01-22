'''
Ethan R Feldman
Scenery
CSCI 141 Lab 1
'''

# Imports the turtle library
# Imports the random library
# Imports pi
import turtle
import random
import math

# Global penInk variable
penInk = 0

# ~ #

def initialize():
	'''
	Initializes the pen
	'''

	# Sets the pensize of the turtle
	turtle.pensize(2)

	# Sets the position of the turtle without drawing
	turtle.penup()
	turtle.setpos(-250,0)

	# Sets the turtle to draw mode
	turtle.pendown()

	# Sets the pen color to green
	turtle.pencolor("green")


def drawTree():
	'''
	Draws either a pine or maple tree randomly with random sizes
	'''

	# Grabes the global variable
	global penInk

	# Moves forwards 
	turtle.forward(100)
	penInk += 100

	# Takes a random int between 0 and 1 to determind the tree type
	if random.randint(0,1) == 1:
		# Draws a pine tree
		# While drawing the tree, penInk is constantly recording the amount of ink used
		
		# Sets trunk height
		trunkHeight = random.randint(50,200)
		topLength = trunkHeight*0.6

		# Records the penInk
		penInk = penInk + trunkHeight + topLength*3

		# Draws trunk
		turtle.left(90)
		turtle.forward(trunkHeight)

		# Draws the triangle top
		turtle.left(90)
		turtle.forward(topLength/2)
		turtle.right(120)
		turtle.forward(topLength)
		turtle.right(120)
		turtle.forward(topLength)
		turtle.right(120)
		turtle.forward(topLength/2)

		# Pen up, move down the trunk, pen down
		turtle.left(90)
		turtle.penup()
		turtle.forward(trunkHeight)
		turtle.pendown()

	else:
		# Draws a maple tree

		# Sets trunk height
		trunkHeight = random.randint(50,150)
		topRadius = trunkHeight*0.4

		# Records the penInk
		penInk = penInk + trunkHeight + 2*math.pi*topRadius

		# Draws trunk
		turtle.left(90)
		turtle.forward(trunkHeight)

		# Draws the circle top
		turtle.right(90)
		turtle.circle(topRadius)

		# Pen up, move down the trunk, pen down
		turtle.right(90)
		turtle.penup()
		turtle.forward(trunkHeight)
		turtle.pendown()

	# Draws the rest of the grass
	turtle.left(90)
	turtle.forward(100)
	penInk += 100


def drawHouse(houseCol):
	'''
	Draws the house with the parameter house color (houseCol)
	'''

	# Grabes the global variable
	global penInk

	# Sets the pen color to houseCol
	turtle.pencolor(houseCol)

	# Finds the roof length
	roofLength = 50*math.sqrt(2)

	# Records the amount of ink used
	penInk += 300 + roofLength*2

	# Draws the house
	turtle.left(90)
	turtle.forward(100)
	turtle.right(45)
	turtle.forward(roofLength)
	turtle.right(90)
	turtle.forward(roofLength)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(100)

	# Pen up, turtle moves backwards, pen down
	turtle.right(180)
	turtle.penup()
	turtle.forward(100)
	turtle.pendown()

	# Changes the pen color back to green
	turtle.pencolor("green")


def drawScene(housePos,houseCol):
	'''
	This function contains all the turtle drawing functions and draws the scene
	'''

	# Initializes the pen
	initialize()

	# Depending on the house position the program will run differently
	if housePos == 1:
		# This setup puts the house first followed by the 2 trees

		# Draws the house
		drawHouse(houseCol)
		
		# Draws the first tree
		drawTree()

		# Sets the pen backwards to keep 100 pixels between tree trunks
		turtle.penup()
		turtle.left(180)
		turtle.forward(100)
		turtle.right(180)
		turtle.pendown()

		# Draws the second tree
		drawTree()

	elif housePos == 2:
		# This setup puts the house in the middle of the 2 trees
		
		# Draws the first tree
		drawTree()

		# Draws the house
		drawHouse(houseCol)

		# Draws the second tree
		drawTree()

	elif housePos == 3:
		# This setup puts the house in the middle of the 2 trees
		
		# Draws the first tree
		drawTree()

		# Sets the pen backwards to keep 100 pixels between tree trunks
		turtle.penup()
		turtle.left(180)
		turtle.forward(100)
		turtle.right(180)
		turtle.pendown()

		# Draws the second tree
		drawTree()

		# Draws the house
		drawHouse(houseCol)

	else:
		print("drawScene(): you messed up the if statement")

	

def main():
	'''
	This function asks for the scenery of the turtle drawing
	'''

	# Asks where there is a house or not
	houseStr = input("Is there a house in the forest (y/n)? ")

	# If y or yes for a house in the forest
	# houseStr.lower() changes the input to lowercase in case the user capitalizes it
	if houseStr.lower() == "y" or houseStr.lower() == "yes":
		# Sets the house position
		housePos = int(input("At what position (1/2/3)? "))

		# If someone puts in anything other than 1, 2, or 3 then the default will be 2
		if housePos != 1 and housePos != 2 and housePos != 3:
			housePos = 2
			print("*Nice try, the house will be in position 2*")
		# Sets the house color
		houseCol = input("What color is the house? ")

		# Calls the drawScene function
		drawScene(housePos,houseCol)

		# Prints the final amount of ink used
		print(f"We used {penInk} pixels of ink for the drawing")

		# Once the program is all exicuted, it will wait for the user to click the (X) button and print "Done"
		print("Close the program with the (X) button")
		turtle.done()
		print("Done")

	else:
		print("You have decided not to continue or didn't answer yes correctly, ending program...")
	
	
# Starts the program
if __name__ == "__main__":
	main()