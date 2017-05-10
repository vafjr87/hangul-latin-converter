import korean.hangul as kr
import sys
import pickle

class romanizator(object):

	def __init__(self):
		print('Welcome to the Hangul->Latin Script Conversor 0.9\n')
		self.input = self.get_input()
		self.hangul = pickle.load(open('./hangul.dat', "rb"))
		self.output = ''

	def get_input(self):
		print('Please insert the korean text and press CTRL + D:\n')

		return sys.stdin.read().split('\n')

	def romanize(self):

		romanized_output = list()

		for sentence in self.input:
			romanized_sentence = ''
			upper = True

			blocks = list(sentence)

			for block in blocks:
				if kr.is_hangul(block):
					letters = kr.split_char(block)
					
					for i in range(len(letters)):
						if i == (len(letters) - 1): # If it's batchim
							if letters[i] != '' and letters[i] in self.hangul['batchim']:
 								romanized_sentence = romanized_sentence + self.hangul['batchim'][letters[i]]
						else:
							if upper:
								if len(self.hangul['letters'][letters[i]]) > 1:
									romanized_sentence += str.upper(self.hangul['letters'][letters[i]][0]) + \
																	self.hangul['letters'][letters[i]][1:]
								else:
									romanized_sentence += str.upper(self.hangul['letters'][letters[i]])
								
								if romanized_sentence != '':
									upper = False
							else:
								romanized_sentence += self.hangul['letters'][letters[i]]

				else:
					if block in '.!?':
						upper = True
					else:
						upper = False

					romanized_sentence += block

			romanized_output.append(romanized_sentence.strip())

		self.output = romanized_output

	def print_output(self):
		print('\nRomanized version:\n')

		for line in self.output:
			print(line)


r = romanizator()
r.romanize()
r.print_output()