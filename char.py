class Char():
	def __init__(self, c=None):
		if c:
			self.c = c
			self.empty = False
		else:
			self.c = 'ε'
			self.empty = True

	def is_empty(self):
		return self.empty

	def __hash__(self):
		return hash(self.c)

	def __eq__(self, other):
		return self.c == other

	def __repr__(self):
		return self.c