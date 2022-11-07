import replit
import random
import art
from GameData import data
should_contnue = True
corect_answer = 0
while should_contnue:
	print(art.logo)
	if corect_answer >= 1 :
		print(f"you are right your point is  {corect_answer}")

	choice1 = random.choice(data)
	keys = list(choice1)
	#del keys[1]
	print(f"compare A: ")
	for item in keys :
		print({choice1.get(item)})
	chice2 = random.choice(data)

	keys2 = list(chice2)
	#del keys2[1]
	print(f"compare B: ")
	for item in keys2 :
		print({chice2.get(item)})
	user_choice = input("Who has more follewers ? Type A or  B or E equal  : ")
	if user_choice == "A" :
		if choice1["follower_count"] > chice2["follower_count"] :
			corect_answer +=1
			replit.clear()
		else :
			print(f"you lose :( , your total score is {corect_answer}")
			break

	elif user_choice == "B" :
		if chice2["follower_count"] > choice1 ["follower_count"] :
			corect_answer +=1
			replit.clear()
		else :
			print(f"you lose :( , your total score is {corect_answer}")
			break
	elif user_choice == "E" :
		if chice2["follower_count"] == choice1 ["follower_count"] :
			corect_answer +=1
			replit.clear()
		else :
			print(f"you lose :( , your total score is {corect_answer}")
			break