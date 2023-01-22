'''
Ethan R Feldman
Moving
CSCI 141 PSS 6
'''

from dataclasses import dataclass

@dataclass
class Boxes:
	id : int
	capacity: int
	items: list
	#full: bool

# ~ #

def read_file(fileName):
	'''
	Reads the file data
	Postcondition: file name (fileName)
	Precondition: boxes data, and list of items data
	'''

	# Defines some lists
	lines = []
	boxes = []
	list_of_items = []
	
	# Opens the file and reads every file into the lines list
	with open(fileName) as f:
		lines = f.read().splitlines()

	if len(lines) == 0:
		return False

	# Box capacity defined in line 1, plus an additional box for left overs
	boxes = lines[0].split(" ")
	for x in range(0,len(boxes)):
		boxes[x] = int(boxes[x])
	boxes.append(0)
	
	# All the item info comes in the lines later
	for x in range(1,len(lines)):
		text = lines[x].split(" ")
		item = [text[0], int(text[1])]
		list_of_items.append(item)
		
	# Returns boxes and list of items
	return boxes, list_of_items

def make_box(id, capacity):
	'''
	Makes an empty box with the id (id) and capacity (capacity) with no items in it
	Precondition: capacity (capacity)
	Postcondition: returns the newly made box
	'''

	return Boxes(id, capacity, [])


def roomiest(newStorage,newData):
	'''
	Sort all items by decreasing weight. Iterate
	through the items one by one, from largest weight to smallest. For each item, identify
	the box with the greatest remaining allowed weight that can support the item, and
	place the item in that box. Ties can be broken arbitrarily. If no box can support
	the item, it is not placed in any box. Continue until all items have been considered,
	and either placed in a box or left out.
	Precondition: storage list (newStorage), data items list (newData)
	Postcondition: new storage (newStorage)
	'''
	
	# Finds the greatest weight item
	greatestItem = newData[0]
	for element in newData:
		if element[1] > greatestItem[1]:
			greatestItem = element
	#print(greatestItem)
	
	# Finds the greatest capacity box
	greatestBox = newStorage[-1]
	for element in newStorage:
		if element.capacity > greatestBox.capacity:
			greatestBox = element
	#print(greatestBox)
	
	# Finds the index of the greatest box in the storage list
	index = newStorage.index(greatestBox)

	# Adds the item to the box and subtracs it's weight from the capacity
	newStorage[index].capacity -= greatestItem[1]
	if newStorage[index].capacity >= 0:
		newStorage[index].items.append(greatestItem)
		
		# Removes greatest item in the d list
		newData.remove(greatestItem)

		#print(newStorage[index])
		#print()

		# Checks if there are no more items in the data list
		if len(newData) != 0:
			# Calls the function again recursively
			roomiest(newStorage,newData)

	else:
		# This means that there is no more spaces in all the boxes so it undoes subtracting the capacity
		newStorage[index].capacity += greatestItem[1]

		# All remaining items go into the left over box
		newStorage[-1].items += newData

		#print(newStorage[-1])
		#print()
	
	# Returns the final storage
	return newStorage


def func(e):
	'''
	Used for a sorting key function
	Sorts by box capacity
	'''
	return e.capacity

def tightest_fit(newStorage,newData):
	'''
	Sort all items by decreasing weight. Iterate
	through the items one by one, from largest weight to smallest. For each item, identify
	the box with the least remaining allowed weight that can support the item, and place
	the item in that box. Ties can be broken arbitrarily. If no box can support the item,
	it is not placed in any box. Continue until all items have been considered, and either
	placed in a box or left out.
	Precondition: storage list (newStorage), item data (newData)
	Postcondition: new storage (newStorage)
	'''
	
	# Sorts the boxes by capacity from least to greatest
	newStorage.sort(key=func)
	
	# Finds the greatest weight item
	greatestItem = newData[0]
	for element in newData:
		if element[1] > greatestItem[1]:
			greatestItem = element
	#print(greatestItem)

	for box in newStorage:
		if box.capacity >= greatestItem[1]:
			#print(greatestItem, " in ", box)
			
			# Adds the item to the box
			box.capacity -= greatestItem[1]
			box.items.append(greatestItem)
		
			# Removes greatest item in the d list
			newData.remove(greatestItem)

			break

	# As long as there are items left in d, it will continue to recursively put items in boxes
	if greatestItem in newData:
		# If there are left over items in d, add them to the left overs
		newStorage[0].items += newData
	else:
		tightest_fit(newStorage,newData)

	# Returns the final storage
	return newStorage


def func2(e):
	'''
	Used for a sorting key function
	Sorts by item weight
	'''
	return e[1]

def one_box_at_a_time(newStorage,newData):
	'''
	Sort all items by decreasing weight.
	Fill the boxes one by one. For each box, iterate through all remaining items (not
	yet placed in a previously considered box) one by one. If there is room for an item
	to be placed in the current box, do so.
	Precondition: storage list (newStorage), item data (newData)
	Postcondition: new storage (newStorage)
	'''

	# Sorts the data from greatest to least weight
	newData.sort(reverse=True,key=func2)

	x = 0
	while len(newData) > 0:
		#print(newData)
		#print(x)
		#Goes through all the boxes
		for box in newStorage:
			
			# Gets the item
			item = newData[x]
			#print(item)
			if box.capacity >= item[1]:
				#print(item, " was added to storage ", box.id)
				
				# Adds the item to the box
				box.capacity -= item[1]
				box.items.append(item)

				# Removes greatest item in the d list
				newData.remove(item)

		# Can't fit in the box that it was on
		newStorage[3].items.append(item)
		#print(item, " wasn't added")

		# Removes greatest item in the d list
		newData.remove(item)

	return newStorage


def init_dataclass(fileName):
	'''
	I didin't know that once you make a dataclass, the class will carry over to everything even when you change values in it.
	So this just downloads the data over and over again
	Not ideal, but I don't know how to fix this...
	Precondition: file name (fileName)
	Postcondition: storage boxes (storage), item data (data)
	'''

	# Gets the file data (boxes capacity = b, and item data = data)
	b,data = read_file(fileName)

	# Ends program if empty file
	if b == False or data == False:
		print("Empty file...")
		exit()

	# Creats a storage dictionary to contain the boxes
	# Makes each box with a loop
	storage = []
	for x in range(0,len(b)):
		storage.append(make_box(x,b[x]))
		#print(storage[x])

	return storage,data

def func3(e):
	'''
	Used for a sorting key function
	Sorts by box id
	'''
	return e.id

def main():
	'''
	Does what the lab outlines
	'''
	
	# Prompts the user for a file name
	fileName = input("Enter data file name: ")
	print()
	
	# Gets the data from the file
	storage,data = init_dataclass(fileName)

	# I need to store the original capacity data in order for it to be used later...
	capacities = []
	for box in storage:
		capacities.append(box.capacity)

	# Gets your sorted boxes 
	storageRoomiest = roomiest(storage,data)
	storageRoomiest.sort(key=func3)

	print("Results from Greedy Strategy 1...")

	# Prints the data in box id order
	for x in range(0,len(storageRoomiest)-1):
		print(f"Box {x+1} of a weight of {capacities[x]} contains:")
		for item in storageRoomiest[x].items:
			print(f"{item[0]} of weight {item[1]}")
	if len(storageRoomiest[len(storageRoomiest)-1].items) > 0:
		# This prints the last box which contains left overs
		print(f"Left overs:")
		for item in storageRoomiest[len(storageRoomiest)-1].items:
			print(f"{item[0]} of weight {item[1]}")
	print()
	
	# Gets the data from the file
	storage2,data2 = init_dataclass(fileName)

	# I need to store the original capacity data in order for it to be used later...
	capacities = []
	for box in storage2:
		capacities.append(box.capacity)

	# Gets your sorted boxes 
	storageTightestFit = tightest_fit(storage2,data2)
	storageTightestFit.sort(key=func3)
	
	print("Results from Greedy Strategy 2...")

	# Prints the data in box id order
	for x in range(0,len(storageTightestFit)-1):
		print(f"Box {x+1} of a weight of {capacities[x]} contains:")
		for item in storageTightestFit[x].items:
			print(f"{item[0]} of weight {item[1]}")
	if len(storageTightestFit[len(storageTightestFit)-1].items) > 0:
		# This prints the last box which contains left overs
		print(f"Left overs:")
		for item in storageTightestFit[len(storageTightestFit)-1].items:
			print(f"{item[0]} of weight {item[1]}")
	print()

	# Gets the data from the file
	storage3,data3 = init_dataclass(fileName)

	# I need to store the original capacity data in order for it to be used later...
	capacities = []
	for box in storage3:
		capacities.append(box.capacity)

	# Gets your sorted boxes 
	storageOAAT = one_box_at_a_time(storage3,data3)
	storageOAAT.sort(key=func3)
	
	print("Results from Greedy Strategy 3...")

	# Prints the data in box id order
	for x in range(0,len(storageOAAT)-1):
		print(f"Box {x+1} of a weight of {capacities[x]} contains:")
		for item in storageOAAT[x].items:
			print(f"{item[0]} of weight {item[1]}")
	if len(storageOAAT[len(storageOAAT)-1].items) > 0:
		# This prints the last box which contains left overs
		print(f"Left overs:")
		for item in storageOAAT[len(storageOAAT)-1].items:
			print(f"{item[0]} of weight {item[1]}")
	print()
	

if __name__ == "__main__":
	main()

