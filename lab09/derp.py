'''
Ethan R Feldman
Derp
CSCI 141 Lab 9

The Derp interpreter parses and evaluates prefix integer expressions 
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, prints the infix expression with 
parentheses to denote order of operation, and evaluates the expression to
print the result.
'''

# Imports the needed libraries
from derp_types import *


##############################################################################
# infix
##############################################################################

def infix(node):
	'''
	Takes a parse tree and returns a string that represents the fully parenthesized, infix form of the expression.
	Precondition: parsed data (node)
	Postcondition: string version of data
	'''

	# Recursively creates the expression string depending on the node type
	if node != None:
		if isinstance(node, VariableNode):
			return str(node.value)

		elif isinstance(node, LiteralNode):
			return str(node.value)
			
		elif isinstance(node, MathNode):
			return f"({infix(node.left)} {str(node.value)} {infix(node.right)})"

##############################################################################
# parse
##############################################################################

def is_digit(x):
	'''
	Test if the input is an number
	Precondition: input (x)
	Postcondition: True/False
	'''

	# Test by trying to make it an int
	try:
		newX = int(x)
		return True
	except:
		return False

def is_variable(x):
	'''
	Test if the input is an variable
	Precondition: input (x)
	Postcondition: True/False
	'''

	# Checks against any preestablished operations
	# (* // - +)
	if x == "*":
		return False
	elif x == "//":
		return False
	elif x == "-":
		return False
	elif x == "+":
		return False
	else:
		return True

def parse(tokens):
	'''
	From a prefix stream of tokens, construct and return the tree, as a collection of Nodes, that represent the expression.
	Precondition: tokens is a non-empty list of strings
	Postcondition: returns the built tree
	'''
	
	# Checks if tokens is empty first
	if len(tokens) == 0:
		# Error handling
		return None
	
	# Takes the top token from the list out every recursive step
	head = tokens.pop(0)

	# Recursively finds LiteralNodes and VariableNode to create the final MathNode tree
	if is_digit(head):
		return LiteralNode(int(head))
	elif is_variable(head):
		return VariableNode(head)
	else:
		# Splits into left and right
		left = parse(tokens)
		right = parse(tokens)

		# Returns finalized tree
		return MathNode(left, head, right)

##############################################################################
# evaluate
##############################################################################

def evaluate(node, sym_tbl):
	'''
	Returns the result of evaluating the expression represented by node.
	Precondition: all variable names must exist in sym_tbl
	precondition: node is a valid derp tree node
	'''
	
	# Recursively goes thru the nodes in an inorder style
	if node != None:
		if isinstance(node, VariableNode):
			# Finds the value of the variable in the sym_tbl
			if node.value not in sym_tbl:
				Print(f"Error trying to find the corresponding value for ({node.value}), defaulting to (1)")
				return 1
			return sym_tbl[node.value]

		elif isinstance(node, LiteralNode):
			# Just returns the plan value
			return node.value

		elif isinstance(node, MathNode):
			# Checks what operation to do
			if node.value == "*":
				return evaluate(node.left, sym_tbl) * evaluate(node.right, sym_tbl)
			elif node.value == "//":
				return evaluate(node.left, sym_tbl) // evaluate(node.right, sym_tbl)
			elif node.value == "-":
				return evaluate(node.left, sym_tbl) - evaluate(node.right, sym_tbl)
			elif node.value == "+":
				return evaluate(node.left, sym_tbl) + evaluate(node.right, sym_tbl)

##############################################################################
# read_file
##############################################################################

def read_file(fileName):
	'''
	Takes the name of a symbol table file, reads the file, and returns the symbol table. 
	Precondition: file name (fileName)
	Postcondition: data (data)
	'''

	# Creates an empty list and data
	data = {}
	lines = []

	# Gets every line from the txt file
	with open(fileName) as f:
		lines = f.read().splitlines()
	
	print("Adding data to symbol table...")

	# Puts every line the data
	for x in lines:
		l = x.split(" ")
		data[l[0]] = int(l[1])
		print(f"{l[0]} = {l[1]}")

	# Returns the data
	return data

##############################################################################
# main
##############################################################################

def main():
	'''
	Handles user input and does as described in the prompt pdf
	'''

	# Welcome and asks for the file name for the symbol table
	print("Welcome to Derp!")
	fileName = input("Enter the symbol_table file name: ")
	print()

	# Creates the symbol table using the file
	symbol_table = read_file(fileName)
	print()

	# User prompt
	print("Enter either a prefex expression (* 3 * 2 1) or leave blank and press ENTER to quit.")
	print("WARNING: all expressions use integers and will not convert them to floats!")
	print()

	# Continuously will ask for the user to enter a derp command or ENTER to quit
	while True:
		prefix_exp = input("derp> ")
		
		# Chosen the quit
		if prefix_exp == "":
			break

		# Parses the derp command
		tree = parse(prefix_exp.split(" "))

		# Infix 
		print(f"Derping the infix expression: {infix(tree)}")

		# Evaluation
		print(f"Derping the evaluation: {evaluate(tree, symbol_table)}")

		print()
	
	print("Goodbye!")

if __name__ == "__main__":
	main()