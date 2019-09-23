from char import Char

class Alphabet(list):
	def __init__(self, data=[]):
		super(Alphabet, self).__init__(data)
		# self.insert(0, Char())
		# Adds empty character (ε) to alphabet

	def is_empty(self):
		return not len(self)

	def __repr__(self):
		return 'Alphabet<{}>'.format(', '.join(map(str, self)))