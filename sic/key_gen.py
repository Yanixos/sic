#!/usr/bin/python3.6

import string, random

def count(key):
	sum = 0
	for char in key :
		sum += ord(char)
	return sum

def KeyCheck(key):
	secret_number = 1111
	sum = 0
	for char in key :
		sum += ord(char)
	if sum == secret_number ^ 5207  : 	
		return True
	else : 
		return False

if __name__ == '__main__' :

	secret_number = 1111
	import sys, os, string, random
	key = ''
	while True :
		key += random.choice(string.ascii_letters+string.digits)
		cpt = count(key)
		if cpt == secret_number ^ 5207 :
			break
		elif cpt > secret_number ^ 5207 :
			key = ''
	print(key)


