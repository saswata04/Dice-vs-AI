import random
import os
import time
choice_AI=0
		
def choices_AI():
	global choice_AI
	try:
		choice_AI=input("Choice: ")
		if(choice_AI != "r" and choice_AI != "q"):
			raise Exception
	except:
		print("Invalid Input\nTry Again")
		choices_AI()

def logic_AI():
	global choice_AI
	for i in range(1,3):
		if i==1:
			print(">>>>Your turn")
			print("Press 'r' to roll the dice")
			print("Press 'q' to quit")
			choices_AI()
			if(choice_AI=='r'):
				print("<<<Rolling the dice>>>")
				time.sleep(4)
				print(">>",random.randint(1,6),"<<")
				print()
			else:
				os._exit(0)
		else:
			print(">>>>My turn")
			print("<<<Rolling the dice>>>")
			time.sleep(4)
			print(">>",random.randint(1,6),"<<")
			print()
			logic_AI()
print("<<<<<<<<<< The Dice >>>>>>>>>>")
logic_AI()