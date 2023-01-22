'''
Ethan R Feldman
Select Median
CSCI 141 Lab 5

To be honost, this makes more sense in a program called "quick_select",
so if you need more detail go there.
'''

# Imports quick_select
import quick_select

"""
Quick select file

def quick_select(L,k):
	'''
	Given k, find the item in k-index if the list was sorted
	Precondition: unsorted list (L), k'th index
	Postcondition: item that would be in sortedList[k]
	'''

	# Follows the prompt given in the assignment
	if len(L) != 0:
		# Defines the variables
		pivot = L[len(L)//2]
		smallerL = []
		largerL = []
		counter = 0

		# Collects data for smaller and larger lists
		# Collects data for counter
		for n in L:
			if n<pivot:
				smallerL.append(n)
			elif n==pivot:
				counter += 1
			elif n>pivot:
				largerL.append(n)
		
		# Defines m
		m = len(smallerL)

		# Recursion step
		if k>=m and k<(m+counter):
			return pivot
		elif m>k:
			return quick_select(smallerL,k)
		else:
			return quick_select(largerL,k-m-counter)
"""


def find_median(L):
	'''
	Finds the median value without sorting the list
	Precondition: unsorted list (L)
	Postcondition: returns median
	'''

	if len(L)%2 == 0:
		# Gets the 2 middle indexes
		indexA = len(L)//2
		indexB = indexA-1

		# Finds the 2 middle elements
		valueA = quick_select.quick_select(L,indexA)
		#print(valueA)
		valueB = quick_select.quick_select(L,indexB)
		#print(valueB)

		# Returns the average value between the 2 middle values
		return (valueA+valueB)//2
	else:
		# Gets the middle indexes
		k = len(L) // 2

		# Returns the middle value
		return quick_select.quick_select(L,k)

