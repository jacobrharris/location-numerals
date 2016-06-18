import argparse
import math

class LocationNumerals:
	def __init__(self):
		self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
						 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

	def method_one(self, integer):
		integers_list = self.integers_to_keep(integer)
		logs_list = self.integers_to_logs(integers_list)
		letters_list = self.logs_to_string(logs_list)
		print "Method 1: %s" % letters_list

	def method_two(self, string):
		print "Method 2: %s" % self.string_to_integer(string)
	
	def method_three(self, string):
		print "Method 3: %s" % self.convert_dupes(string)


	# List all base integers up to x
	def powers_of_2(self, x, integer_list=[]):
		log = math.floor(math.log(x, 2))
		power_of_2 = int(math.pow(2, log))

		if power_of_2 == x:
			if x == 1:
				integer_list.append(power_of_2)
				return integer_list
			else:
				return self.powers_of_2(x - 1)

		integer_list.append(power_of_2)
		return self.powers_of_2(power_of_2)

	# List the base integers that add up to x
	def integers_to_keep(self, x):
		integer_list = []
		all_powers = self.powers_of_2(x)
		for power in all_powers:
			if power + sum(integer_list) <= x:
				integer_list.append(power)
	
		integer_list.reverse()
		return integer_list

	# Convert integers to their respective logs
	def integers_to_logs(self, int_list):
		log_list = []
		for integer in int_list:
			if integer == 0:
				log_list.append(0)
			else:
				log = int(math.log(integer, 2))
				log_list.append(log)
	
		return log_list

	# Convert logs to their respective letters
	def logs_to_string(self, log_list):
		letters_list = []
		for log in log_list:
			letter = self.alphabet[log]
			letters_list.append(letter)
	
		return "".join(letters_list)

	# Convert alphabet to list of logs
	def alphabet_to_logs(self):
		logs_list = []
		for letter in self.alphabet:
			log = self.alphabet.index(letter)
			logs_list.append(log)
	
		return logs_list

	# Convert a string to an integer
	def string_to_integer(self, string):
		string_list = [letter for letter in string]
		integers_list = []
		for letter in string_list:
			integer = self.alphabet.index(letter)
			integers_list.append(integer)

		logs_list = self.integers_to_logs(integers_list)
		newInteger = 0
		for integer in integers_list:
			newInteger += 2 ** integer 
	
		return newInteger

	# Convert duplicate letters to the next letter
	def convert_dupes(self, string):
		letters_list = [letter for letter in string]
		letters_list.sort()

		currentIndex = 0
		previousLetter = ""
		for currentLetter in letters_list:
			currentIndex = letters_list.index(currentLetter)

			if currentLetter != previousLetter:
				previousLetter = currentLetter
			else:
				nextAlphabetIndex = self.alphabet.index(currentLetter) + 1
				letters_list.remove(previousLetter)
				letters_list.remove(currentLetter)
				letters_list.insert(currentIndex, self.alphabet[nextAlphabetIndex])
				newString = "".join(letters_list)
				return self.convert_dupes(newString)
	
		return "".join(letters_list)



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Convert from decimal numbers to location numerals and back.")
	parser.add_argument('-1', type=int, help="Takes an integer and returns the location numeral in abbreviated form. That is, you pass in 9 and it returns 'ad'.")
	parser.add_argument('-2', type=str, help="Takes a location numeral and returns its value as an integer. That is, you pass 'ad' in, and it returns 9.")
	parser.add_argument('-3', type=str, help="Takes a location numeral and returns it in abbreviated form. That is, you pass in 'abbc' and it returns 'ad'.")
	args = vars(parser.parse_args())

	ln = LocationNumerals()

	if args['1']:
		ln.method_one(args['1'])

	if args['2']:
		ln.method_two(args['2'])

	if args['3']:
		ln.method_three(args['3'])