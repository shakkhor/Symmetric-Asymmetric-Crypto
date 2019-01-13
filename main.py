from task1 import aes
from task2 import rsa 
from lab6task3 import signature
from lab6Task4 import sha256 

welcome = 0
while(1):
	print('\n\n')
	if(welcome == 0):
		print("=======================Welcome=======================\n")
		welcome = 2

	key = 0
	print("Press 1 for AES encryption and decryption")
	print("Press 2 for RSA encryption and decryption")
	print("Press 3 for RSA Signature")
	print("Press 4 for SHA-256")
	print("Press 0 to end the progam")

	key = int(input())

	if(key == 1):
		aes()
	elif(key == 2):
		rsa()
	elif(key==4):
		sha256()
	elif(key==3):
		signature()	
	elif(key == 0):
		break
	else:
		print("Invalid input\n Run the program again\n")
		break







