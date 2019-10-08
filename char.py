class Char():
	def __init__(self, c='ε'):
		self.c = c

	def __hash__(self):
		return hash(self.c)

	def __eq__(self, other):
		return self.c == other

	def __repr__(self):
		return self.c