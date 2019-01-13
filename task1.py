from Crypto.Hash import SHA256
#SHA256.new('abc').hexdigest()
from Crypto.Cipher import AES
import os
from binascii import hexlify, unhexlify

import time

#then  =  time.time()
#now =  time.time()

#print("It took ", now-then, "seconds to complete the operation")
#links 
#https://techtutorialsx.com/2018/04/09/python-pycrypto-using-aes-128-in-ecb-mode/ 
#https://stackoverflow.com/questions/46904355/aes-128-cbc-decryption-in-python


def aes():

	print("Press 1 for ECB mode")
	print("Press 2 for CBC mode")

	command = int(input())
	if(command == 1):
		print("Press 1 for key length 128 bits")
		print("Press 2 for key length 256 bits")
		l = int(input())
		if(l==1):
			ecb128()
		elif(l==2):
			ecb256()


	elif(command==2):
		print("Press 1 for key length 128 bits")
		print("Press 2 for key length 256 bits")
		l = int(input())
		if(l==1):
			cbc128()
		elif(l==2):
			cbc256() 



def ecb128():
	key = 'abcdefghijklmnop'

	cipher = AES.new(key, AES.MODE_ECB)
	print("Enter your message:")
	plain_text = input()
	l = len(plain_text)
	plain_text = padding(plain_text)
	#print(len(plain_text))

	then  =  time.time()
	msg =cipher.encrypt(plain_text)
	#print (type(msg))
	now =  time.time() 
	print("Encrypted text: ", str(msg).encode("utf-8"))
	 
	decipher = AES.new(key, AES.MODE_ECB)
	text = decipher.decrypt(msg)
	print("Decrypted text: ",text[0:l])


	print("It took ", now-then, "seconds to complete the operation")


def ecb256():


	key2 = 'abcdefghijklmnop1234569874123658'
	cipher = AES.new(key2, AES.MODE_ECB)
	print("Enter your message:")
	plain_text = input()
	l = len(plain_text)
	plain_text = padding(plain_text)
	#print(len(plain_text))
	then  =  time.time()
	msg =cipher.encrypt(plain_text)
	#print (type(msg))
	now =  time.time()
	print("Encrypted text: ", str(msg).encode("utf-8"))
	 
	decipher = AES.new(key2, AES.MODE_ECB)
	text = decipher.decrypt(msg)
	print("Decrypted text: ",text[0:l])

	print("It took ", now-then, "seconds to complete the operation")


def cbc128():
	key = 'abcdefghijklmnop'

	IV = os.urandom(16)

	cipher = AES.new(key, AES.MODE_CBC, IV)
	print("Enter your message:")
	plain_text = input()
	l = len(plain_text)
	plain_text = padding(plain_text)
	#print(len(plain_text))
	then  =  time.time()
	msg =cipher.encrypt(plain_text)
	#print (type(msg))
	now =  time.time()
	print("Encrypted text: ", str(msg).encode("utf-8"))
	 
	decipher = AES.new(key, AES.MODE_CBC, IV)
	text = decipher.decrypt(msg)
	print("Decrypted text: ",text[0:l])

	
	print("It took ", now-then, "seconds to complete the operation")
def cbc256():
	key2 = 'abcdefghijklmnop1234569874123658'

	IV = os.urandom(16)

	cipher = AES.new(key2, AES.MODE_CBC, IV)
	print("Enter your message:")
	plain_text = input()
	l = len(plain_text)
	plain_text = padding(plain_text)
	#print(len(plain_text))
	then  =  time.time()
	msg =cipher.encrypt(plain_text)
	#print (type(msg))
	now =  time.time()
	print("Encrypted text: ", str(msg).encode("utf-8"))
	 
	decipher = AES.new(key2, AES.MODE_CBC, IV)
	text = decipher.decrypt(msg)
	print("Decrypted text: ",text[0:l])
	

	print("It took ", now-then, "seconds to complete the operation")
def padding(x):
	l = len(x)
	a = 16 - l%16
	for i in range(a):
		x = x+ '0'

	return x
