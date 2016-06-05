import argparse
import math

class Letter:
	def __init__(self, letter, index):
		self.letter = letter
		self.exponent = index
		self.position = index + 1
		
	def __str__(self):
		return self.letter
		
	__repr__ = __str__

# List all base integers up to x
def powers_of_2(x, integer_list=[]):
	log = math.floor(math.log(x, 2))
	power_of_2 = int(math.pow(2, log))

	if power_of_2 == x:
		if x == 1:
			integer_list.append(power_of_2)
			return integer_list
		else:
			return powers_of_2(x - 1)

	integer_list.append(power_of_2)
	return powers_of_2(power_of_2)

# List the base integers that add up to x
def integers_to_keep(x):
	integer_list = []
	all_powers = powers_of_2(x)
	for power in all_powers:
		if power + sum(integer_list) <= x:
			integer_list.append(power)
	
	integer_list.reverse()
	return integer_list

# Convert integers to their respective logs
def integers_to_logs(int_list):
	log_list = []
	for integer in int_list:
		if integer == 0:
			log_list.append(0)
		else:
			log = int(math.log(integer, 2))
			log_list.append(log)
	
	return log_list

# Convert logs to their respective letters
def logs_to_string(alphabet, log_list):
	letters_list = []
	for log in log_list:
		letter = alphabet[log]
		letters_list.append(letter)
	
	return "".join(letters_list)

# Convert alphabet to list of logs
def alphabet_to_logs(alphabet):
	logs_list = []
	for letter in alphabet:
		log = alphabet.index(letter)
		logs_list.append(log)
	
	return logs_list
	
def string_to_integer(alphabet, string):
	string_list = [letter for letter in string]
	integers_list = []
	for letter in string_list:
		integer = alphabet.index(letter)
		integers_list.append(integer)

	logs_list = integers_to_logs(integers_list)
	newInteger = 0
	for integer in integers_list:
		newInteger += 2 ** integer 
	
	return newInteger

if __name__ == '__main__':
	# Set up letter objects
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

	# 1
	integers_list = integers_to_keep(87)
	logs_list = integers_to_logs(integers_list)
	letters_list = logs_to_string(alphabet, logs_list)
	print letters_list
	
	# 2	
	print string_to_integer(alphabet, 'ad')