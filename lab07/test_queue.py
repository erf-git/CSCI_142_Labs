"""
Test queue implementation.
file: test_queue.py
author: CS @ rit.edu
"""

from cs_queue import make_empty_queue, is_empty, front, back, enqueue, dequeue

def main():
	"""
	test the cs_queue implementation
	"""

	# begin with an empty queue
	queueCh = make_empty_queue()
	print("Creating empty queue...")
	print("Queue empty?", True == is_empty(queueCh))
	print("Queue size is 0?", 0 == queueCh.size)
	
	
	# add first element
	print("enqueue A...")
	enqueue(queueCh, 'A')
	print("Queue not empty?", False == is_empty(queueCh))
	print("Queue size is 1?", 1 == queueCh.size)
	print("front is A?", 'A' == front(queueCh))
	print("back is A?", 'A' == back(queueCh))
	
	# add second element
	print("enqueue B...")
	enqueue(queueCh, 'B')
	print("front is A?", 'A' == front(queueCh))
	print("back is B?", 'B' == back(queueCh))
	
	# add third element
	print("enqueue C...")
	enqueue(queueCh, 'C')
	print("Queue size is 3?", 3 == queueCh.size)
	print("front is A?", 'A' == front(queueCh))
	print("back is C?", 'C' == back(queueCh))
	
	# dequeue front element, A
	print("dequeue...")
	dequeue(queueCh)
	print("Queue not empty?", False == is_empty(queueCh))
	print("Queue size is 2?", 2 == queueCh.size)
	print("front is B?", 'B' == front(queueCh))
	print("back is C?", 'C' == back(queueCh))
		
	# add fourth element
	print("enqueue D...")
	enqueue(queueCh, 'D')
	print("front is B?", 'B' == front(queueCh))
	print("back is D?", 'D' == back(queueCh))
	
	# Empty the queue
	print("Emptying the queue...")
	while not is_empty(queueCh):
		print("Front of stack:", front(queueCh))
		print("Back of stack:", back(queueCh))
		print("dequeue...")
		dequeue(queueCh)
 
 
if __name__ == "__main__":
	main()
