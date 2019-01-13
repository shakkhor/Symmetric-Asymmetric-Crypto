#https://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python
	#RSA encryption and decryption


import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import time

#then  =  time.time()
#now =  time.time()

#print("It took ", now-then, "seconds to complete the operation")

def rsa():	
	
	

	random_generator = Random.new().read
	key = RSA.generate(1024, random_generator) #generate pub and priv key
	f = open ('keyfile', 'w')
	f.write(str(key))
	f.close()



	publickey = key.publickey() # pub key export for exchange
	

	print("Enter your message:")
	plain_text = input()
	
	f = open ('message.txt', 'w')
	f.write(str(plain_text)) #write ciphertext to file
	f.close()



	then  =  time.time()
	encrypted = publickey.encrypt(str(plain_text).encode('utf-8'), 32)
	#message to encrypt is in the above line 'encrypt this message'

	print ('Encrypted message:', encrypted) #ciphertext
	f = open ('encryption.txt', 'w')
	f.write(str(encrypted)) #write ciphertext to file
	f.close()

	#decrypted code below

	f = open('encryption.txt', 'r')
	message = f.read()


	decrypted = key.decrypt(ast.literal_eval(str(message)))
	now =  time.time()

	print("")
	print ('Decrypted message:-> ', decrypted)
	print("It took ", now-then, "seconds to complete the operation")

	f = open ('encryption.txt', 'w')
	f.write(str(message))
	f.write(str(decrypted))
	f.close()