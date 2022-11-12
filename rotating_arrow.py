from os import system
from time import sleep


while(True):

	system('cls')
	
	print("\n"*4)
	for i in range(1,6):
		print("  "*15+"* "*i)	
	
	print (" "*20+"* "*11)

	for i in range(5,0,-1):
		print("  "*15+"* "*i)
	
	
	sleep(0.3)
	system('cls')
	
	print("\n"*9)
	for i in range(1,6):
		print("  "*10+"*")
	

	for i in range(11,0,-2):
		print(" "*10+" "*(11-i)+"* "*i)

	sleep(0.3)	
	system('cls')

	print("\n"*4)
	for i in range(1,6):
		print("  "*(6-i)+"* "*i)
	
	print ("* "*11)

	for i in range(5,0,-1):
		print("  "*(6-i)+"* "*i)

	sleep(0.3)	
	system('cls')

	for i in range(1,12,2):
		print(" "*10+" "*(11-i)+"* "*i)
	
	for i in range(1,6):
		print("  "*10+"*")

	sleep(0.3)	
