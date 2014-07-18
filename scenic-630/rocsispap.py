import random

again = "yes"
while (again == "yes"):
	player = raw_input("choose [rock/sissors/paper] :")

	while (player != "rock" and player != "sissors" and player != "paper"):
		print player
		player = raw_input("invalid choice. [rock/sissors/paper]:")

	computerInput = random.randint(0,2)
	if computerInput == 0:
		computerP = "rock"
	elif computerInput == 1:
		computerP = "sissors"
	elif computerInput == 2:
		computerP = "paper"
	else : 
		computerP = "This is an error"


	if (player == computerP):
		print "computer : ",computerP
		print "draw"

	elif (player == "rock"):
		if  (computerP == "sissors"):
			print "computer : ",computerP
			print "win"
		
		elif (computerP == "paper"):
			print "computer : ",computerP
			print "lose"
			
	elif (player == "sissors"):
		if  (computerP == "paper"):
			print "computer : ",computerP
			print "win"
			
		elif (computerP == "rock"):
			print "computer : ",computerP
			print "lose"
			
	elif (player == "paper"):
		if  (computerP == "rock"):
			print "computer : ",computerP
			print "win"
			
		elif (computerP == "sissors"):
			print "computer : ",computerP
			print "lose"
	again = raw_input("try again [yes/no]:")
	while (again != "yes" and again != "no"):
		again = raw_input("invalid choise. [yes/no] :")
	
	if (again == "no"):
		print "Bye"
		break



			



