
print("for scientific calculator press 1 ")
print("for Programmer calculator press 2 ")

mode=input("Mode = ")
mode=int(mode)

if mode == 1 :
	snum1=input("number 1 = ")
	snum2=input("number 2 = ")
	soperation=input("enter the operation (+ , - , / , * ) : ")
	
	
	if soperation == '+' :
		print(" num1 + num2 = ",int(snum1)+int(snum2))
		
	elif soperation == '-' :
		print(" num1 - num2 = ",int(snum1)-int(snum2))
	
	elif soperation == '/' :
		print(" num1 / num2 = ",int(snum1)/int(snum2))
		
	elif soperation == '*' :
		print(" num1 * num2 = ",int(snum1)*int(snum2))
		
	else :
		print ("wrong input")
	
elif mode == 2 :
	print("for normal operations press 0 ")
	print("for bitwise operations press 1 ")
	print("for number transormation press 2 ")
	operation = input()
	operation=int(operation)
	
	if operation == 0 :
	
		pnum1=input("number 1 = ")
		pnum2=input("number 2 = ")
		poperation=input("enter the operation (+ , - , / , * ) : ")
	
	
		if poperation == '+' :
			result = int(pnum1)+int(pnum2)
		
		elif poperation == '-' :
			result = int(pnum1)-int(pnum2)
	
		elif poperation == '/' :
			result = int(pnum1)/int(pnum2)
			result=int(result)
		
		elif poperation == '*' :
			result = int(pnum1)*int(pnum2)
		
		else :
			print ("wrong input")
			
		print("result in decimal     = ", result)
		print("result in binary      = ", bin(result))
		print("result in octal       = ", oct(result))
		print("result in hexadecimal = ", hex(result))
	
	if operation == 1 :
		
		poperation=input("enter the operation (& , | , ^ , ~ ) : ")
		
		if poperation == '&' :
			pnum1=input("number 1 = ")
			pnum2=input("number 2 = ")
			result = int(pnum1)&int(pnum2)
		
		elif poperation == '|' :
			pnum1=input("number 1 = ")
			pnum2=input("number 2 = ")
			result = int(pnum1)|int(pnum2)
	
		elif poperation == '^' :
			pnum1=input("number 1 = ")
			pnum2=input("number 2 = ")
			result = int(pnum1)^int(pnum2)
		
		elif poperation == '~' :
			pnum1=input("number 1 = ")
			result = ~int(pnum1)
		
		else :
			print ("wrong input")
			
		print("result in decimal     = ", result )
		print("result in binary      = ", bin(result))
		print("result in octal       = ", oct(result))
		print("result in hexadecimal = ", hex(result))
	
		
	if operation == 2 :
	
		pnum1=input("number in decimal = ")
		poperation=input(" enter 0 for binary \n enter 1 for octal \n enter 2 for hexadecimal \n ")
	
		poperation=int(poperation)
		pnum1=int(pnum1)
	
		if poperation == 0 :
			print("number in binary = ",bin(pnum1))
	
		elif poperation == 1 :
			print("number in octal = ",oct(pnum1))
	
		elif poperation == 2 :
			print("number in hexadecimal = ",hex(pnum1))
		
		
