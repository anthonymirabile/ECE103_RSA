#-------------------------------------------------------------------------------
# Name:        Optional RSA Exercise
# Purpose:	   Implement knowledge of RSA and standard packages to implement RSA
#			   encryption, decryption and key generation
#
# Author:      Anthony Mirabile - 20633189
#
# Created:     08/10/2016
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import random
import math
import sys
from fractions import gcd

def split(s, chunk_size):
	a = zip(*[s[i::chunk_size] for i in range(chunk_size)])
	return [''.join(t) for t in a]

def decode(code):
	code_list = split(code,3)
	decode_list = []
	
	for i in code_list:
		i = int(i)
		decode_list.append(chr(i))
		
	return "".join(decode_list)

def encode(text):
	encode_list = []
	
	for i in text:
		i = ord(i)
		encode_list.append(str(i).zfill(3))
		
	return "".join(encode_list)
			
def rabinMiller(n):
	  s = n-1
	  t = 0
	  while s&1 == 0:
			s = s/2
			t +=1
	  k = 0
	  while k<128:
			a = random.randrange(2,n-1)
			v = pow(a,s,n) #where values are (num,exp,mod)
			if v != 1:
				 i=0
				 while v != (n-1):
					  if i == t-1:
							return False
					  else:
							i = i+1
							v = (v**2)%n
			k+=2
	  return True

def isPrime(n):
	  lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
						 ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
						 ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
						 ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
						 ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
						 ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
						 ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
						 ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
						 ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
						 ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
	  if (n >= 3):
			if (n&1 != 0):
				 for p in lowPrimes:
					  if (n == p):
						  return True
					  if (n % p == 0):
							return False
				 return rabinMiller(n)
	  return False

def generateLargePrime(k):
	  #k is the desired bit length
	  r=100*(math.log(k,2)+1) #number of attempts max
	  r_ = r
	  while r>0:
			n = random.randrange(2**(k-1),2**(k))
			r-=1
			if isPrime(n) == True:
				 return n
	  return "Failure after "+`r_` + " tries."
	
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	g, y, x = egcd(b%a,a)
	return (g, x - (b//a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('No modular inverse')
	return x%m

def generateKeys():	
	p = generateLargePrime(1024)
	q = generateLargePrime(1024)
	n = p*q
	phi = (p-1)*(q-1)
	e = random.randint(70001,1000000)
	d = modinv(e, phi)
	
	print 'P =', p
	print 'Q =', q
	print 'N =', n
	print 'Phi =', phi
	print 'E =', e
	print 'D =', d
	print '(E*D) % Phi =', (e*d)%phi

def encrypt():
	m = raw_input("Type the message you would like to encrypt: ")
	e = input("Enter your encryption key (e): ")
	n = input('Enter your encryption key (n): ')	
	bigM = encode(m)
	print "BIG M=",bigM
	if bigM[0] == "0": #remove first 0, otherwise Python will interpret as an octal digit
		bigM = bigM[1::]
		print "BIG M=",bigM
	print "\nCypher text:", pow(int(bigM),e,n)	
	
def decrypt():
	c = input("Enter cypher text: ")
	d = input("Enter private key (d): " )
	n = input("Enter private key (n): ")
	m = str(pow(c,d,n))
	if len(m) % 3 != 0: #pad message with 0
		m = "0" + m
		
	print "\nOriginal message:", decode(m)
	

def main():
	print ("Type 0,1, 2 or 3 to select which task you would like to complete\n")	
	user_choice = input("Would you like to generate keys (1), encrypt a message(2), decrypt cypher text(3) or end program(0): ")

	while (user_choice != 0):
	
		if (user_choice == 1):
			connected = False

			while not connected:# may produce invalid ouptuts, therefore re-run try/catch loop until valid keys are produced
				try:
					generateKeys()
					connected = True
				except:
					continue
				break
				
			user_choice = input("\nWould you like to generate keys (1), encrypt a message(2), decrypt cypher text(3) or end program(0): ")
		elif (user_choice == 2): 
			encrypt()
			user_choice = input("\nWould you like to generate keys (1), encrypt a message(2), decrypt cypher text(3) or end program(0): ")
		elif (user_choice == 3): 
			decrypt()
			user_choice = input("\nWould you like to generate keys (1), encrypt a message(2), decrypt cypher text(3) or end program(0): ")	

#generateKeys()
main()	