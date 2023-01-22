'''
Ethan R Feldman
Shapy Turtle
CSCI 141 PSS 4
'''

# Imports the need libraries
import turtle


# ~ #


def init():
	'''
	Resets the turtle pen
	Precondition: none
	Postcondition: none
	'''

	# Sets the speed
	turtle.speed(0)

	# Clears the canvas 
	turtle.clear()

	# Sets the turtle to the center
	turtle.penup()
	turtle.goto(0,0)
	turtle.pendown()

	turtle.color("black")


def find_letter(s):
	'''
	Finds the first non-numeric character in the string
	Precondition: string (s)
	Postcondition: returns either the place of the non-numeric or len(s) if (s) contains all numeric values
	'''

	# Counter for the for-loop
	counter = 0

	# Checks every character (c) in the string (s)
	for c in s:
		# If (c) is not a numeric
		if c.isdigit() == False:
			# Return counter which is the place of the non-numeric
			return counter
		else:
			# Keep counting
			counter += 1

			# If the counter reaches the end
			if counter == len(s):
				# Returns None since all values in string (s) are numeric
				return len(s)


def func_left(counter,s):
	'''
	Turns the turtle left degrees
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1
	
	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(<) is missing supporting numbers at the end")
		return None
	
	# Checks if the proceeding 
	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		num = int(s[a:b])

		# Turns left num degrees
		turtle.left(num)

		#print(f"<{num}")

		# Success
		return True


def func_right(counter,s):
	'''
	Turns the turtle right degrees
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1

	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(>) is missing supporting numbers at the end")
		return None

	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		num = int(s[a:b])

		# Turns right num degrees
		turtle.right(num)

		#print(f">{num}")
		
		# Success
		return True


def func_square(counter,s):
	'''
	Makes a square
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1

	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(S) is missing supporting numbers at the end")
		return None

	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		num = int(s[a:b])

		# Makes a square
		turtle.left(90)
		turtle.forward(num)
		turtle.left(90)
		turtle.forward(num)
		turtle.left(90)
		turtle.forward(num)
		turtle.left(90)
		turtle.forward(num)

		#print(f"S{num}")


def func_triangle(counter,s):
	'''
	Makes an equalateral triangle
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1

	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(T) is missing supporting numbers at the end")
		return None

	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		num = int(s[a:b])

		# Makes an equilateral triangle
		turtle.forward(num)
		turtle.left(120)
		turtle.forward(num)
		turtle.left(120)
		turtle.forward(num)
		turtle.left(120)
		turtle.forward(num)

		#print(f"T{num}")

		# Success
		return True


def func_circle(counter,s):
	'''
	Makes a circle
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1

	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(C) is missing supporting numbers at the end")
		return None
	
	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		num = int(s[a:b])

		# Makes a circle with num radius
		turtle.circle(num)

		#print(f"C{num}")

		# Success
		return True


def func_forwards(counter,s):
	'''
	Moves turtle forwards
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1

	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(F) is missing supporting numbers at the end")
		return None

	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		num = int(s[a:b])

		# Moves forwards num units
		turtle.forward(num)

		#print(f"F{num}")

		# Success
		return True


def func_backwards(counter,s):
	'''
	Moves turtle backwards
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1

	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(B) is missing supporting numbers at the end")
		return None

	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		num = int(s[a:b])

		# Moves backwards num units
		turtle.backward(num)

		#print(f"B{num}")

		# Success
		return True

		
def func_color(counter,s):
	'''
	Changes the turtle's color
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1

	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(Z) is missing supporting numbers at the end")
		return None

	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		num = int(s[a:b])
		
		# Choses the color from the assigment using the num in a if statement
		if num == 0:
			turtle.color("red")
		elif num == 1:
			turtle.color("blue")
		elif num == 2:
			turtle.color("green")
		elif num == 3:
			turtle.color("yellow")
		elif num == 4:
			turtle.color("brown")
		else:
			turtle.color("black")

		#print(f"Z{num}")

		# Success
		return True


def func_up(counter,s):
	'''
	Turtle penup()
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1

	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		b = a

	if b == a:
		# Pen up
		turtle.penup()
		#print("U")

		# Success
		return True
	else:
		# Resets
		init()
		print("There should be no numbers following (U)")
		return None


def func_down(counter,s):
	'''
	Turtle pendown()
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1

	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		b = a

	if b == a:
		# Pen up
		turtle.pendown()
		#print("D")

		# Success
		return True
	else:
		# Resets
		init()
		print("There should be no numbers following (D)")
		return None


def func_rectangle(counter,s):
	'''
	Makes a rectangle
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1
	
	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(R) is missing supporting numbers at the end")
		return None
	
	# Checks if the proceeding 
	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		numH = int(s[a:b])

		#print(f"R{numH}")
	
	# (a) is the (b) spot+2
	a = b+1
	
	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(R) is missing second supporting numbers at the end")
		return None
	
	# Checks if the proceeding 
	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		numW = int(s[a:b])

		#print(f",{numW}")
	
	# Makes a rectangle
	turtle.forward(numW)
	turtle.left(90)
	turtle.forward(numH)
	turtle.left(90)
	turtle.forward(numW)
	turtle.left(90)
	turtle.forward(numH)
	turtle.left(90)
	turtle.forward(numW)

	# Success
	return True


def func_goto(counter,s):
	'''
	Turtle goto()
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1
	
	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(G) is missing supporting numbers at the end")
		return None
	
	# Checks if the proceeding 
	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		numX = int(s[a:b])

		#print(f"G{numX}")
	
	# (a) is the (b) spot+2
	a = b+1
	
	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(G) is missing second supporting numbers at the end")
		return None
	
	# Checks if the proceeding 
	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		numY = int(s[a:b])

		#print(f",{numY}")
	
	# Turtle goto
	turtle.penup()
	turtle.goto(numX,numY)
	turtle.pendown()

	# Success
	return True


def func_polygon(counter,s):
	'''
	Makes a polygon
	Precodition: counter (counter), string (s)
	Postcondition: returns (True) or (None)
	'''

	# (a) is the current spot+1
	a = counter+1
	
	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(P) is missing supporting numbers at the end")
		return None
	
	# Checks if the proceeding 
	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		numS = int(s[a:b])

		#print(f"P{numS}")
	
	# (a) is the (b) spot+2
	a = b+1
	
	try:
		# (b) finds the next non-numeric starting from (a)
		b = find_letter(s[a:])+a
	except:
		print("(P) is missing second supporting numbers at the end")
		return None
	
	# Checks if the proceeding 
	if b == a:
		##print("There are no numbers proceeding the command!")
		init()
		print(f"({s[counter]}) is missing supporting numbers")
		return None
	else:
		# So the number should be whatever the current spot+1 to the spot of the next non-numeric
		numL = int(s[a:b])

		#print(f",{numL}")
	
	# Makes the polygon
	# sides (numS)
	# length (numL)
	# angle is related to numS
	angle = 360/numS
	for x in range(0,numS):
		turtle.left(angle)
		turtle.forward(numL)
	
	# Success
	return True


def interpret(s):
	'''
	Interprets a string into a squence of turtle commands 
	Precondition: string (s)
	Postcondition: draws an image with turtle based on the commands and will return either True or None
	'''

	# Declares a counter placeholder
	counter = 0

	if len(s) == 0:
		init()
		print("This sting is empty")
		return None

	# Checks the frist chracter with a Try-Except case
	try:
		firstDigit = int(s[0])

		# If it continues, then the first character is a number
		init()
		print("The first character was a number")
		return None
	except:
		# Checks every character (c) in the string (s)
		for c in s:
			# If (c) is a non numeric
			if c.isdigit() == False:
				# Goes through the different commands
				if c == "<":
					# Calls the function and returning None if an error
					if func_left(counter,s) == None:
						return None
				
				elif c == ">":
					# Calls the function and returning None if an error
					if func_right(counter,s) == None:
						return None

				elif c == "S":
					# Calls the function and returning None if an error
					if func_square(counter,s) == None:
						return None

				elif c == "T":
					# Calls the function and returning None if an error
					if func_triangle(counter,s) == None:
						return None

				elif c == "C":
					# Calls the function and returning None if an error
					if func_circle(counter,s) == None:
						return None

				elif c == "F":
					# Calls the function and returning None if an error
					if func_forwards(counter,s) == None:
						return None

				elif c == "B":
					# Calls the function and returning None if an error
					if func_backwards(counter,s) == None:
						return None

				elif c == "Z":
					# Calls the function and returning None if an error
					if func_color(counter,s) == None:
						return None

				elif c == "U":
					# Calls the function and returning None if an error
					if func_up(counter,s) == None:
						return None

				elif c == "D":
					# Calls the function and returning None if an error
					if func_down(counter,s) == None:
						return None

				elif c == "R":
					# Calls the function and returning None if an error
					if func_rectangle(counter,s) == None:
						return None

				elif c == "G":
					# Calls the function and returning None if an error
					if func_goto(counter,s) == None:
						return None

				elif c == "P":
					# Calls the function and returning None if an error
					if func_polygon(counter,s) == None:
						return None

				# Don't do anything with this characters
				elif c == ",":
					pass
				elif c == "h":
					pass
				elif c == "w":
					pass
				elif c == "s":
					pass
				elif c == "l":
					pass
				elif c == "x":
					pass
				elif c == "y":
					pass
				elif c == "-":
					# This means there is a negative number somewhere
					init()
					print(f"(-) isn't a valide input")
					return None
				else:
					# This means something else unspecified is in here
					init()
					print(f"({s[counter]}) is unspecified")
					return None
			else:
				pass
			
			##print(counter)
			counter += 1
		
		# The read was a success
		return True
		

def find_non_numeric(s):
	'''
	Finds the first non-numeric character in the string
	Precondition: string (s)
	Postcondition: returns either the place of the non-numeric or len(s) if (s) contains all numeric values
	'''

	# Counter for the for-loop
	counter = 0

	# Checks every character (c) in the string (s)
	for c in s:
		# If (c) is not a numeric
		if c.isdigit() == False:
			# Return counter which is the place of the non-numeric
			return counter
		else:
			# Keep counting
			counter += 1

			# If the counter reaches the end
			if counter == len(s):
				# Returns None since all values in string (s) are numeric
				return None


def main():
	'''
	Asks for user input and calls the functions above
	'''

	# Sets up the turtle
	init()
	
	# Asks for user code
	call = input("Enter your code: ")

	# interprets the code
	answ = interpret(call)

	# Waits for the window to be closed
	print("End the program by closing the window")
	turtle.done()

if __name__ == "__main__":
	main()
