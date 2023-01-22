"""
Test stack data structure.
file: test_stack.py
author: CS @ rit.edu
"""

from cs_stack import make_empty_stack, top, push, pop, size, is_empty

def main():
	"""
	main tests the stack implementation.
	"""
	# begin with an empty stack
	stackCh = make_empty_stack()
	print("Creating empty stack...")
	print("Stack empty?", True == is_empty(stackCh))
	print("Stack size is 0?",  0 == size(stackCh))   
	
	# add first element
	print("push A...")
	push(stackCh, 'A')
	print("Stack not empty?", False == is_empty(stackCh))
	print("Stack size is 1?", 1 == size(stackCh))   
	print("top is A?", 'A' == top(stackCh))
	
	# add second element
	print("push B...")
	push(stackCh, 'B')
	print("top is B?", 'B' == top(stackCh))
	
	# add third element
	print("push C...")
	push(stackCh, 'C')
	print("top is C?", 'C' == top(stackCh))
	print("Stack size is 3?", 3 == size(stackCh))   
	  
	# pop top element, C
	print("pop...")
	pop(stackCh)
	print("Stack not empty?", False == is_empty(stackCh))
	print("Stack size is 3?", 2 == size(stackCh))   
	print("top is B?", 'B' == top(stackCh))
	
	# add fourth element
	print("push D...")
	push(stackCh, 'D')
	print("top is D?", 'D' == top(stackCh))
	
	# Empty the stack
	print("Emptying the stack...")
	while not is_empty(stackCh):
		print("Top of stack:", top(stackCh))
		print("pop...")
		pop(stackCh)
	
if __name__ == "__main__":
	main()
