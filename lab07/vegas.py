'''
Ethan R Feldman
Vegas 
CSCI 141 PSS 7
'''

from cs_queue import make_empty_queue, is_empty, front, back, enqueue, dequeue
from cs_stack import make_empty_stack, top, push, pop, size, is_empty
import random

# ~ #

def init_deck(size):
	'''
	Creates and returns a new deck of cards of a given size, using an appropriate data structure.
	Precondition: deck size (size)
	Postcondition: return deck
	'''

	# Makes the deck with a queue with the amount of cards equal to the size variable
	deck = make_empty_queue()
	for x in range(1,size+1):
		enqueue(deck, x)

	# Returns the made deck 
	return deck

def random_draw(deck):
	'''
	Takes an argument of a deck of cards and chooses and returns a randomly-selected card as described in problem solving.
	Precondition: deck (deck)
	Postcondition: returns randomly chosen card
	'''

	# Shuffles the deck a rand amount of times (0 to deck-size)
	for x in range(0,random.randint(0,deck.size)):
		card = dequeue(deck)
		enqueue(deck,card)

	# Returns a card form the top and removes it from the deck
	return dequeue(deck)

def play_game(size):
	'''
	Takes an argument of a deck of cards and uses random_draw to deal out all of the cards one at a time, printing the card dealt each time.
	Precondition: deck size (size)
	Postcondition: returns size of victory 
	'''

	# Creates the deck with a size of size
	deck = init_deck(size)
	#print(f"Created a deck of {deck.size} cards")

	# Creates the discard piles
	discard_A = make_empty_stack()
	#print(f"Created discard pile A")

	# Creates the discard piles
	discard_B = make_empty_stack()
	#print(f"Created discard pile B")

	# Creates the victory piles
	victory = make_empty_stack()
	cardInVictory = 0
	#print(f"Created victory pile")

	#print()

	# Gets the first cards, this one will determind where the other cards go
	initialCard = random_draw(deck)
	#print(f"Initial card draw: {initialCard}")

	# If initialCard is 1, we can place it right on victory
	if initialCard == 1:
		push(victory,initialCard)
		cardInVictory = initialCard
		#print("Added initialCard to victory pile")
	else:
		push(discard_A,initialCard)
		#print("Added initialCard to discard pile A")
	
	#print()

	# Pointer divides discard_A and discard_B by the cards that are bellow or above the pointer
	pointer = initialCard

	# Sorts the other cards into discard_A or discard_B depending on if they are greater or less than initialCard
	for x in range(0,deck.size):
		randomCard = random_draw(deck)

		# victory contains cards 1 to deck-size
		# discard_A contains cards less than initialCard
		# discard_B contains cards greater than initalCard
		if randomCard-1 == cardInVictory:
			push(victory,randomCard)
			cardInVictory = randomCard
			#print(f"Random card {x+2} delt: {randomCard}, adding it to vitory")
		elif randomCard < pointer:
			push(discard_A,randomCard)
			pointer = randomCard
			#print(f"Random card {x+2} delt: {randomCard}, adding it to discard_A")
		else:
			push(discard_B,randomCard)
			#print(f"Random card {x+2} delt: {randomCard}, adding it to discard_B")
	#print()

	# Use cards from discard_A to add to victory in ascending order
	for x in range(0,discard_A.size):
		#print(f"Top of discard_A: {top(discard_A)}")
		#print(f"Top of cardInVictory: {cardInVictory}")
		
		# As long as the card being added from discard_A is 1 above the card at the top of the victory
		if top(discard_A)-1 == cardInVictory:
			card = pop(discard_A)
			push(victory,card)
			cardInVictory = card
	
	#print(f"discard_A: {discard_A}")
	#print(f"discard_B: {discard_B}")
	#print(f"victory: {victory}")
	#print()

	return victory.size

def main():
	'''
	Prompts the user for the number of cards in the deck, creates a deck of the given size, and calls play game appropriately.
	'''

	# Asks for the deck size
	ans = input("What size deck do you want? ")
	# If you don't input the deck size in correctly, it will default to 8
	try:
		n = int(ans)
	except:
		n = 10
		print("Your input didn't go through, defaulting to a deck size of 10...")
	print()

	# Asks for the number of games
	ans = input("How many games do you want to play? ")
	# If you don't input the number of games in correctly, it will default to 8
	try:
		repeat = int(ans)
	except:
		repeat = 10000
		print("Your input didn't go through, defaulting to 10000 games...")
	print()

	# This will store the results from each game
	counter = 0
	maxi = 0
	mini = 0

	# Plays the game repeat number of times
	for x in range(0,repeat):
		r = play_game(n)

		# Counts up the results
		counter = counter + r

		# Finds the greatest game
		if maxi < r:
			maxi = r
		
		# Finds the least game
		if mini > r:
			mini = r
	
	# Prints the average wins from this strategy
	result = counter/repeat
	print(f"Average number of cards in victory pile from {repeat} games: {result+1}")
	print(f"Greatest number of cards in victory pile from {repeat} games: {maxi}")
	print(f"Least number of cards in victory pile from {repeat} games: {mini}")
	print()

if __name__ == "__main__":
	main()