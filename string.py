from char import Char
from alphabet import Alphabet

class String(list):
	def __init__(self, s, a):
		super(String, self).__init__(s)
		self.a = a

	def is_empty(self):
		return not len(self.s)

	def __repr__(self):
		return 'String<{}>'.format(''.join(map(str, self)))