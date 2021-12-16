
import random
print("RULES ARE: \n"
		+"Rock vs paper = paper wins \n"
		+ "Rock vs scissor = Rock wins \n"
		+"paper vs scissor = scissor wins ")

while True:
	print("Enter your choice \n 1. Rock \n 2. paper \n 3. scissor ")
	
	
	ch = int(input("Choose  wisely: "))

	
	while ch > 3 or ch < 1:
		ch = int(input("enter valid input: "))
	if ch == 1:
		ch_name = 'Rock'
	elif ch == 2:
		ch_name = 'paper'
	else:
		ch_name = 'scissor'
		
	print("user choice is: " + ch_name)
	print("\nNow its computer's turn..........")
             

	
	comp_choice = random.randint(1, 3)
	
	
	while comp_choice == ch:
		comp_choice = random.randint(1, 3)

	
	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
		
	print("Computer's choice is: " + comp_choice_name )

	print(ch_name + " V/s " + comp_choice_name)

	
	if((ch == 1 and comp_choice== 2) or
	(ch == 2 and comp_choice ==1 )):
		print("paper wins :) ", end = "")
		result = "paper"
		
	elif((ch == 1 and comp_choice == 3) or
		(ch == 3 and comp_choice == 1)):
		print("Rock wins :)", end = "")
		result = "Rock"
	else:
		print("scissor wins :)", end = "")
		result = "scissor"

	
	if result == ch_name:
		print("-------------------------------------User wins----------------------------------")
	else:
		print("----------------------------------Computer wins ------------------------------------")
		
	print("Do you want to play again? (Y/N)")
	ans = input()


	if ans == 'n' or ans == 'N':
		break
print("\nThanks for playing")
