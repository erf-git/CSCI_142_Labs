'''
Ethan R Feldman
Quick Select
CSCI 141 Lab 5
'''


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


def quick_select_sort(L):
	'''
	Sorts the list using quick select algorthm
	Precondition: unsorted list (L)
	Postcondition: sorted list (lst)
	'''

	# Defines an empty list
	lst = []

	# Uses every number of k to sort the list
	for k in range(0,len(L)):
		lst.append(quick_select(L,k))

	# Returns the sorted list
	return(lst)


def quick_select_median(L):
	'''
	Finds the median value without sorting the list
	Precondition: unsorted list (L)
	Postcondition: median
	'''

	if len(L)%2 == 0:
		# Gets the 2 middle indexes
		indexA = len(L)//2
		indexB = indexA-1

		# Finds the 2 middle elements
		valueA = quick_select(L,indexA)
		#print(valueA)
		valueB = quick_select(L,indexB)
		#print(valueB)

		# Returns the average value between the 2 middle values
		return (valueA+valueB)//2
	else:
		# Gets the middle indexes
		k = len(L) // 2

		# Returns the middle value
		return quick_select(L,k)


if __name__ == "__main__":
	print(quick_select_median([10,2,1,3,5,3,7,0]))