'''
Ethan R Feldman
Train Run
CSCI 142 PSS 8
'''

from dataclasses import dataclass
from node_types import MutableNode
from linked_list_type import LinkedList, make_empty_list
from mutable_list import to_str, append, insert_before_index, remove_value

# Creates a TrainCar data class
@dataclass
class TrainCar:
	contents: str
	destination: str
	#capacity: int

# Initalizes stations with Rocherster (home)
stations = {"ROC": 0.0}

# Initalizes the train
train = make_empty_list()
train_speed = 60.0

LAYOVER = 0.5

# ~ #

def add_station(name, distance):
	'''
	Add a new stopping point named station to the train’s route.
	Parameters: name, distance
	Return: True/False
	'''

	# Manipulate the stations
	global stations
	
	# Checks to see if the distance can-be/is a float
	try:
		distance = float(distance)
	
	except:
		print("Distance of the station isn't an float")
		return False

	# Does some error handling before continueing
	if name is None or distance is None:
		print("Missing the name or distance of the station")
		return False
	
	elif isinstance(name, str) == False:
		print("Name of the station isn't a string")
		return False
	
	elif name in stations:
		print("Station has already been declared")
		return False
	
	elif distance <= 0.0:
		print("Distance of the new station can't be less than or equal to 0.0")
		return False
	
	else:
		
		# Checks if new station's distance matches that of another station
		for key in stations:
			if distance == stations[key]:
				print("Distance of the new station matches that of an other station, try again")
				return False

		stations[name] = distance
		print(f"Added a station '{name}' at a distance of '{distance}'")

		# Sorts the stations
		# Creates a new dictionary that goes through all values of the old dictionary and sorts them by value 
		# This is the most concise way to do this!
		stations = {key: value for key, value in sorted(stations.items(), key=lambda item: item[1])}
		return True


def set_speed(speed):
	'''
	Specify the speed for the train.
	Parameters: speed
	Return: True/False
	'''

	# Manipulate the train_speed
	global train_speed

	# Checks to see if the distance can-be/is a float
	try:
		speed = float(speed)
	except:
		print("The speed entered isn't an float")
		return False

	train_speed = speed
	print(f"Changed the train's speed to {train_speed} mph")
	return True


def add_car(contents, destination):
	'''
	Add a new traincar containing content destined for station.
	Parameters: contents, destination
	Return: True/False
	'''
	
	# Manipulate the train
	global train
	global stations

	# Does some error handling before continueing
	if destination is None or contents is None:
		print("Missing the destination or contents of the new traincar")
		return False
	
	elif isinstance(destination, str) == False:
		print("Destination of the traincar isn't a string")
		return False
	
	elif isinstance(contents, str) == False:
		print("Contents of the traincar isn't a string")
		return False
	
	elif destination not in stations:
		print("The destination listed for this traincar doesn't exist yet")
		return False
	
	elif destination == "ROC":
		print("The destination can't be the same as the inital station [ROC]")
		return False
	
	else:
		# Adds the train car to it's respective spot depending on where it is going
		if train.size == 0:
			append(train, TrainCar(contents, destination))
		
		else:
			# Compares the value of the station of the added car to the already know car's stations 
			node = train.head
			index = 0
			while node is not None and stations[node.value.destination] < stations[destination]:
				index += 1
				#print(index)
				#print("stations[destination]", stations[destination])
				#print("stations[node.value.destination]", stations[node.value.destination])
				node = node.next
			insert_before_index(train, TrainCar(contents, destination), index)

		print(f"Added a traincar to the train [contents: {contents}, destination: {destination}]")
		return True


def show_route():
	'''
	Print all the stations on the route.
	Parameters: none
	Return: True/False
	'''
	
	# Manipulate the stations
	global stations

	# Copies the stations dictionary
	tempStations = stations.copy()

	# Removes the first station to the route string
	tempStations.pop("ROC")
	route = "ROC"
	tempDis = 0.0

	# Adds to the route string dynamically with values and keys from tempStations
	for key, value in tempStations.items():
		route += f" -- {value-tempDis} --> {key}"
		tempDis = value-tempDis
	
	print(route)
	return True


def show_train():
	'''
	Print a list of the cars currently on the train and the train speed.
	Parameters: none
	Return: True/False
	'''
	
	# Manipulate the train
	global train
	global train_speed

	print(f"Engine speed: {train_speed}, Cars {to_str(train)}")
	return True


def help():
	'''
	Print a list of possible commands.
	Parameters: none
	Return: True/False
	'''
	
	# Shows all the commans
	print("----------------------------------------------------")
	print("List of commands:")
	print("    add_station <station (string)> <distance (float)>")
	print("    set_speed <speed (float)>")
	print("    add_car <contents (string)> <destination (string)>")
	print("    show_route")
	print("    show_train")
	print("    start")
	print("    quit")
	print("    help")
	print("----------------------------------------------------")

	return True


def start():
	'''
	Given the current route and train of cars, visit all the stations where the train has cars destined for them.
	Parameters: none
	Return: True/False
	'''
	
	# Manipulate these
	global stations
	global train
	global train_speed
	tempStaions = stations.copy()
	tempStaions.pop("ROC")
	removedTraincar = False
	timeTaken = 0.0
	tempDis = 0.0

	print("Starting train yard simulation...")
	
	for stop in tempStaions:
		print(f"Moving on to {stop}")

		# Removes the traincars that were destined at the stop
		node = train.head
		tempContents = ""
		while node is not None:
			if node.value.destination == stop:
				remove_value(train, node.value)
				removedTraincar = True
				tempContents = tempContents + node.value.contents + ", "
			node = node.next
		
		# Calculates the timeSpent, tempDis for the next station, and timeTaken
		timeSpent = round((tempStaions[stop]-tempDis)/train_speed, 2)
		tempDis = tempStaions[stop]-tempDis

		# Sees if a traincar was headed for the station in question
		# If so, it will unload the contents and the car
		# else, it will go through the station
		if removedTraincar == True:
			print("0.5 hours taken to separate traincars.")
			print(f"Unloading {tempContents}in {stop}.")
			timeSpent += 0.5
			removedTraincar = False
		else:
			print("No traincar headed for this station, the train will be passing through")
		
		# Adds up the timeTaken
		timeTaken += timeSpent

		print(f"This segment took {timeSpent} to travel.")

	# Total time
	print(f"Total time for trip was {timeTaken} hours.")

	return True


def quit():
	'''
	Terminates the program.
	Parameters: none
	Return: True/False
	'''
	
	print("Train yard simulation ending...")
	return True


def process_commands():
	'''
	It should go into a loop, reading a line of input until the quit command is entered.
	Parameters: none
	Return: none
	'''

	# Loops for user command input
	while True:

		# Splits the user's command
		command = input()
		command.lower()

		# If you don't put anything in it'll just keep going
		if command == "":
			commandParts = ["none"]
		else:
			commandParts = command.split()

		try:
			if commandParts[0] == "add_station":
				# Called the add_station command
				outcome = add_station(commandParts[1], commandParts[2])
				if outcome == False:
					print("Illegal use or form for this command.")
			
			elif commandParts[0] == "set_speed":
				# Called the set_speed command
				outcome = set_speed(commandParts[1])
				if outcome == False:
					print("Illegal use or form for this command.")
			
			elif commandParts[0] == "add_car":
				# Called the add_car command
				outcome = add_car(commandParts[1], commandParts[2])
				if outcome == False:
					print("Illegal use or form for this command.")
			
			elif commandParts[0] == "show_route":
				# Called the show_route command
				outcome = show_route()
				if outcome == False:
					print("Illegal use or form for this command.")
			
			elif commandParts[0] == "show_train":
				# Called the show_train command
				outcome = show_train()
				if outcome == False:
					print("Illegal use or form for this command.")
			
			elif commandParts[0] == "start":
				# Called the start command
				outcome = start()
				if outcome == False:
					print("Illegal use or form for this command.")
			
			elif commandParts[0] == "quit":
				# Called the quit command
				outcome = quit()
				if outcome == False:
					print("Illegal use or form for this command.")
				else:
					# Breaks the loop
					break
			
			elif commandParts[0] == "help":
				# Called the quit command
				outcome = help()
				if outcome == False:
					print("Illegal use or form for this command.")

			elif commandParts[0] == "none":
				# No command
				pass

			else:
				# Messed up the command
				print("Illegal command name.")
				
		except:
			# Messed up the command
			print("Illegal use or form for this command.")
		
		print()


def main():
	'''
	User imput here, defined in the pass prompt
	'''

	# Initial message
	print("Welcome to GenericMetro.co, before we start remember to enter 'help' for command information!")
	print("    There is no need to enter a starting station, 'ROC' at distance 0 has already been added.")
	print("    The train has a default speed of 60.0 mph")
	help()
	print()

	# Loop
	process_commands()
	
if __name__ == "__main__":
	main()