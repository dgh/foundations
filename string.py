from char import Char

class String(list):
	def __init__(self, s, a):
		if isinstance(s, str):
			s = [Char(c) for c in list(s)]
		super(String, self).__init__(s)
		self.a = a
		
	def is_empty(self):
		return not len(self)

	def __repr__(self):
		return 'String<{}>'.format(''.join(map(str, self)))