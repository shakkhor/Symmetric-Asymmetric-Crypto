#https://gist.github.com/ErbaAitbayev/8f491c04af5fc1874e2b0744965a732b#file-rsa-py-L126




import random
from hashlib import sha256
import time


def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
    
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

#Euclid's extended algorithm for finding the multiplicative inverse of two numbers    
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise Exception('Modular inverse does not exist')
	return x % m    

        
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime 
    g = coprime(e, phi)
  
    while g != 1:
        e = random.randrange(1, phi)
        g = coprime(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = modinv(e, phi)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(privatek, plaintext):
    #Unpack the key into it's components
    key, n = privatek

    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
            
    numberRepr = [ord(char) for char in plaintext]
    cipher = [pow(ord(char),key,n) for char in plaintext]
    
    #Return the array of bytes
    return cipher


def decrypt(publick, ciphertext):
    #Unpack the key into its components
    key, n = publick
       
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    numberRepr = [pow(char, key, n) for char in ciphertext]
    plain = [chr(pow(char, key, n)) for char in ciphertext]

    
    #Return the array of bytes as a string
    return ''.join(plain)
    
    
def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed
    
    
def verify(f, g):
    receivedHashed=f.read()
    message=g.read()
    f.close()
    g.close()
    ourHashed = hashFunction(message)
    if receivedHashed == ourHashed:
        print("Verification successful: ", )
    else:
        
        print("Verification failed")
        

def signature():
    p = 11
    q=23
    
    

    public, private = generate_keypair(p, q)
    
    #print("Enter a message to Signature: ")
    #message = raw_input()
    #print(message)

    print("input from txt file");
    f=open('input.txt','r')
    message=f.read()
    f.close()

    then  = time.time()
    hashed = hashFunction(message)
    
    encrypted_msg = encrypt(private, hashed)   

    
    print("your message:", ' ', message)
    print("Encrypted hash:", ' ', encrypted_msg)	

    sign = decrypt(public, encrypted_msg)
    now = time.time()

    g=open('signature.txt','w')
    g.write(str(sign))
    g.close()
    
    print("")
    print("Verification process . . .")
    verify(open('signature.txt','r'), open('input.txt','r'))

    print("It took ", now-then, "seconds to complete the operation")
   

