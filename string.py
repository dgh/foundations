from char import Char

class String(list):
	def __init__(self, s, a):
		if isinstance(s, str):
			s = [Char(c) for c in list(s)]
		super(String, self).__init__(s)
		self.a = a
		
	def is_empty(self):
		#print(self)
		if self == [Char()]:
			# if the string is just the empty character then its empty
			return True
		return not len(self)

	def __repr__(self):
		if self.is_empty():
			return 'String<ε>'
		return f'String<{"".join(map(str, self))}>'