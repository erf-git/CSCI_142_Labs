'''
Ethan R Feldman
Tools
CSCI 141 Lab 5
'''

# Imported needed libraries
import math


# ~ #


def find_median(lst):
	'''
	Gets the median value of the list
	Precondition: sorted list (lst)
	Postcondition: returns the median of the lst
	'''
	
	# Check if the list is even or odd
	if len(lst)%2 == 0:
		# Gets the 2 middle indexes
		indexA = len(lst)//2
		indexB = indexA-1
		
		# Returns floor division by 2
		return (lst[indexA]+lst[indexB])//2
	
	else:
		# Gets in middle index
		index = len(lst)//2

		# Returns the middle item
		return lst[index]


def find_sum(lst,median):
	'''
	Finds the sum of all the distances from the median
	Precondition: sorted list (lst)
	Postcondition: sum of all distances
	'''
	
	# Sums the distances from the median point
	sum = 0
	for n in lst:
		distance = abs(median-n)
		sum += distance

	#print(median)
	#print(sum)

	# Returns the sum
	return sum


def read_location_file(file):
	'''
	Reads the incoming file and returns a sorted list of locations
	Precondition: file name (file)
	Postcondition: returns the list (newLst)
	'''

	# Opens the file safely
	with open(file, "r") as f:

		# Puts each line in the tempList as strings
		tempLst = f.read().splitlines()

		# Empty list (lst)
		newLst = []

		# Goes through every item in the tempList and add only the numbers from each line to the newLst
		for item in tempLst:
			stringList = item.split()
			newLst.append(int(stringList[1]))

		#print(tempLst)
		#print(newLst)

	# Returns the new list
	return newLst


#print(read_location_file("test_data_writeup.txt"))
#print(find_median(read_location_file("test_data_writeup.txt")))
#print(find_sum(read_location_file("test_data_writeup.txt")))