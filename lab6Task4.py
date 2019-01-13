#https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

import hashlib
import time

def sha256():

	inputFile = input("Enter the name of the file: ")
	openedFile = open(inputFile)
	readFile = openedFile.read()

	#md5Hash = hashlib.md5(readFile.encode('utf-8'))
	#md5Hashed = md5Hash.hexdigest()
	then = time.time()
	sha1Hash = hashlib.sha1(readFile.encode('utf-8'))
	sha1Hashed = sha1Hash.hexdigest()
	now = time.time()

	#print "File Name: %s" % inputFile
	#print "MD5: %r" % md5Hashed
	#print "SHA1: %r" % sha1Hashed



	with open('hasout.txt', 'a') as the_file:
	    the_file.write(sha1Hashed)

	print("check hasout.txt file to see the hashed value\n")

	print("It took ", now-then, "seconds to complete the operation")