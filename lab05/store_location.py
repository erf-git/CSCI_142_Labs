'''
Ethan R Feldman
Store Location
CSCI 141 Lab 5
'''

# Imported needed libraries
import tools
import quick_sort
import quick_select
import select_median
import time


# ~ #


def main():
	'''
	Contains the user prompts to find the best location of the store
	'''

	# Asks for the file name
	fileName = input("Enter data file name: ")

	# Gets the lst from the file, then 
	lst = tools.read_location_file(fileName)

	# Tracks the time it takes with sorting
	# Sort the list with quick sort and finds the median for the optimum new store location
	start = time.perf_counter()
	sortedList = quick_sort.quick_sort(lst)
	median = tools.find_median(sortedList)
	elapsedSorted = time.perf_counter()-start

	# Tracks the time it takes without sorting
	# Using quick select finds the median for the optimum new store location
	start = time.perf_counter()
	median = select_median.find_median(lst)
	elapsedUnsorted = time.perf_counter()-start

	# Prints results
	print(f"Optimum new store location: {median}")

	# Gets the sum of all the distances between the new store location and the other buildings
	sum = tools.find_sum(lst,median)
	print(f"Sum of distances to the new store: {sum}")
	
	# Prints the elapsed time for both methods
	print(f"Sorted elapsed time: {elapsedSorted}")
	print(f"Unsorted elapsed time: {elapsedUnsorted}")


if __name__ == "__main__":
	main()