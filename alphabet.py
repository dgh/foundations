from char import Char
from string import String

from itertools import product
from math import log

class Alphabet(list):
	def __init__(self, data=[]):
		super(Alphabet, self).__init__(data)
		# self.insert(0, Char())
		# Adds empty character (ε) to alphabet

	def is_empty(self):
		return not len(self)

	def generate_nth_string(self, n):
		'''
			Find the layer(length) of the nth string is on.
			Generate the all the strings in lexi order with
			the length of the nth string. Return the nth string
			of the alphabet.
		'''
		if not n: return String([], self)
		# |A|^l
		l = int(log(n + 1, len(self))) # l = layer
		i =  n + 1 - len(self) ** l # i = layer index + 1
		return String(list(product(self, repeat=l))[i], self)
	
	def __repr__(self):
		return 'Alphabet<{}>'.format(', '.join(map(str, self)))