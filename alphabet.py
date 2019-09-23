from char import Char

class Alphabet():
	def __init__(self, set={}):
		self.set = set

	def is_empty(self):
		return not len(self.set)

	def __repr__(self):
		return self.set.__repr__()